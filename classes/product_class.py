class Product():
  def __init__(
      self,
      id_product:int,
      name:str,
      unit:str,
      price:float,
  ):
    self.id_product = id_product
    self.name = name
    self.unit = unit
    self.price = price

  def __str__(self):
    return f'{self.id_product}) Product({self.name},{self.unit},{self.price})'