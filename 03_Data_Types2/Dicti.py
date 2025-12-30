chai_order=dict(type="Masala Chai", size="large",suger=2)
print(f"order: {chai_order}")
# order: {'type': 'Masala Chai', 'size': 'large', 'suger': 2}

recipe={}
recipe["base"]="black tea"
recipe["liquid"]="milk"

# print(f"recipe: {recipe['base']}")
# # recipe: black tea

# del recipe["liquid"]
# print(f"recipe after deleting liquid: {recipe}")
# recipe after deleting liquid: {'base': 'black tea'}

#print(f"is 'suger' in chai_order? {'suger' in chai_order} ")
# is 'suger' in chai_order? True 

# print(f"chai_order keys: {chai_order.keys()} ")
# # chai_order keys: dict_keys(['type', 'size', 'suger'])

# print(f"chai_order values: {chai_order.values()} ")
# # chai_order values: dict_values(['Masala Chai', 'large', 2])

# print(f"chai_order items: {chai_order.items()} ")
# # chai_order items: dict_items([('type', 'Masala Chai'), ('size', 'large'), ('suger', 2)])

last_item=chai_order.popitem()
print(f"Removed item: {last_item}")

extra_spices={"cardamon":"crushed","ginger":"fresh"}
chai_order.update(extra_spices)
print(f"Updated chai_order: {chai_order}")

chai_size= chai_order["size"]
print(f"Chai size: {chai_size}")
# Chai size: large

chai_note= chai_order.get("note")
print(f"Chai note: {chai_note}")    