from flet import *
from components.menu import Menu
from constants.style_cosntants import bottom_padding
from data.products_provider import get_products
from components.product_component import Product_component

class Products_manager(UserControl):
  def __init__(self,page):
    super().__init__()
    self.page = page
    self.products = get_products()

  def build(self):
    return SafeArea(
      Container(
        Column([
          Menu(self.page),
          Text("Products",size=30),
          Divider(),
          Column([
            Column([Product_component(product) for product in self.products]),
            IconButton(icon=icons.ADD,on_click=lambda _: self.page.go("/products/new"),icon_size=40)
          ],horizontal_alignment="center")
        ],),
        padding=padding.only(bottom=bottom_padding)
      )
    )

