class Product_quotation_class():
  def __init__(
      self,
      id_product_quotation=0,
      id_product=0,
      amount=0):
    self.id_product_quotation = id_product_quotation
    self.id_product = id_product
    self.amount = amount
    
  def __str__(self):
    return f"{self.id_product_quotation}) id_product: {self.id_product} x {self.amount}"