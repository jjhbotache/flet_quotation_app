from classes.product_quotation_class import Product_quotation_class
from data.gspread_provider import get_product_quotations as get_products_quotations_gspread
import random

def get_products_quotations():
  test_data = [
    Product_quotation_class(
      id_product_quotation=i+1,
      id_product=i+1,
      amount=random.randint(1,10)
    )
    for i in range(10)
  ]

  try:
    real_data = get_products_quotations_gspread()
    real_data = [
      Product_quotation_class(
        id_product_quotation=p["id_product_quotation"],
        id_product=p["id_product"],
        amount=p["amount"]
      )
      for p in real_data
    ]
    data_to_return = real_data
  except Exception as e:
    print("Error in get_products_quotations")
    print(e)
    data_to_return = test_data



  return data_to_return
