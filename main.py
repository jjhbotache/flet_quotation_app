# make a simple flet app
import flet as ft
from main_component import *
from flet import *



def main(page = Page):

  

  def on_change_route(e):
    print(e)
    print('route change attempt')
    troute = TemplateRoute(page.route)

    page.views.clear()
    page.views.append(View("/",[Courtines_quotator(page)],appbar=Nav(page),scroll=ScrollMode.ADAPTIVE))

    # for each route in routes, check if the route is the same as the current route
    # if it is, then add the view to the page views
    if troute.match("/details/:details_id"):
      page.views.append(View("/details/:details_id",[Details(page,int(troute.details_id))],appbar=Nav(page)))

  def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

  page.on_route_change = on_change_route
  page.on_view_pop = view_pop 

  

  page.go("/")

ft.app(main)
