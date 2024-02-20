from flet import *
import flet as ft
from classes.quotation_class import Quotation_class
import random
from functions.string_functions  import put_points



class Quotation_card(UserControl):
  def __init__(self,page,quotation:Quotation_class,on_delete=None):
    super().__init__()
    self.quotation = quotation
    self.total_products = quotation.total_products or 0
    self.page = page
    self.on_delete = lambda: on_delete(quotation)

     

  def build(self):
    return Card(
        Container(
          ResponsiveRow([
            Column([
              ResponsiveRow([
                Column([
                  Text(f"{self.quotation.quotation_id}) {self.quotation.name}"),
                ],col=10),
                Column([
                  IconButton(icon=icons.DELETE,on_click=lambda _: self.on_delete()),
                ],col=2,alignment=CrossAxisAlignment.END),
              ]),

              Text(f"#{self.total_products} products",color=colors.GREY_700),

              Container(
                Column([Text(f"$ {put_points(self.quotation.price*1000)}"),
                ],horizontal_alignment=CrossAxisAlignment.END),
                width=float('inf'),
              )
            ],col=12,spacing=0),
          ]),
          padding=12,
          on_click=lambda _: self.page.go(f"/details/{self.quotation.quotation_id}"),
        ),
        elevation=2,
        width=float('inf'),
      )
  