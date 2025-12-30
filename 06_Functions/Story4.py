def calculate_bill(cups, price):
    return cups*price
bill = calculate_bill(3,15)
print(bill)

print("Order for table 2 is",calculate_bill(2,50))