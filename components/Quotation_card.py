from flet import *
import flet as ft
from classes.Quotation_card_class import Quotation_card_class
import random

class Quotation_card(UserControl):
  def __init__(self,quotation:Quotation_card_class):
    super().__init__()
    self.quotation = quotation
    self.products_amount = random.randint(2,10)


    
  def build(self):
    
    return Card(
        Container(
          ResponsiveRow([
            Column([


              Text(self.quotation.name),

              Text(f"#{self.products_amount} products",color=colors.GREY_700),

              Container(
                Column([Text(f"$ {self.quotation.price}.000"),
                ],horizontal_alignment=CrossAxisAlignment.END),
                width=float('inf'),
              )
            ],col=12,spacing=0),
          ]),
          padding=12,
        ),
        elevation=2,
        width=float('inf'),
      )
  