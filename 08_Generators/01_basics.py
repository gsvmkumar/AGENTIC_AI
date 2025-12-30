def serve_chai():
    yield "cup 1: masala chai"
    yield "cup 2: ginger chai"
    yield "cup 3: elachi chai"

stall=serve_chai()

# for cup in stall:
#     print(cup)


def get_chai_list():
    return ["cup 1","cup 3","cup 3"]

def get_chai_gen():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"

chai=get_chai_gen()
print(chai)
print(next(chai))
print(next(chai))
print(next(chai))
# print(next(chai))  # it gives errors