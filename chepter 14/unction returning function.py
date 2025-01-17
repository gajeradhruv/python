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

# ###### Decorators Intro #######
# def decorator_function(any_function):
#     def wrapper_function():
#         print('this is awesome function')
#         any_function()
#     return wrapper_function
# ##this is awesome Function  
# def func1():
#     print('this is function 1')
# ## this is awesome Function ####

# def func2():
#     print('this is Function 2')    

# var= decorator_function(func1)
# var()



# ###### Decorators Intro part 2#######
# def decorator_function(any_function):
#     def wrapper_function(*args,**kwargs):
#         print('this is awesome function')
#         return any_function(*args,**kwargs)
#     return wrapper_function
# @decorator_function
# def func(a):
#     print(f'this is the sunction without argument {a}')
# func(5)

# @decorator_function
# def add(a,b):
#     return a+b
# print(add(2,3))



# ###### Decorators Intro Part 3 #######
# from functools import wraps
# def decorator_function(any_function):
#     @wraps(any_function)
#     def wrapper_function(*args,**kwargs):
#         print('this is awesome function')
#         return any_function(*args,**kwargs)
#     return wrapper_function
# @decorator_function
# def add(a,b):
#     return a+b
# print(add.__doc__)
# print(add.__name__)

 ##Exercise in Decorators Intro 1#######
# from functools import wraps
# import time
# def calculate_time(function):
#     @wraps(function)
#     def wrapper(*args,**kwargs):
#         print(f'Executing ....{function.__name__}')
#         t1=time.time()
#         returned_value=function(*args,**kwargs)
#         t2=time.time()
#         total_time=t2-t1
#         print(f'this function took {total_time} seconds')
#         return returned_value
#     return wrapper
# @calculate_time
# def square_finder(n):
#     return[i**2 for i in range(1,n+1)]
# square_finder(1000)

####Exercise in the practice ######
# from functools import wraps
# def only_int_allow(function):
#     @wraps(function)
#     def wrapper(*args,**kwargs):
#         data_types=[]
#         for arg in args:
#             data_types.append(type(arg)==int)
#         if all(data_types):
#             return function(*args,**kwargs)
#         else:
#               print("Invalid arguments")
#     return wrapper
# @only_int_allow
# def add_all(*args):
#     total = 0
#     for i in args:
#         total +=i
#     return total

# print(add_all(1,2,3,4,5,[1,2,3]))


###Decorators Intro in the argument in the python ####
from functools import wraps
def only_data_type_allow(data_type):
    def decorator(function):
        @wraps(function)
        def wrapper(*args,**kwargs):
            if all([type(arg) == data_type for arg in args]):
                return function(*args,**kwargs)
            print("Invalid the arguments")
        return wrapper
    return decorator

@only_data_type_allow(str)
def string_join(*args):
    string =''
    for i in args:
        string +=i
    return string
print(string_join('vivek','Savaliya','a',8))

