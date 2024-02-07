from flet import *
from data.products_provider import get_products
from classes.product_quotation_class import Product_quotation_class
class Product_quotation_component(UserControl):
  def __init__(self,id_product=None,amount=1):
    super().__init__()
    self.id_product = id_product
    self.amount = amount
    self.products = get_products()
    self.amount_component_ref = Ref[TextField]()

    # print([p.name for p in self.products],sep="\n")

  def product_changed(self,e):
    amount_field = self.amount_component_ref.current
    product = list(filter(lambda p: p.name == e.control.value,self.products))[0]
    self.id_product = product.id_product
    amount_field.label = product.unit
    print(product.unit)
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
      id_product=self.id_product,
      amount=self.amount
    )

  def build(self):
    return ResponsiveRow(
            [
              Dropdown(
                hint_text="Select a product",
                options=[dropdown.Option(p.name) for p in self.products],
                col=7,
                on_change=self.product_changed,
              ),
              TextField(ref=self.amount_component_ref,col=3,keyboard_type=KeyboardType.NUMBER,value=self.amount,on_change=lambda e: self.amount_changed()),
              Column([
                IconButton(on_click=lambda e: self.amount_changed(1),style=ButtonStyle(padding=padding.all(0)),icon_size=15,icon=icons.ADD),
                IconButton(on_click=lambda e: self.amount_changed(-1),style=ButtonStyle(padding=padding.all(0)),icon_size=15,icon=icons.REMOVE)
              ],col=2,spacing=0)
            ],
            spacing=0,vertical_alignment="center"
          )
          