import flet as ft
from components.Quotation_card import Quotation_card
from classes.Quotation_card_class import Quotation_card_class
from flet import *

class Courtines_quotator(UserControl):
  def __init__(self,page):
    super().__init__()
    self.page = page

  
  def change_route(self,e):
    self.page.go("/details")
    self.page.update()

  def build(self):
    quotation_cards = [
      Quotation_card_class('Producto A', 150),
      Quotation_card_class('Producto B', 200),
      Quotation_card_class('Producto C', 180),
      Quotation_card_class('Producto D', 220),
      Quotation_card_class('Producto E', 170),
      Quotation_card_class('Producto F', 190),
      Quotation_card_class('Producto G', 210),
      Quotation_card_class('Producto H', 160),
      Quotation_card_class('Producto I', 230),
      Quotation_card_class('Producto J', 240)
    ]
    return Container(
      Column(
        [
          ElevatedButton("change route",on_click=self.change_route),
          *[Quotation_card(quotation) for quotation in quotation_cards],
        ],
      ),
    )
  
class Details(UserControl):
  def __init__(self,page):
    super().__init__()
    self.page = page

  def change_route(self,e):
    print('change route from details')
    self.page.go("/")
    self.page.update()

  def build(self):
    return Container(
      Column(
        [
          Text("Details"),
          ElevatedButton("change route",on_click=self.change_route),
        ],
      ),
    )
  


def Nav(page):
  return AppBar(title=SafeArea(
      ResponsiveRow([
        PopupMenuButton(col=2,icon=ft.icons.TABLE_ROWS,items=[PopupMenuItem(text='Cortinas', icon=ft.icons.CLEAR_ALL_OUTLINED),PopupMenuItem(text='Cotizaciones', icon=ft.icons.OTHER_HOUSES_ROUNDED),]),
        TextField(col=10,label='Enter your name',hint_text='Your name')
      ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN,vertical_alignment=ft.CrossAxisAlignment.CENTER),
    )
  )
  

  