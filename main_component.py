import flet as ft
from components.Quotation_card import Quotation_card
from classes.Quotation_card_class import Quotation_card_class
from flet import (
  UserControl,
  SafeArea,
  TextField,
  Container,
  PopupMenuButton,
  PopupMenuItem,
  ResponsiveRow,
  Column,
  Text,
)

class Courtines_quotator(UserControl):

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
    return ResponsiveRow([
      Column([
        Quotation_card(qc) for qc in quotation_cards
      ],col=12)
    ])
  
class Nav(UserControl):

  def build(self):
    return SafeArea(
      ResponsiveRow([
        PopupMenuButton(col=2,icon=ft.icons.TABLE_ROWS,items=[PopupMenuItem(text='Cortinas', icon=ft.icons.CLEAR_ALL_OUTLINED),PopupMenuItem(text='Cotizaciones', icon=ft.icons.OTHER_HOUSES_ROUNDED),]),
        TextField(col=10,label='Enter your name',hint_text='Your name')
      ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN,vertical_alignment=ft.CrossAxisAlignment.CENTER),
    )