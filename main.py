# make a simple flet app
import flet as ft
from flet import *
from pages.courtines_quotator import Courtines_quotator
from pages.quotation_editor import Quotation_editor
from pages.products_manager import Products_manager



def main(page = Page):

  def on_change_route(route):
    print(route)
    troute = TemplateRoute(page.route)

    page.views.clear()
    page.views.append(View("/",[Courtines_quotator(page)]))
    # for each route in routes, check if the route is the same as the current route
    # if it is, then add the view to the page views
    if troute.match("/details/new"): 
      page.views.append(View("/details/new",[Quotation_editor(page)]))
    elif troute.match("/details/:details_id"):
      page.views.append(View("/details/:details_id",[Quotation_editor(page,int(troute.details_id))]))
    elif troute.match("/products"):
      page.views.append(View("/products",[Products_manager(page)]))
    elif troute.match("/products/new"):
      page.views.append(View("/products",[Products_manager(page)]))
      page.views.append(View("/products/new",[Text("New product")]))
    elif troute.match("/products/edit/:product_id"):
      page.views.append(View("/products",[Products_manager(page)]))
      page.views.append(View("/products/edit/:product_id",[Text("edit product")]))

  def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

  page.on_route_change = on_change_route
  page.on_view_pop = view_pop 
  page.padding = 0
  page.margin = 0
  page.go("/products")


ft.app(main)
# 1080*2400 dimensions