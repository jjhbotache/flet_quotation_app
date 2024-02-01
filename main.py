# make a simple flet app
import flet as ft
from main_component import (Courtines_quotator,Nav)
from flet import(
  AppBar
)

def main(page = ft.Page):
  page.scroll = ft.ScrollMode.ADAPTIVE
  page.appbar = ft.AppBar(title=Nav())
  page.add(Courtines_quotator())

ft.app(main)

