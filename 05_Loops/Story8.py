'''flavours=["ginger","outofstock","lemon","Discontinued"]
for f in flavours:
    if f=="outofstock":
        continue
    elif f=="Discontinued":
        break
    print(f)

print("Order completed")'''

staff=[["Amith",15],["mani",9],["hsjh",11]]

for i,j in staff:
    if j>=18:
        print(i,j)
        break
else:
    print('no one is found to vote')
