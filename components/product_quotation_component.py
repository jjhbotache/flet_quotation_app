from flet import *
from data.products_provider import get_products
from classes.product_quotation_class import Product_quotation_class
class Product_quotation_component(UserControl):
  def __init__(self,on_change:callable,id_product=None,amount=1):
    super().__init__()
    self.id_product = id_product
    self.amount = amount
    self.products = get_products()
    self.on_change = on_change
    self.amount_component_ref = Ref[TextField]()

    # print([p.name for p in self.products],sep="\n")

  def product_changed(self,e):
    self.id_product = list(filter(lambda p: p.name == e.control.value,self.products))[0].id_product
    self.whole_data_changed()
  def amount_changed(self,add_or_remove=0):
    # first if it's not a number, set the number before
    if add_or_remove == 0:
      if isinstance(self.amount_component_ref.current.value,int):
        self.amount = self.amount_component_ref.current.value
      else:
        self.amount_component_ref.current.value = self.amount
        return
    else:
      self.amount += add_or_remove
      self.amount_component_ref.current.value = self.amount
      

    self.amount_component_ref.current.update()
    self.whole_data_changed()


  def whole_data_changed(self):
    product_quotation_to_send = Product_quotation_class(
      id_product=self.id_product,
      amount=self.amount
    )
    if self.on_change: self.on_change(product_quotation_to_send)

  def build(self):
    return ResponsiveRow(
            [
              Dropdown(
                # label="Product",
                # hint_text="Select a product",
                options=[dropdown.Option(p.name) for p in self.products],
                col=8,
                on_change=self.product_changed,
              ),
              TextField(ref=self.amount_component_ref,col=2,keyboard_type=KeyboardType.NUMBER,value=self.amount,on_change=lambda e: self.amount_changed()),
              Column([
                IconButton(on_click=lambda e: self.amount_changed(1),style=ButtonStyle(padding=padding.all(0)),icon_size=15,icon=icons.ADD),
                IconButton(on_click=lambda e: self.amount_changed(-1),style=ButtonStyle(padding=padding.all(0)),icon_size=15,icon=icons.REMOVE)
              ],col=2,spacing=0)
            ],
            spacing=0,vertical_alignment="center"
          )
          