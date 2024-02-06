from flet import *
from data.quotations_provider import get_quotations
from components.product_quotation_component import Product_quotation_component
from classes.product_quotation_class import Product_quotation_class
from data.products_provider import get_products
import random

class New_quotation(UserControl):
  def __init__(self,page):
    super().__init__()
    self.page = page
    self.products_quotations = Ref[Column]()
    self.quotation_name = ""
    self.quotation_price = 0
    self.list_of_product_quotation_ids = set()
    self.products = get_products()

  def add_product_quotation(self,e):
    # create a new product quotation obj
    # add it to the list of product quotations
    # update the view


    self.products_quotations.current.controls.append(
      Product_quotation_component(on_change=lambda x: print(x))
    )
    self.products_quotations.current.update()


  def build(self):
    return SafeArea(
      Container(
      Column(
        [
          TextField(value=self.quotation_name,hint_text="Quotation name"),
          Container(
          Column([
            
          ],
          ref=self.products_quotations,scroll=ScrollMode.ALWAYS,height=self.page.height-220,width=float("inf"),horizontal_alignment="center",spacing=0),
          bgcolor=colors.GREY_800,
          ),
          Text(f"Total: {self.quotation_price}",size=20),
          IconButton(icon_color="black",bgcolor=colors.GREY_100,icon=icons.ADD,on_click=self.add_product_quotation),
          ElevatedButton("Save",on_click=lambda _: self.page.go("/")), 
        ],
        horizontal_alignment="center",
        height=self.page.height-15,
        width=float("inf"),
      ),
      bgcolor=colors.GREY_900
      )
    )
