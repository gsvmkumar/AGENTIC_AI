order=input("Enter your order: ").lower()

print(f"Your order: {order}")
if order=="samosa" or order=="cookies":
    print("Order Successfull")
else:
    print("Order Unsuccessfull")