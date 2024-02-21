from flet import *
from data.quotations_provider import get_quotations
from data.products_provider import get_products
from data.gspread_provider import delete_product_quotation,create_quotation,create_a_product_quotation

from components.product_quotation_component import Product_quotation_component
from classes.product_quotation_class import Product_quotation_class
from functions.string_functions import put_points
from constants.style_cosntants import bottom_padding
import random,time

class Quotation_editor(UserControl):
  def __init__(self,page,quotation_id=None,products=get_products(),quotations=get_quotations()):
    super().__init__()
    self.page = page
    self.quotation_id = quotation_id
    self.products_quotations = Ref[Column]()
    self.main_column_ref = Ref[Column]()
    self.totalRef = Ref[Text]()

    self.products_quotations_components = []


    self.quotation_name = ""
    self.quotation_price = 0
    self.list_of_product_quotation_ids = set()
    self.products = products
    
    if self.quotation_id != None:
      # bring the quotation 
      # get the quotation by id
      self.quotation = next(
        (quotation for quotation in quotations if quotation.quotation_id == self.quotation_id)
        ,None
      )
      print("quotation",self.quotation.__dict__)
      self.quotation_name = self.quotation.name
      self.quotation_price = self.quotation.price

      def delete_pq(id_product_quotation):
        delete_product_quotation(id_product_quotation)
        self.products_quotations.current.controls = [pq for pq in self.products_quotations.current.controls if pq.id_product_quotation != id_product_quotation]
        self.products_quotations.current.update()

      self.products_quotations_components = [
          Product_quotation_component(
            id_pq=pq.id_product_quotation,
            product_quotation=pq,
            on_delete_product_quotation=lambda _: delete_pq(pq.id_product_quotation),
            products=self.products,
          )
          for pq in self.quotation.products_quotations
      ]
      print("p quotations ==============================",self.quotation.products_quotations)
      

  def add_product_quotation(self,e):
    product_quotations_column = self.products_quotations.current
    # create a new product quotation obj
    # add it to the list of product quotations
    # update the view

    no_id_quotations = [
      pq.id_product_quotation for pq in product_quotations_column.controls if isinstance(pq.id_product_quotation,str)
    ]

    new_pq_ids = [int(str_id[1:]) for str_id in no_id_quotations]
    last_id = max(new_pq_ids) if len(new_pq_ids) > 0 else 0

    new_component_id = f"N{last_id + 1}"
    print("new_component_id",new_component_id)
    component = Product_quotation_component(
      products=self.products,
      on_delete_product_quotation=lambda _:self.delete_product_quotation(new_component_id),
      id_pq=str(new_component_id),
      on_change=lambda _:self.update_total()
    )
    product_quotations_column.controls.append(component)
    self.update()
    self.update_total()

  def delete_product_quotation(self,id_pq):
    print("delete_product_quotation id:",id_pq)
    print("from pq:",[pq.id_product_quotation for pq in self.products_quotations.current.controls])
    pqcontrols = self.products_quotations.current.controls
    new_controls = list(filter(
      lambda pq: str(pq.id_product_quotation) != str(id_pq)
      ,pqcontrols
    ))

    self.products_quotations.current.controls = new_controls  
    self.update()
    self.update_total()

  def save_quotation(self,e):
    print("saving quotation")
    
    pq_components = self.products_quotations.current.controls
    if any([pq.current_product == None  for pq in pq_components]):
      dialog = AlertDialog(
        title=Text("Ups..."),
        content=Text("You must select a product for each product quotation"),
      )
      self.page.dialog = dialog
      dialog.open = True
      self.page.update()
      return
    if self.quotation_name == "":
      dialog = AlertDialog(
        title=Text("Ups..."),
        content=Text("You must enter a name for the quotation"),
      )
      self.page.dialog = dialog
      dialog.open = True
      self.page.update()
      return
    # get all the product_quotations from the column
    product_quotations = [product_quotation.get_data() for product_quotation in self.products_quotations.current.controls]	

    print("product_quotations","="*20)
    print([pq.__dict__ for pq in product_quotations]) #list of product_quotations classes
    # todo: save the quotation in excel

    # set the save_quotation to a loading comoonent
    self.main_column_ref.current.controls[-1] = ProgressRing()
    self.main_column_ref.current.update()

    # simulate a delay
    # time.sleep(2)
    if self.quotation_id != None:
      # update the quotation
      print("updating")
      # for each product_quotation, check if it is a new one or an old one
      return
    else:
      # add a new quotation
      print("creating new quotation")
      create_quotation(
        quotation_name=self.quotation_name,
        list_of_product_quotations_dicts=[pq.__dict__ for pq in product_quotations]
      )

    # return
    success = True
    if success: dialog = AlertDialog(title=Text("Success"),content=Text("The quotation was saved successfully"),on_dismiss=lambda e: self.page.go("/"))
    else: dialog = AlertDialog(title=Text("Ups..."),content=Text("There was an error saving the quotation"),)

    self.page.dialog = dialog
    dialog.open = True
    self.page.update()

    # set the save_quotation to a button again
    self.main_column_ref.current.controls[-1] = ElevatedButton("Save",on_click=self.save_quotation)
    self.main_column_ref.current.update()

  def update_total(self):
    prices = []
    for pq in [pq for pq in self.products_quotations.current.controls if pq.current_product != None]:
      prices.append(pq.amount * pq.current_product.price)
    total = sum(prices)

    self.totalRef.current.value = f"Total: {put_points(total)}"
    self.update()

  def build(self):
    return SafeArea(
      Container(
      Column(
        [
          TextField(
            value=self.quotation_name,
            on_change=lambda e: setattr(self,"quotation_name",e.control.value),
            hint_text="Quotation name",
            ),
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
          Text(f"Total: {put_points(self.quotation_price * 1000)}",size=20,ref=self.totalRef),
          IconButton(icon_color="black",bgcolor=colors.GREY_100,icon=icons.ADD,on_click=self.add_product_quotation),
          ElevatedButton("Save",on_click=self.save_quotation), 
          ElevatedButton("cancel",on_click= lambda e: self.page.go("/")), 

        ],
        horizontal_alignment="center",
        height=50,
        width=float("inf"),
        spacing=2
        ,ref=self.main_column_ref
      ),
      bgcolor=colors.GREY_900,
      height=self.page.height-bottom_padding,
      ),
    )
