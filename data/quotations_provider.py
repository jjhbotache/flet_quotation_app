from classes.quotation_class import Quotation_class
from data.gspread_provider import get_quotations as get_quotations_gspread
from data.products_provider import get_products
from data.products_quotations_provider import get_products_quotations
from data.gspread_provider import get_quotation_product_quotations
import random
def get_quotations():
    # letters = ['A','B','C','D','E','F','G','H','I','J']
    # test_data = [
    # Quotation_class(
    #     name=f'Quotation {letters[i]}',
    #     quotation_id=i+1,
    # ) 
    #     for i in range(len(letters))
    # ]

    products_quotations = get_products_quotations()
    quotation_product_quotations = get_quotation_product_quotations()
    print("products_quotations",[pq.__dict__ for pq in products_quotations])

    real_data = get_quotations_gspread()
    real_data  = [
        Quotation_class(
            name=q["name"],
            quotation_id=q["id_quotation"],
            product_quotations_objs=products_quotations,
            quotation_product_quotations_objs=quotation_product_quotations
        )
        for q in real_data
    ]
    data_to_return = real_data

    return data_to_return