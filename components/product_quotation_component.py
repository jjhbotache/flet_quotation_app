from flet import *
from data.products_provider import get_products
from classes.product_quotation_class import Product_quotation_class
class Product_quotation_component(UserControl):
  # def __init__(self,id_product=None,amount=1):
  def __init__(self,product_quotation=None,on_delete_product_quotation=None):
    super().__init__()
    self.id_product_quotation =product_quotation.id_product if product_quotation != None else None
    self.amount = product_quotation.amount if product_quotation != None else 1
    self.product_quotation = product_quotation
    self.products = get_products()
    self.current_product = None
    self.amount_component_ref = Ref[TextField]()

    self.delete_product_quotation = on_delete_product_quotation

    if self.id_product_quotation != None:
      self.current_product = list(filter(lambda p: p.id_product == self.id_product_quotation,self.products))[0]

    # print([p.name for p in self.products],sep="\n")

  def product_changed(self,e):
    amount_field = self.amount_component_ref.current
    product = list(filter(lambda p: p.name == e.control.value,self.products))[0]
    self.id_product_quotation = product.id_product
    amount_field.label = product.unit
    amount_field.update()

  def amount_changed(self,add_or_remove=0):
    amount_field = self.amount_component_ref.current
    # first if it's not a number, set the number before
    if add_or_remove == 0:
      try:
        self.amount = int(amount_field.value)
      except:
        amount_field.value = self.amount
        amount_field.update()
        return
    else:
      self.amount += add_or_remove
      amount_field.value = self.amount
      

    amount_field.update()

  def get_data(self):
    return Product_quotation_class(
      id_product=self.id_product_quotation,
      amount=self.amount
    )

  

  def build(self):
    print(self.current_product)
    return ResponsiveRow(
            [
              Dropdown(
                hint_text= self.current_product.name if self.current_product != None else "Select a product",
                options=[dropdown.Option(p.name) for p in self.products],
                col=6,
                on_change=self.product_changed,
              ),
              TextField(ref=self.amount_component_ref,col=3,keyboard_type=KeyboardType.NUMBER,value=self.amount,on_change=lambda e: self.amount_changed(),label=self.current_product.unit if self.current_product != None else "??"),
              Column([
                IconButton(on_click=lambda e: self.amount_changed(1),style=ButtonStyle(padding=padding.all(0)),icon_size=15,icon=icons.ADD),
                IconButton(on_click=lambda e: self.amount_changed(-1),style=ButtonStyle(padding=padding.all(0)),icon_size=15,icon=icons.REMOVE)
              ],col=2,spacing=0),
              IconButton(icon=icons.DELETE,on_click=self.delete_product_quotation,col=1)
            ],
            spacing=0,vertical_alignment="center"
          )
          