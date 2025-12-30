from functools import wraps

def require_admin(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role!="admin":
            print("Access denied")
        else:
            return func(user_role)
    return wrapper
        
@require_admin
def acess_tea_inventory(role):
    print("Acess granted to tea inventory")
# "def acess_tea_inventory(role):=my_decorator(def acess_tea_inventory(role):)"

acess_tea_inventory("user")
acess_tea_inventory("admin")