from flet import *
from data.quotations_provider import get_quotations
from components.quotation_card import Quotation_card  
from components.menu import Menu
from constants.style_cosntants import bottom_padding
from threading import Thread
import time

class Courtines_quotator(UserControl):
  def __init__(self,page):
    super().__init__()
    self.page = page
    # self.quotations = []
    self.quotations = get_quotations()

    self.columnRef = Ref[Column]()


    self.quotations_to_render = self.quotations
    self.quotations_column = Column(width=float("inf"),scroll=ScrollMode.ADAPTIVE,horizontal_alignment="center")
    self.quotations_column.controls = [Quotation_card(self.page,quotation) for quotation in self.quotations_to_render]

    
    def render_quotations():
      time.sleep(2)
      self.columnRef.current.controls = [
        Text("No quotations found",color="red",size=30,text_align="center",expand=True)
      ]
      self.columnRef.current.update()
      print("rendering quotations")
      # self.quotations = get_quotations()
      # self.quotations_column.controls = [
      #   Quotation_card(self.page,quotation) for quotation in self.quotations_to_render
      #   ]
      # self.quotations_column.update()
      # self.update()
      pass

    Thread(target=lambda:render_quotations()).start()
  
  def build(self):

    def filter_quotations(e):
      if e.control.value == "": 
        quotations_to_render = [Quotation_card(self.page,quotation) for quotation in self.quotations]
      else:
        # reset the value of the control to the strip value
        e.control.value = e.control.value.strip()
        quotations_to_render = [Quotation_card(self.page,quotation) for quotation in self.quotations if e.control.value.lower().strip() in quotation.name.lower().strip()]

        if quotations_to_render == []:
          quotations_to_render = [
            Container(Text("No quotations found",color="red",size=30,text_align="center",expand=True),padding=padding.only(top=20))
            ]


      e.control.update()
      self.quotations_column.controls = quotations_to_render
      # self.quotations_column.update()
      self.update()



    total_height = self.page.height-12
    
    return SafeArea(
            Stack([
            Column(
              [
                Row([
                  Menu(self.page),
                  TextField(label="Search",expand=True,on_change=filter_quotations),
                ],),
                Container(
                  self.quotations_column,
                  bgcolor="grey800",
                  expand=True,
                  ref= self.columnRef
                ),
              ],
              height=total_height,
            ),
            FloatingActionButton(icon=icons.ADD,bottom=20,right=20,on_click=lambda _: self.page.go("/details/new")),
            ],
            height=total_height-bottom_padding,
            ),
            expand=True,
            maintain_bottom_view_padding=True,
          )
  