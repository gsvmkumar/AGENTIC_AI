
b=input("Enter the status of machine: ").lower()
if b=="active":
    a=int(input("Enter the temperature: "))
    if a>35:
        print("High Temperature alert")
    else:
        print("Temperature is normal")
else:
    print("Device is Offline")
