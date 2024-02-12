from flet import *
import flet as ft
from classes.quotation_class import Quotation_class
import random
from functions.string_functions  import put_points
from data.gspread_provider import delete_quotation as delete_quotation_gspread
from data.gspread_provider import get_quotation_product_quotations

class Quotation_card(UserControl):
  def __init__(self,page,quotation:Quotation_class):
    super().__init__()
    self.quotation = quotation
    self.products_amount = random.randint(2,10)
    self.page = page

  def delete_quotation(self,id_quotation_to_del:int):
     delete_quotation_gspread(
       id_quotation_to_del=id_quotation_to_del,
       quotation_product_quotations=get_quotation_product_quotations()
     )
     self.page.update()
     self.page.go("/")

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
                  IconButton(icon=icons.DELETE,on_click=lambda _: self.delete_quotation(self.quotation.quotation_id))
                ],col=2,alignment=CrossAxisAlignment.END),
              ]),

              Text(f"#{self.products_amount} products",color=colors.GREY_700),

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
  