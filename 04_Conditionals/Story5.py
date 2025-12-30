Order_amount=int(input("ENte the oder amount: "))
print(f"Order amount: {Order_amount}")
Delivery= 0 if Order_amount>300 else 30
#value_if_true if condition else value_if_false
print(f"Delivery Fee is {Delivery}")
'''
if Order_amount>300:
    Delivery=0
else
    Delivery=30
    '''