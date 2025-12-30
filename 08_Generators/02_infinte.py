def infinite_chai():
    c=1
    while True:
        yield f"Refill #{c}"
        c+=1

refill = infinite_chai()
user2 = infinite_chai()
print(next(refill))
print("######")


for _ in range(5):
    print(next(refill))

for _ in range(6):
    print(next(user2))

