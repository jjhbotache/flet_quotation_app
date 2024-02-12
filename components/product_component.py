from flet import *
from classes.product_class import Product
from data.gspread_provider import delete_product

class Product_component(UserControl):
  def __init__(self, product):
    super().__init__()
    self.product = product

  def on_edit_product(self,product):
    self.page.go("/products/edit/"+str(product.id_product))
  
  def on_delete_product(self,product):
    print("deleting product")
    delete_product(product.id_product)


  def build(self):
    return Card(
      Container(
        Column([
          ResponsiveRow([
            Text(self.product.name,size=30,col=10),
            IconButton(icon=icons.DELETE,col=2, on_click=lambda _: self.on_delete_product(self.product) )
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