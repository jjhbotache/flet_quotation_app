from classes.product_class import Product
import random
def get_products():
    
    return [
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