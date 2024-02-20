from classes.product_class import Product
from classes.product_quotation_class import Product_quotation_class
from functools import reduce
class Quotation_class():
  def __init__(
      self,
      name:str,
      quotation_id:int,
      product_quotations_objs:list[Product_quotation_class] = [],
      quotation_product_quotations_objs:list[dict] = []
      ):
    

    self.quotation_id = quotation_id
    self.name = name
    self.price = 0
    self.total_products = 0

    self.products_quotations_ids = []
    for qpq in quotation_product_quotations_objs:
      if qpq["id_quotation"] == self.quotation_id:
        self.products_quotations_ids.append(qpq["id_product_quotation"])


    self.products_quotations = [
      pq for pq in product_quotations_objs
      if pq.id_product_quotation in self.products_quotations_ids
    ]
    





  def __str__(self):
    return f'{self.quotation_id}) Quotation_class({self.name},{self.price})'