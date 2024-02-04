import flet as ft
from components.quotation_card import Quotation_card
from classes.quotation_card_class import Quotation_card_class
from flet import *
import random,os
from data.quotations_provider import get_quotations

class Courtines_quotator(UserControl):
  def __init__(self,page):
    super().__init__()
    self.page = page
  
  def build(self):
    quotation_cards = get_quotations()
    quotations_to_render = quotation_cards

    return Container(
      Column(
        [
          *[Quotation_card(self.page,quotation_obj) for quotation_obj in quotations_to_render],
        ],
      ),
    )
  
class Details(UserControl):
  def __init__(self,page,details_id):
    super().__init__()
    self.page = page
    self.quotation = list(filter(lambda q: q.quotation_id == details_id,get_quotations()))[0]


  def build(self):
    return Container(
      Column(
        [
          Text(f"{self.quotation.name}",color=colors.GREY_100,size=40),
          ElevatedButton("change route",on_click=lambda _: self.page.go("/")),
        ],
        horizontal_alignment=CrossAxisAlignment.CENTER,
      ),
      width=float('inf'),
      height=self.page.height,
      bgcolor=colors.GREY_900,
    )

def Nav(page):
  return AppBar(title=SafeArea(
      ResponsiveRow([
        PopupMenuButton(col=2,icon=ft.icons.TABLE_ROWS,items=[PopupMenuItem(text='Cortinas', icon=ft.icons.CLEAR_ALL_OUTLINED),PopupMenuItem(text='Cotizaciones', icon=ft.icons.OTHER_HOUSES_ROUNDED),]),
        TextField(col=10,label='Enter your name',hint_text='Your name')
      ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN,vertical_alignment=ft.CrossAxisAlignment.CENTER),
    )
  )
  

  