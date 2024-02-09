from flet import (
  ResponsiveRow,
  PopupMenuButton,
  PopupMenuItem,
  TextField
)
import flet as ft

class Menu(ft.UserControl):
  def __init__(self, page):
    super().__init__()
    self.page = page

  def build(self):
    return PopupMenuButton(
      col=5,
      icon=ft.icons.TABLE_ROWS,
      items=[
        PopupMenuItem(
          text='Productos',
          icon=ft.icons.CLEAR_ALL_OUTLINED,
          on_click=lambda e: self.page.go("/products")
        ),
        PopupMenuItem(
          text='Cotizaciones',
          icon=ft.icons.OTHER_HOUSES_ROUNDED,
          on_click=lambda e: self.page.go("/")
        ),
      ]
      )