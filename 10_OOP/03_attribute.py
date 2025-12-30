class Chai:
    temp="hot"
    strength="Strong"


cutting=Chai()
print(cutting.temp)

cutting.temp="mild"
cutting.cup="small"
print("After changing ",cutting.temp)
print("Cup size ",cutting.cup)
print("After changing; main class chai is: ",Chai.temp)

del cutting.temp
del cutting.cup
print(cutting.temp)
# print(cutting.cup) it return error since it is deleted
