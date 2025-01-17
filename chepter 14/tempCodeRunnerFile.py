######## unction returning function ##########




####### Pass function as argument Function ########

#####Function returning Function (closure) Practice in the Python 
# def to_power(x):
#     def calc_power(n):
#         return n**x
#     return calc_power
# cube = to_power(3)
# print(cube(2))

# square= to_power(2)
# print(square(4))

###### Decorators Intro #######
def decorator_function(any_function):
    def wrapper_function():
        print('this is awesome function')
        any_function()
        return wrapper_function
##this is awesome Function  
def func1():
    print('this is function 1')
## this is awesome Function ####

def func2():
    print('this is Function 2')    

var=decorator_function(func1)
var()