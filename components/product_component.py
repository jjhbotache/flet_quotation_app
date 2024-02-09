from flet import *
from classes.product_class import Product

class Product_component(UserControl):
  def __init__(self, product):
    super().__init__()
    self.product = product

  def on_edit_product(self,product):
    self.page.go("/products/edit/"+str(product.id_product))

  def build(self):
    return Card(
      Container(
        Column([
          ResponsiveRow([
            Text(self.product.name,size=30,col=10),
            IconButton(icon=icons.DELETE,col=2)
          ]),
          ResponsiveRow([
            Column([
              Text("Unit: "+str(self.product.unit)),
              Text("Price per unit: "+str(self.product.price))
            ],col=10),
            IconButton(icon=icons.EDIT,col=2, on_click=lambda _: self.on_edit_product(self.product))
          ],vertical_alignment="center"),
        ]),
        padding=padding.all(10)
      ),
      width=float("inf"),
    )