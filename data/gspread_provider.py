import gspread
import os
# ----------------------------------------------------------------------------------------------------------------
def delete_letters(cadena):
    return ''.join(filter(str.isdigit, cadena))

def get_next_id_from_sh(sh):
  values = sh.col_values(1)
  try: return int(values[-1]) + 1
  except: return 1
# ----------------------------------------------------------------------------------------------------------------

gc = gspread.service_account(filename=os.path.join(os.path.dirname(os.path.abspath(__file__)),"courtines-config.json"))

bk = gc.open("courtines_quotator_db")


# C
def create_product(name:str,unit:str,price:str):
  # global sh
  # get the first row to get the properties
  sh = bk.worksheet("product")
  data = {
    "id_product": get_next_id_from_sh(sh),
    "name": name,
    "unit": unit,
    "price": price
  }

  sh.append_row(
    [data["id_product"],data["name"],data["unit"],data["price"]]
  )
  print("product created!: ",data)
  return data["id_product"]

def create_a_product_quotation(id_product:int,amount:int):

  product_quotation_ws = bk.worksheet("product_quotation")
  id_product_quotation = get_next_id_from_sh(product_quotation_ws)
  product_quotation_ws.append_row([id_product_quotation,id_product, amount]) #don't change this order
  print("product quotation created!:",id_product_quotation)
  return id_product_quotation

def create_quotation(quotation_name:str,list_of_product_quotations_dicts:list[dict]):
  """
  the list of product_quotations_dicts is a list dicts:
  {
    "id_product_quotation":int,
    "id_product":str,
    "amount":int
  }
  """
  # [{'id_product_quotation': 0, 'id_product': 'N1', 'amount': 2}]


  # ask for the name of the quotation
  # then, meanwhile the user wants to add products quotations
   
  list_of_product_quotations_ids = []

  # create the quotation
  quotation_sh = bk.worksheet("quotation")
  id_quotation = get_next_id_from_sh(quotation_sh)
  quotation_sh.append_row([id_quotation,quotation_name])

  # create  the product_quotations
  for pq_dict in list_of_product_quotations_dicts:
    list_of_product_quotations_ids.append(
      create_a_product_quotation(pq_dict["id_product"],pq_dict["amount"])
    )

  # for each product_quotation, link the pq and the quotation by adding it to a quotation_product_quotation
  quotation_product_quotation_sh = bk.worksheet("quotation_product_quotation")
  for pq_id in list_of_product_quotations_ids:
    id_quotation_product_quotation = get_next_id_from_sh(quotation_product_quotation_sh)
    quotation_product_quotation_sh.append_row(
      [id_quotation_product_quotation,  id_quotation, pq_id]
      )
  
  print("quotation created!:",id_quotation)
  return id_quotation
  
# R
def get_quotations():
  # get the quotations
  quotations_ws = bk.worksheet("quotation")
  quotations = quotations_ws.get_all_records()
  print(f"bringed quotations({len(quotations)})")
  return quotations

def get_products():
  # get the products
  products_ws = bk.worksheet("product")
  products = products_ws.get_all_records()
  # add the id_product field
  print(f"bringed products({len(products)})",)
  return products

def get_product_quotations():
  # get the products
  product_quotations_ws = bk.worksheet("product_quotation")
  product_quotations = product_quotations_ws.get_all_records()
  print(f"bringed product_quotations({len(product_quotations)})")
  return product_quotations

def get_quotation_product_quotations():
  quotation_product_quotations_ws = bk.worksheet("quotation_product_quotation")
  quotation_product_quotations = quotation_product_quotations_ws.get_all_records()
  print(f"bringed quotation_product_quotations ({len(quotation_product_quotations)})")
  return quotation_product_quotations

