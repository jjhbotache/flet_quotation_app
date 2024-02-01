from flet import (
  UserControl,
  Card,
  Column,
  Text,
)
from classes.Quotation_card_class import Quotation_card_class

class Quotation_card(UserControl):
  def __init__(self,quotation:Quotation_card_class):
    super().__init__()
    self.quotation = quotation


    
  def build(self):
    
    return Card(
      Column([
        Text(self.quotation.name),
        Text(self.quotation.price),
      ],expand=True,col=12),
    expand=True,col=12)