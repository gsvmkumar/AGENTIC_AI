#Set comprehensions

# {expression for item in iterable if condition}

fav_chai=[
    "Masala chai","Green tea","Masala chai",
    "Lemon Tea","Green tea","Elachi Chai"
]
unique_chai = {chai for chai in fav_chai if len(chai)<12}

# print(unique_chai)

recipes={
    "Masala Chai": ["ginger", "cardamom","clove"],
    "Elachi Chai": ["cardamom","milk"],
    "spicy chai" : ["ginger","black pepper","clove"]
}

unique_spice={ spice for ingr in recipes.values() for spice in ingr}

print(unique_spice)

