from classes.quotation_class import Quotation_class
from data.gspread_provider import get_quotations as get_quotations_gspread
from data.products_provider import get_products
from data.products_quotations_provider import get_products_quotations
import random
def get_quotations():
    letters = ['A','B','C','D','E','F','G','H','I','J']
    # test_data = [
    # Quotation_class(
    #     name=f'Quotation {letters[i]}',
    #     quotation_id=i+1,
    # ) 
    #     for i in range(len(letters))
    # ]

    products = get_products()
    products_quotations = get_products_quotations()

    try:
        real_data = get_quotations_gspread()
        real_data  = [
            Quotation_class(
                name=real_data[0]["name"],
                quotation_id=real_data[0]["id_quotation"],
                products_objs=products,
                product_quotations_objs=products_quotations
            )
        ]
        data_to_return = real_data
    except Exception as e:
        print("Error in get_quotations")
        print(e)
        # data_to_return = test_data
        data_to_return = []

    return data_to_return