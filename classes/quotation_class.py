class Quotation_class():
  def __init__(self,name:str,price:int,quotation_id:int):
    self.quotation_id = quotation_id
    self.name = name
    self.price = price # price of the whole quotation is calculated 

  def __str__(self):
    return f'{self.quotation_id}Quotation_card_class({self.name},{self.price})'