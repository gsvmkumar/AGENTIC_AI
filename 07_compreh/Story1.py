#List comprehension
# [expression for item in iterable]

'''menu=["masala chai", "Ice lemon Chai","Green chai","Ginger chai"]

iced_chai = [tea for tea in menu]
print (iced_chai)'''


# [expression for item in iterable if condition]
menu=["masala chai", "Iced lemon Chai","Iced Green chai","Ginger chai"]

iced_chai = [tea for tea in menu if "Iced" in tea]
print (iced_chai)