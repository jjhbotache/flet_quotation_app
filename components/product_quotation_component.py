from flet import *
from data.products_provider import get_products
from classes.product_quotation_class import Product_quotation_class
from functions.string_functions import put_points
class Product_quotation_component(UserControl):
  # def __init__(self,id_product=None,amount=1):
  def __init__(self,id_pq=None,products=get_products(),product_quotation=None,on_delete_product_quotation=None,on_change=None):
    super().__init__()
    self.id_product_quotation =product_quotation.id_product if product_quotation != None else id_pq
    self.amount = product_quotation.amount if product_quotation != None else 1
    self.product_quotation = product_quotation
    self.products = products
    self.current_product = None
    self.amount_component_ref = Ref[TextField]()
    self.amount_total_ref = Ref[Text]()

    self.delete_product_quotation = on_delete_product_quotation
    self.on_change = on_change

    self.total = 0

    if self.id_product_quotation != None and id_pq == None:
      self.current_product = list(filter(lambda p: p.id_product == self.id_product_quotation,self.products))[0]

    # print([p.name for p in self.products],sep="\n")

  def product_changed(self,e):
    amount_field = self.amount_component_ref.current
    product = list(filter(lambda p: p.name == e.control.value,self.products))[0]
    self.current_product = list(filter(
      lambda p: p.name == e.control.value,
      self.products
    ))[0]
    amount_field.label = product.unit
    amount_field.update()
    self.pq_changed()

  def amount_changed(self,add_or_remove=0):
    amount_field = self.amount_component_ref.current
    # first if it's not a number, set the number before
    if add_or_remove == 0:
      try:
        self.amount = int(amount_field.value)
      except:
        amount_field.value = self.amount
        amount_field.update()
        return
    else:
      self.amount += add_or_remove
      amount_field.value = self.amount
    
    if self.amount < 0:
      self.amount = 1
      amount_field.value = self.amount  

    amount_field.update()
    self.pq_changed()

  def get_data(self):
    return Product_quotation_class(
      id_product=self.current_product.id_product if self.current_product != None else 0,
      amount=self.amount
    )

  def pq_changed(self):
    try:self.total = self.current_product.price * self.amount
    except: self.total = 0
    self.amount_total_ref.current.text = f"Total: {put_points(self.total)}"
    self.amount_total_ref.current.update()
    self.on_change(self.get_data())


  def build(self):
    return Column([
      ResponsiveRow(
                [
                  Dropdown(
                    hint_text= self.current_product.name if self.current_product != None else "Select a product",
                    options=[dropdown.Option(p.name) for p in self.products],
                    col=6,
                    on_change=self.product_changed,
                  ),
                  TextField(ref=self.amount_component_ref,col=3,keyboard_type=KeyboardType.NUMBER,value=self.amount,on_change=lambda e: self.amount_changed(),label=self.current_product.unit if self.current_product != None else "??"),
                  Column([
                    IconButton(on_click=lambda e: self.amount_changed(1),style=ButtonStyle(padding=padding.all(0)),icon_size=15,icon=icons.ADD),
                    IconButton(on_click=lambda e: self.amount_changed(-1),style=ButtonStyle(padding=padding.all(0)),icon_size=15,icon=icons.REMOVE)
                  ],col=2,spacing=0),
                  IconButton(icon=icons.DELETE,on_click=self.delete_product_quotation,col=1)
                ],
                spacing=0,vertical_alignment="center"
              ),
        Text(f"Total: 0",size=12, ref=self.amount_total_ref),

    ],
    expand=True,
    spacing=2
    )
          