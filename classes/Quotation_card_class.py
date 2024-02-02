class Quotation_card_class():
  def __init__(self,name:str,price:int,quotation_id:int):
    self.name = name
    self.price = price
    self.quotation_id = quotation_id

  def __str__(self):
    return f'{self.quotation_id}Quotation_card_class({self.name},{self.price})'