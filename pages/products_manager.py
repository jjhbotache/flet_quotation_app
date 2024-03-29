from flet import *
from components.menu import Menu
from constants.style_cosntants import bottom_padding
from data.products_provider import get_products
from data.gspread_provider import update_product,create_product,delete_product
from components.product_component import Product_component
from threading import Thread

class Products_manager(UserControl):
  def __init__(self,page, **kwargs):
    super().__init__()
    self.page = page
    self.products = []

    self.products_column_ref = Ref[Column]()


    # self.products = []
    self.products = get_products()

    

    try: self.product_id = kwargs["product_id"]
    except: self.product_id = None
    try: self.new = kwargs["new"]
    except: self.new = False


    # editor refs
    self.product_name_ref = Ref[TextField]()
    self.product_price_ref = Ref[TextField]()
    self.product_unit_ref = Ref[TextField]()

  def on_create_product(self,data):
    print(data)

  def on_delete_product(self,id_product):
    delete_product(id_product)
    self.products = list(filter(lambda p: p.id_product != id_product,self.products))
    self.page.go("/")
    print("deleted product with id: ",id_product)

  def build(self):

    products_viewer = SafeArea(
      Container(
        Column([
          Menu(self.page),
          Text("Products",size=30),
          Divider(),
          Column([
            Column(
              [Product_component(
                product=product,
                on_delete_product=lambda product: self.on_delete_product(product.id_product),
              ) for product in self.products],
              scroll=ScrollMode.ALWAYS,
              height=self.page.height-300,
              width=float("inf"),
              ref=self.products_column_ref
            ),
            IconButton(icon=icons.ADD,on_click=lambda _: self.page.go("/products/new"),icon_size=40)
          ],horizontal_alignment="center")
        ],
        ),
        padding=padding.only(bottom=bottom_padding)
      )
    )
    # ------------------------------------------------------------------------
    def products_editor(id_product=None): 

      product = None
      if id_product:
        product = next((product for product in self.products if product.id_product == id_product),None)
        # print(product)

      def save_or_create_product(action):
        data = {
          "id_product": id_product,
          "name": self.product_name_ref.current.value,
          "price": self.product_price_ref.current.value,
          "unit": self.product_unit_ref.current.value
        }
        if action == "save":
          print("saving product")
          update_product(id_p=int(data["id_product"]),data_dict=data)
          self.page.go("/products")
          
        elif action == "create":
          print("creating product")
          create_product(
            name=data["name"],
            price=data["price"],
            unit=data["unit"]
          )
          self.page.go("/products")
        
        print(data)
        # here goes the logic to save the data

      return SafeArea(
        Container(
          Column([
            Menu(self.page),
            Text("Product creator",size=30),
            Divider(),
            TextField(label="Product name",ref=self.product_name_ref,value=product.name if product else None),
            TextField(label="Unit",ref=self.product_unit_ref,value= product.unit if product else None),
            TextField(label="Price per unit",ref=self.product_price_ref,value= product.price if product else None),
            ResponsiveRow([
              ElevatedButton("Save",on_click=lambda _:save_or_create_product("save"if product else "create")),
              ElevatedButton("Cancel",on_click=lambda _: self.page.go("/products"))
            ],alignment="center")
          ]),
          padding=padding.only(bottom=bottom_padding)
        )
      )
    # ------------------------------------------------------------------------
    to_render = None

    if not self.new and not self.product_id:
      to_render = products_viewer
    elif self.new:
      to_render = products_editor()
    elif self.product_id:
      to_render = products_editor(self.product_id)

      
    return to_render

