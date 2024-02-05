from flet import (
  ResponsiveRow,
  PopupMenuButton,
  PopupMenuItem,
  TextField
)
import flet as ft

class Menu(ft.UserControl):
  def build(self):
    return PopupMenuButton(col=5,icon=ft.icons.TABLE_ROWS,items=[PopupMenuItem  (text='Cortinas', icon=ft.icons.CLEAR_ALL_OUTLINED),PopupMenuItem(text='Cotizaciones', icon=ft.icons.OTHER_HOUSES_ROUNDED),])