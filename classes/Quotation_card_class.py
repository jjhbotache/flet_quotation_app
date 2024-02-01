class Quotation_card_class():
  def __init__(self,name,price):
    self.name = name
    self.price = price

  def __str__(self):
    return f'Quotation_card_class({self.name},{self.price})'