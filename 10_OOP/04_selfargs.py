class chaiCup:
    size=150 #ml

    def describe(self):
        return f"A {self.size}ml chai cup"
    
cup=chaiCup()
print(cup.describe())
print(chaiCup.describe(cup))

cup2=chaiCup()
cup2.size=100
print(chaiCup.describe(cup2))