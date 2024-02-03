from flet import *
import flet as ft
from classes.Quotation_card_class import Quotation_card_class
import random
from functions.string_functions  import put_points

class Quotation_card(UserControl):
  def __init__(self,page,quotation:Quotation_card_class):
    super().__init__()
    self.quotation = quotation
    self.products_amount = random.randint(2,10)
    self.page = page

  def build(self):
    return Card(
        Container(
          ResponsiveRow([
            Column([

              Text(f"{self.quotation.quotation_id}) {self.quotation.name}"),

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
  