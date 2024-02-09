from classes.product_quotation_class import Product_quotation_class
import random

def get_products_quotations():
  return [
    Product_quotation_class(
      id_product_quotation=i+1,
      id_product=i+1,
      amount=random.randint(1,10)
    )
    for i in range(10)
  ]
