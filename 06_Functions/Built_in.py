def chai_flavour(flavour="masala"):
    '''return thr flavour of the chai'''
    chai="ginger"
    return flavour``

print(chai_flavour.__doc__)
print(chai_flavour.__name__)

# help(len)

def generate_bill(chai=0,samosa=0):
    '''
    Docstring for generate_bill
    
    :param chai: number of chai cups
    :param samosa: number of samosa
    '''
    total=chai*10 + samosa*15
    return total,"thank you visit again"

print(generate_bill(10,5))