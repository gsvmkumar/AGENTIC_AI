def chai_customer():
    print("welcome! what chai would you like? ")
    order=yield
    while True:
        print(f"preparing: {order}")
        order=yield

stall=chai_customer()
next(stall) #starting point of generator

stall.send("Masala Chai")
stall.send("Lemon Chai")