# U
def update_product(id_p:int,data_dict,products=get_products()):
  """
  This function updates a product
  data_dict: dict {
    "name":str,
    "unit":str,
    "price":str
  }
  """
  # this requires:
  # the id of the product
  # the data dict

  # get all the products
  # products = get_products()
  # ask for the user to choose a product to update
  # print(*[f"{p['id_product']}) {p['name']}"
  #   for p in products
  # ],sep="\n")
  # product_id_chose = input("Enter the product id: ")
  product_id_chose = id_p

  choosen_product = next(filter(lambda p: p["id_product"]==int(product_id_chose),products),None)
  print("updating the product",choosen_product["name"])
  ws = bk.worksheet("product")
  # find the row
  ids = [int(_id) for _id in ws.col_values(1)[1:]]
  row_index_to_update = ids.index(product_id_chose) + 2
  # update the row
  ws.update(
    range_name= f"B{row_index_to_update}:D{row_index_to_update}",
    values=
    [
      [data_dict["name"],data_dict["unit"],data_dict["price"]]
    ]
  )
  print("updated product!:",choosen_product["name"])

# D
def delete_register_by_id(id_to_delete:int,sh_name:str):
  product_sh = bk.worksheet(sh_name)
  ids = list(map(lambda p_id: int(p_id),product_sh.col_values(1)[1:]))
  try:
    index_to_delete = ids.index(id_to_delete) + 2
    product_sh.delete_rows(index_to_delete)
    print(f"deleted {sh_name}!:",id_to_delete)
  except:
    print("The id does not exist")

def delete_product(id_product:int,product_quotations=get_product_quotations(),quotation_product_quotations = get_quotation_product_quotations()):
  delete_register_by_id(id_product,"product")
  # delete the product_quotations where the id_product is the same
  product_quotations_to_delete = list(filter(lambda pq: pq["id_product"]==id_product,product_quotations))
  for pq in product_quotations_to_delete: 
    delete_product_quotation(pq["id_product_quotation"],quotation_product_quotations=quotation_product_quotations)
  print("deleted product!:",id_product)

def delete_product_quotation(id_product_quotation:int,quotation_product_quotations=[]):
  delete_register_by_id(id_product_quotation,"product_quotation")
  quotations_to_delete = list(filter(lambda qpq: qpq["id_product_quotation"]==id_product_quotation , quotation_product_quotations))
  for q in quotations_to_delete:
    if len(quotation_product_quotations)==0: delete_quotation(q["id_quotation"])
    delete_register_by_id(q["id_quotation_product_quotation"],"quotation_product_quotation")
  print("deleted product_quotation!:",id_product_quotation)

def delete_quotation(id_quotation_to_del:int,quotation_product_quotations=get_quotation_product_quotations()):
  delete_register_by_id(id_quotation_to_del,"quotation")
  quotation_product_quotations_to_delete = list(filter(lambda qpq: qpq["id_quotation"]==id_quotation_to_del , quotation_product_quotations))
  for qpq in quotation_product_quotations_to_delete:
    delete_product_quotation(qpq["id_product_quotation"])
    delete_register_by_id(qpq["id_quotation_product_quotation"],"quotation_product_quotation")
  print("deleted quotation!:",id_quotation_to_del)


# testing -------------------------------------------

# create_product()
# create_a_product_quotation()
# create_quotation()
  
# get_quotations()
# get_products()
# get_product_quotations()
  
# update_product(
#   id_p=int(input("Enter the id of the product to update: ")),
#   data_dict={
#     "name":input("Enter the new name: "),
#     "unit":input("Enter the new unit: "),
#     "price":input("Enter the new price: ")
#   }
# )


# delete_quotation(
#   id_quotation_to_del=int(input("Enter the id of the quotation to delete: ")),
#   quotation_product_quotations=get_quotation_product_quotations()
#   )

# delete_product(
#   id_product=int(input("Enter the id of the product to delete: ")),
#   product_quotations=get_product_quotations(),
#   quotation_product_quotations=get_quotation_product_quotations()
# )

# delete_product_quotation(
#   id_product_quotation=int(input("Enter the id of the product quotation to delete: ")),
#   quotation_product_quotations=get_quotation_product_quotations()
# )





