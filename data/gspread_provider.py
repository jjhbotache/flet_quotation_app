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
def create_product():
  # global sh
  # get the first row to get the properties
  sh = bk.worksheet("product")
  fields = sh.row_values(1)

  data = {}
  for i in range(len(fields)):
    field = fields[i]
    if "id" in field:
      data[field] = get_next_id_from_sh(sh)
      continue
    data[field] = input(f"Enter the {field}: ")

  sh.append_row([data[field] for field in fields])
  return data["id_product"]

def create_a_product_quotation():
  #  get the products
  products_ws = bk.worksheet("product")
  products = products_ws.get_all_records()
  # print(products)
  # ask for the user to choose a product
  print(*[ f"{p['id_product']} ) {p['name']}"  for p in products ], sep="\n")

  id_product = int(input("Enter the product id: "))
  amount = int(input("Enter the amount: "))

  product_quotation_ws = bk.worksheet("product_quotation")
  id_product_quotation = get_next_id_from_sh(product_quotation_ws)
  product_quotation_ws.append_row([id_product_quotation,id_product, amount]) #don't change this order
  return id_product_quotation

def create_quotation():
  # ask for the name of the quotation
  # then, meanwhile the user wants to add products quotations
   
  quotation_name = input("Enter the name of the quotation: ")
  product_quotations = []


  while input("Do you want to add another product? (y/n): ")=="y":
    product_quotations.append(create_a_product_quotation())

  # create the quotation
  quotation_sh = bk.worksheet("quotation")
  id_quotation = get_next_id_from_sh(quotation_sh)
  quotation_sh.append_row([id_quotation,quotation_name])

  # for each product_quotation, add it to a quotation_product_quotation
  quotation_product_quotation_sh = bk.worksheet("quotation_product_quotation")
  for product_quotation in product_quotations:
    id_quotation_product_quotation = get_next_id_from_sh(quotation_product_quotation_sh)
    quotation_product_quotation_sh.append_row([id_quotation_product_quotation,id_quotation, product_quotation])
  
  print("done!")
  
# R
def get_quotations():
  # get the quotations
  quotations_ws = bk.worksheet("quotation")
  quotations = quotations_ws.get_all_records()
  return quotations

def get_products():
  # get the products
  products_ws = bk.worksheet("product")
  products = products_ws.get_all_records()
  # add the id_product field
  return products

def get_product_quotations():
  # get the products
  product_quotations_ws = bk.worksheet("product_quotation")
  product_quotations = product_quotations_ws.get_all_records()
  return product_quotations

def get_quotation_product_quotations():
  quotation_product_quotations_ws = bk.worksheet("quotation_product_quotation")
  quotation_product_quotations = quotation_product_quotations_ws.get_all_records()
  return quotation_product_quotations
# U
def update_product():
  # this requires:
  # the id of the product
  # the data per field

  # get all the products
  products = get_products()
  # ask for the user to choose a product to update
  print(*[f"{p['id_product']}) {p['name']}"
    for p in products
  ],sep="\n")
  product_id_chose = input("Enter the product id: ")

  choosen_product = next(filter(lambda p: p["id_product"]==int(product_id_chose),products),None)
  print("updating the product",choosen_product["name"])
  # for each field, ask for the user to update it and if it is empty, keep the old value
  worksheet = bk.worksheet("product")
  fields = worksheet.row_values(1)
  data = {}
  for field in fields:
    data[field] = input(f"Enter the {field} ({choosen_product[field]}): ") or choosen_product[field]
  # update the product
  worksheet.update(f"{product_id_chose}:{product_id_chose}", [[data[field] for field in fields]])
  print("done!") 
  

# D
def delete_register_by_id(id_to_delete:int,sh_name:str):
  product_sh = bk.worksheet(sh_name)
  ids = list(map(lambda p_id: int(p_id),product_sh.col_values(1)[1:]))
  try:
    index_to_delete = ids.index(id_to_delete) + 2
    product_sh.delete_rows(index_to_delete)
    print("done!")  
  except:
    print("The id does not exist")

def delete_product(id_product:int,product_quotations=get_product_quotations(),quotation_product_quotations = get_quotation_product_quotations()):
  delete_register_by_id(id_product,"product")
  # delete the product_quotations where the id_product is the same
  product_quotations_to_delete = list(filter(lambda pq: pq["id_product"]==id_product,product_quotations))
  for pq in product_quotations_to_delete:
    delete_product_quotation(pq["id_product_quotation"],quotation_product_quotations)

def delete_product_quotation(id_product_quotation:int,quotation_product_quotations=[]):
  delete_register_by_id(id_product_quotation,"product_quotation")
  quotations_to_delete = list(filter(lambda qpq: qpq["id_product_quotation"]==id_product_quotation , quotation_product_quotations))
  for q in quotations_to_delete:
    delete_quotation(q["id_quotation"])
    delete_register_by_id(q["id_quotation_product_quotation"],"quotation_product_quotation")

def delete_quotation(id_quotation_to_del:int,quotation_product_quotations=[]):
  delete_register_by_id(id_quotation_to_del,"quotation")
  quotation_product_quotations_to_delete = list(filter(lambda qpq: qpq["id_quotation"]==id_quotation_to_del , quotation_product_quotations))
  for qpq in quotation_product_quotations_to_delete:
    delete_product_quotation(qpq["id_product_quotation"])
    delete_register_by_id(qpq["id_quotation_product_quotation"],"quotation_product_quotation")


# testing -------------------------------------------

# create_product()
# create_a_product_quotation()
create_quotation()
  
# get_quotations()
# get_products()
# get_product_quotations()
  
# update_product()
  
delete_quotation(
  id_quotation_to_del=int(input("Enter the id of the quotation to delete: ")),
  quotation_product_quotations=get_quotation_product_quotations()
  )




