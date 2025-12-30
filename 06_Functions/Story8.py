'''chai_type="plain"

def front_desk():
    def kitchen():
        global chai_type
        chai_type="Irani"
    kitchen()
    print(chai_type)

front_desk()'''

# chai="ginger"

# def prepare_chai(order):
#     print("preparing ",order)

# prepare_chai(chai)


chai=[1,2,3]
def edit_chai(cup):
    cup[1]=42
# print(chai)
edit_chai(chai)
print(chai)
def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

# make_chai("Darjeeling","yes","Low") #positional
# make_chai(tea="Green",milk="medium",sugar="no")

def special(*args, **kwargs):
    print("ingrediants: ",args)
    print("Extras: ",kwargs)

special("cineman","cardamon", sweetner="Honey",foam="Yes")

def chai_order(order=None):
    if order is None:
        order=[]
    else:
        print(order)


chai_order()
chai_order("manikumar")