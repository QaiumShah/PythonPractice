#function for fabonacci series desplay
def fabonacci(n):   #passing total number 'n' in the function. 
                    #This will be the highest number till the fabonacci series will be displayed
    a,b= 0,1   #declaring two variables a and b with values 0 and 1 respectively
    while a<n:      # using while loop to stop the loop till it reaches less then n starting from a
        print(a, end=" ")       # print a with space on the same line
        a,b = b, a+b            # a will become b and b will become a+b
    print()                     #print new line

fabonacci(2000)     #initialising the function with 2000 as its n parameter .

##output: 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 ##


#calling a class object
class Fruit:
    def __init__(self, name, color, flavor):        #defining a construct method with instance 'self' and 
                                                    #parameter of the class

        self.name = name               #instance variable name assigned to name parameter
        self.color = color             # instance variable color assigned to color parameter
        self.flavor = flavor           # instance variable flavor assigned to flavor parameter
    
    def description(self):          # defining a function description with instance self as parameter

        #method of displaying instance variables using %s ordered inside %(self.name, ...)
        print("I'm a %s %s and I taste %s." %(self.color, self.name, self.flavor))

lemon = Fruit("lemon", "yellow", "sour")    #declaring instance of class Fruit with values
lemon.description()         #calling the description method inside the class

##output: I'm a yellow lemon and I taste sour. ##

#calling function inside function
#number represents the order of execution of the code
def f():
    def g():            
        print("Hi, it's me 'g'.") #4
        print("Thanks for calling me.") #5
    
    print("This is funciton 'f'.")  #1
    print("I am calling 'g' now: ") #2
    g() #3

f() ## calling function f

# Functions as parameters
#number represents the order of execution of the code

def g():
    print("Hi, it's me 'g'")    #3

def f(func):    #declaring a function 'f' with function 'func' as parameter
    print("Hi, its me 'f'") #1
    func()  #2

f(g)    #calling function f with g function as parameter

