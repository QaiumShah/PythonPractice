## Function Decorator ##

## Defining a function to decorate
## number represents the order of execution of the code

def decoration_func(func):   #3  #declaring function with function as parameter
    def wrapper(name):      #4 #declaring function with parameter
        return ("Hello there " + func(name) + "!")  #5 #8 #retuning string with function having 'name' parameter
    return wrapper  #returning 'wrapper' function

@decoration_func    #2  #adding Function decorator
def get_msg(name):    #6      #declaring a 'get_msg' function with parameter 'name'
    return name.upper()  #7 #returning 'name' in uppercase letter

## print(get_msg("john")) returns only 'JOHN' as it only calls 'get_msg' if @decorator_func is not used
print(get_msg("john")) #1

##output: Hello there JOHN! #9


## Class Decorator ##

##Decorator use-case for contructor overloading
#Built-in decorator to define class methods
#declaring a class with object
class ABC(object):
    def __init__(self, a_init): #initialising instance variable foo with a_init parameter as its value
        self.foo = a_init
    
    @classmethod    # adding class method

    #cls is class reference as a first argument
    def initWithString(cls, s_str): #declaring initWithString function for any numbers in string
        return cls(int(s_str))  #returning the class instance after converting the string to integer

ABC_obj = ABC.initWithString('34')  #declaring an object to class ABC using the initWithString constructor 

print(ABC_obj.foo)  #printing the value of instance variable 'foo' of class ABC to check if classmethod is working