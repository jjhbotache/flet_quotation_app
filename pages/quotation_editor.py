from flet import *
from data.quotations_provider import get_quotations
from components.product_quotation_component import Product_quotation_component
from classes.product_quotation_class import Product_quotation_class
from data.products_provider import get_products
from functions.string_functions import put_points
from constants.style_cosntants import bottom_padding
import random,time

class   Quotation_editor(UserControl):
  def __init__(self,page,quotation_id=None):
    super().__init__()
    self.page = page
    self.quotation_id = quotation_id
    self.products_quotations = Ref[Column]()
    self.main_column_ref = Ref[Column]()

    self.products_quotations_components = []


    self.quotation_name = ""
    self.quotation_price = 0
    self.list_of_product_quotation_ids = set()
    self.products = get_products()

    
    print(self.quotation_id,f"quotation_id")
    print(self.quotation_id != None,f"quotation_id != None")
    if self.quotation_id != None:
      # bring the quotation 
      quotations = get_quotations()
      # get the quotation by id
      self.quotation = next((quotation for quotation in quotations if quotation.quotation_id == self.quotation_id),None)
      self.quotation_name = self.quotation.name
      self.quotation_price = self.quotation.price

      self.products_quotations_components = [
          Product_quotation_component(pq.id_product,pq.amount) for pq in self.quotation.products_quotations
      ]

  def add_product_quotation(self,e):
    product_quotations_column = self.products_quotations.current
    # create a new product quotation obj
    # add it to the list of product quotations
    # update the view


    product_quotations_column.controls.append(
      Product_quotation_component()
    )
    product_quotations_column.update()

  def save_quotation(self,e):

    if any([pq.id_product == None for pq in self.products_quotations.current.controls]):
      dialog = AlertDialog(
        title=Text("Ups..."),
        content=Text("You must select a product for each product quotation"),
      )
      self.page.dialog = dialog
      dialog.open = True
      self.page.update()
      return

    # if it's empty, redirect to the home
    if len(self.products_quotations.current.controls) == 0:
      self.page.go("/")
      return
    # get all the product_quotations from the column
    product_quotations = [product_quotation.get_data() for product_quotation in self.products_quotations.current.controls]	

    print(*[str(pq) for pq in product_quotations],sep="\n")
    # todo: save the quotation in excel

    # set the save_quotation to a loading comoonent
    self.main_column_ref.current.controls[-1] = ProgressRing()
    self.main_column_ref.current.update()

    # simulate a delay
    time.sleep(2)

    success = random.choice([True,False])
    if success: dialog = AlertDialog(title=Text("Success"),content=Text("The quotation was saved successfully"),on_dismiss=lambda e: self.page.go("/"))
    else: dialog = AlertDialog(title=Text("Ups..."),content=Text("There was an error saving the quotation"),)

    self.page.dialog = dialog
    dialog.open = True
    self.page.update()

    # set the save_quotation to a button again
    self.main_column_ref.current.controls[-1] = ElevatedButton("Save",on_click=self.save_quotation)
    self.main_column_ref.current.update()

  def build(self):


    return SafeArea(
      Container(
      Column(
        [
          TextField(value=self.quotation_name,hint_text="Quotation name"),
          Container(
          Column(
          controls=self.products_quotations_components,
          ref=self.products_quotations,
          scroll=ScrollMode.ALWAYS,
          height=self.page.height-280,
          width=float("inf"),
          horizontal_alignment="center",
          spacing=0
          ),
          bgcolor=colors.GREY_800,
          ),
          Text(f"Total: {put_points(self.quotation_price * 1000)}",size=20),
          IconButton(icon_color="black",bgcolor=colors.GREY_100,icon=icons.ADD,on_click=self.add_product_quotation),
          ElevatedButton("Save",on_click=self.save_quotation), 
        ],
        horizontal_alignment="center",
        height=50,
        width=float("inf"),
        ref=self.main_column_ref
      ),
      bgcolor=colors.GREY_900,
      height=self.page.height-bottom_padding,
      ),
    )
