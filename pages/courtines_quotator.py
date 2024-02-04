from flet import *
from data.quotations_provider import get_quotations
from components.quotation_card import Quotation_card  
from components.menu import Menu

class Courtines_quotator(UserControl):
  def __init__(self,page):
    super().__init__()
    self.page = page
  
  def build(self):
    quotation_cards = get_quotations()
    quotations_to_render = quotation_cards

    total_height = self.page.height-12
    return SafeArea(
            Column(
              [
                Row([
                  Menu(self.page),
                  TextField(label="Search",expand=True),
                ],),
                Container(
                  Column(
                    [*[Quotation_card(self.page,quotation_obj) for quotation_obj in quotations_to_render],]
                    ,scroll=ScrollMode.ADAPTIVE,
                  ),
                  bgcolor="grey800",
                  expand=True,
                )
              ],
              height=total_height,
            ),
            expand=True
          )
  