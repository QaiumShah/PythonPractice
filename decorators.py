## Defining a function to decorate##
## number represents the order of execution of the code

def f():
def decoration_func(func):   #3  #declaring function with function as parameter
    def wrapper(name):      #4 #declaring function with parameter
        return ("Hello there " + func(name) + "!")  #5 #8 #retuning string with function having 'name' parameter
    return wrapper  #returning 'wrapper' function

@decoration_func    #2
def get_msg(name):    #6      #declaring a 'get_msg' function with parameter 'name'
    return name.upper()  #7 #returning 'name' in uppercase letter

## print(get_msg("john")) returns only 'JOHN' as it only calls 'get_msg' if @decorator_func is not used
print(get_msg("john")) #1

##output: Hello there JOHN! #9