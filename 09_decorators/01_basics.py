from functools import wraps as w
def my_decorator(func):
    @w(func)
    def wrapper():
        print("before function runs")
        func()
        print("after function runs")
    return wrapper
@my_decorator
def greet():
    print("Hello from decorators class from chaicode")
# above greet() means "greet=my_decorator(greet)"


greet()
print(greet.__name__)