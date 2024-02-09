from classes.quotation_class import Quotation_class
import random
def get_quotations():
    letters = ['A','B','C','D','E','F','G','H','I','J']
    prices = [1010, 2020, 3030, 4040, 5050, 6060, 7070, 8080, 9090, 10000]
    products_quotations_ids=[
        # quotations ids list between 1 and 3
        [1,3,None],
        [2,3,1],
        [1,2,3],
        [3,1,2],
        [2,3,1],
        [1,2,3],
        [3,1,2],
        [2,3,1],
        [1,2,3],
        [3,1,2]        
    ]
    return [
    Quotation_class(
        name=f'Quotation {letters[i]}',
        price=prices[i],
        quotation_id=i+1,
        products_quotations=products_quotations_ids[i]
    ) 
        for i in range(len(letters))
    ]