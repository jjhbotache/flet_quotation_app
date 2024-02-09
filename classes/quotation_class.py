from data.products_quotations_provider import get_products_quotations
class Quotation_class():
  def __init__(self,name:str,price:int,quotation_id:int,products_quotations:list[int] = []):
    self.quotation_id = quotation_id
    self.name = name

    products_objs = get_products_quotations()
    # no in the db:
    self.products_quotations = [
      # Product_quotation_class(...)
      pq for pq in products_objs if pq.id_product in products_quotations

    ]
    self.price = price # price of the whole quotation is calculated 


  def __str__(self):
    return f'{self.quotation_id}) Quotation_class({self.name},{self.price})'