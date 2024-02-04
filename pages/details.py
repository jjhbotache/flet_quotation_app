from flet import *
from data.quotations_provider import get_quotations

class Details(UserControl):
  def __init__(self,page,details_id):
    super().__init__()
    self.page = page
    self.quotation = list(filter(lambda q: q.quotation_id == details_id,get_quotations()))[0]


  def build(self):
    return Container(
      Column(
        [
          Text(f"{self.quotation.name}",color=colors.GREY_100,size=40),
          ElevatedButton("change route",on_click=lambda _: self.page.go("/")),
        ],
        horizontal_alignment=CrossAxisAlignment.CENTER,
      ),
      width=float('inf'),
      height=self.page.height,
      bgcolor=colors.GREY_900,
    )
