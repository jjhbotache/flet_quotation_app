from classes.product_class import Product
from data.gspread_provider import get_products as get_products_gspread
import random
def get_products():
    test_data = [
      Product(
        id_product=1,
        name="Sheer",
        unit="m2",
        price=random.randint(1000, 10000)
      ),
      Product(
        id_product=2,
        name="Blackout",
        unit="m2",
        price=random.randint(1000, 10000)
      ),
      Product(
        id_product=3,
        name="Americana",
        unit="m2",
        price=random.randint(1000, 10000)
      ),
    ]

    try:
      real_data = get_products_gspread()

      real_data = [
          Product(
              id_product=p["id_product"],
              name=p["name"],
              unit=p["unit"],
              price=p["price"]
          )
          for p in real_data
      ]
      return real_data
    except Exception as e:
      print("Error in get_products")
      print(e)
      return test_data
