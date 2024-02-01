# make a simple flet app
import flet as ft
from main_component import *
from flet import *



def main(page = ft.Page):
  routes = [
      View("/",[Courtines_quotator(page)],appbar=Nav(page)),
      View("/details",[Details(page)],appbar=Nav(page)),
  ]


  page.scroll = ft.ScrollMode.ADAPTIVE

  

  def on_change_route(e):
    print(e)
    print('route change attempt')
    page.views.clear()
    page.views.append(routes[0])
    if page.route == "/details":
      page.views.append(routes[1])
    page.update()

  def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

  page.on_route_change = on_change_route
  page.on_view_pop = view_pop 

  

  page.go("/")

ft.app(main)
