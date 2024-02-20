from flet import *
from classes.product_class import Product
from data.gspread_provider import delete_product
from functions.string_functions import put_points

class Product_component(UserControl):
  def __init__(self, product,on_edit_product=None,on_delete_product=None):
    super().__init__()
    self.product = product
    self.on_edit_product = on_edit_product
    self.on_delete_product = on_delete_product

  def on_edit_product(self,product):
    self.page.go("/products/edit/"+str(product.id_product))
  
  def on_delete_product(self,product):
    print("deleting product")
    self.on_delete_product(product)


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
              Text("Price per unit: "+ put_points(self.product.price))
            ],col=10),
            IconButton(icon=icons.EDIT,col=2, on_click=lambda _: self.on_edit_product(self.product))
          ],vertical_alignment="center"),
        ]),
        padding=padding.all(10)
      ),
      width=float("inf"),
    )