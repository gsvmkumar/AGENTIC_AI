# val=18
# rem=val%5

# if rem:
#     print(f"not divisible")

#Walrus

# val=12

# if (rem:= val%5):
#     print("Not divisible")

# available=["small","medium","high"]

# if(req_size:= input("Enter the req size: ")) in available:
#     print(f"Serving {req_size} chai")
# else:
#     print("not aavilable")

flavors=["masala","ginger","lemon","mint"]

# print (" flavors are ",flavors)

while( flover:=input("Choose your flavor: ")) not in flavors:
    print(f"Sorry, {flover} is not available")
print(f"you choose {flover} chai")