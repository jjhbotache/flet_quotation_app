from data.products_quotations_provider import get_products_quotations
from classes.product_class import Product
from classes.product_quotation_class import Product_quotation_class
from functools import reduce
class Quotation_class():
  def __init__(self,name:str,quotation_id:int,products_objs:list[Product],product_quotations_objs:list[Product_quotation_class],quotation_product_quotations_objs:list[dict]):
    self.quotation_id = quotation_id
    self.name = name
    self.price = 0

    # get the products_quotations_ids
    self.products_quotations_ids = [ qpq["id_product_quotation"] for qpq in quotation_product_quotations_objs if qpq["id_quotation"] == self.quotation_id]


    self.products_quotations = []
    for pq_id in self.products_quotations_ids:
      x = [pq for pq in product_quotations_objs if pq.id_product_quotation == pq_id]
      if len(x) > 0: self.products_quotations.append(x)
    # price of the whole quotation is calculated 
    # self.price = reduce(
    #   lambda acc,pq: acc + pq.amount * list(filter(lambda p: p.id_product == pq.id_product,products_objetcs))[0].price,
    #   self.products_quotations,
    #   0
    # )
    




  def __str__(self):
    return f'{self.quotation_id}) Quotation_class({self.name},{self.price})'