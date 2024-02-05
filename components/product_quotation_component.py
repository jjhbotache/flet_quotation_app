from flet import *
from data.products_provider import get_products

class Product_quotation_component(UserControl):
  def __init__(self,id_product=0,amount=0):
    super().__init__()
    self.id_product = id_product
    self.amount = amount
    self.products = get_products()
    print([p.name for p in self.products],sep="\n")

  def product_changed(self,e):
    print(e.control.value)
    # update the 

  def build(self):
    return ResponsiveRow(
            [
              Dropdown(
                label="Product",
                hint_text="Select a product",
                options=[dropdown.Option(p.name) for p in self.products],
                col=8,
                on_change=self.product_changed
              ),
              TextField(col=2,keyboard_type=KeyboardType.NUMBER,value=self.amount),
              Column([
                IconButton(style=ButtonStyle(padding=padding.all(0)),icon_size=15,icon=icons.ADD),
                IconButton(style=ButtonStyle(padding=padding.all(0)),icon_size=15,icon=icons.REMOVE)
              ],col=2,spacing=0)
            ],
            spacing=0,vertical_alignment="center"
          )
          