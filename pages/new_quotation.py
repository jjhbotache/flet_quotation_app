from flet import *
from data.quotations_provider import get_quotations
from components.product_quotation_component import Product_quotation_component
import random

class New_quotation(UserControl):
  def __init__(self,page):
    super().__init__()
    self.page = page
    self.products_quotations = Ref[Column]()

  def add_product_quotation(self,e):
    self.products_quotations.current.controls.append(
      Product_quotation_component()
    )
    self.products_quotations.current.update()


  def build(self):
    return SafeArea(
      Container(
      Column(
        [
          Text("New Quotation",size=30),
          Container(
          Column([
            
          ],
          ref=self.products_quotations,scroll=ScrollMode.ALWAYS,height=self.page.height-170,width=float("inf"),horizontal_alignment="center",spacing=0),
          bgcolor=colors.GREY_800,
          ),
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
