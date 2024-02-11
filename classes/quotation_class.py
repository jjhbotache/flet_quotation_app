from data.products_quotations_provider import get_products_quotations
from classes.product_class import Product
from classes.product_quotation_class import Product_quotation_class
from functools import reduce
class Quotation_class():
  def __init__(self,name:str,quotation_id:int,products_objs:list[Product],product_quotations_objs:list[Product_quotation_class]):
    self.quotation_id = quotation_id
    self.name = name

    # just get the products_quotations wich id_quotation is the same as the quotation_id
    self.products_quotations = [ p for p in product_quotations_objs if p.id_product_quotation == self.quotation_id ]


    # price of the whole quotation is calculated 
    # self.price = reduce(
    #   lambda acc,pq: acc + pq.amount * list(filter(lambda p: p.id_product == pq.id_product,products_objetcs))[0].price,
    #   self.products_quotations,
    #   0
    # )
    self.price = 0




  def __str__(self):
    return f'{self.quotation_id}) Quotation_class({self.name},{self.price})'