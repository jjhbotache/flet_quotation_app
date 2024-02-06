from classes.quotation_class import Quotation_class
import random
def get_quotations():
    letters = ['A','B','C','D','E','F','G','H','I','J']
    return [Quotation_class(name=f'Quotation {letters[i]}',price=1000*random.randint(1,10),quotation_id=i+1) for i in range(len(letters))]