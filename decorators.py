#Defining a function to decorate 
def decoration_func(func):  #declaring function with function as parameter
    def wrapper(name):      #declaring function with parameter
        return ("Hello there " + func(name) + "!")    #retuning string with function having 'name' parameter
    return wrapper  #returning 'wrapper' function

@decoration_func
def get_msg(name):  #declaring a 'get_msg' function with parameter 'name'
    return name.upper() #returning 'name' in uppercase letter

## print(get_msg("john")) returns only 'JOHN' as it only calls 'get_msg' if @decorator_func is not used
print(get_msg("john"))