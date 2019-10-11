def fabonacci(n):
    a,b= 0,1
    while a<n:
        print(a, end=" ")
        a,b = b, a+b
    print()

fabonacci(2000)

class Fruit:
    def __init__(self, name, color, flavor):
        self.name = name
        self.color = color
        self.flavor = flavor
    
    def description(self):
        print("I'm a %s %s and I taste %s." %(self.color, self.name, self.flavor))

lemon = Fruit("lemon", "yellow", "sour")
lemon.description() 
