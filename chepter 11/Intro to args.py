#Make in the flexible in thy function
#operator
#args

# def total(a,b):
#     return a+b
# def all_total(*args):
#     total=0
#     for num in args:
#          total +=num
#     return total
# print(all_total(1,2,3,4))

# ###normal parameter with args#####
# def multiply_nums(num,*args):
#     multiply=1
#     print(args)
#     for i in  args:
#         multiply*=i
#         return multiply
# print(multiply_nums(2,4,5,3,4))

#######Args as argument ###########
# def multiply_nums(*args):
#     multiply=1
#     print(args)
#     for i in  args:
#         multiply*=i
#         return multiply
# nums=(2,3,4)
# print(multiply_nums(*nums))

############ Exercise 1###############

# def to_power(num,*args):
#     if args:
#         return[i**num for i in args]
#     else:
#         return"you didn'tpass any args"
# nums=[1,2,3]
# print(to_power(nums))


####### kwargs (keyword in the pyhon) #####

# def func(name,**kwargs):
#     for k,v in kwargs.items():
#         print(f"{k}:{v}")
# func('vivek',first_name='harshit',last_name='harshita')


############ Exercise 2############### (function in the string are a reverse in the caracter in the python)

def func(l,**kwargs):
    if kwargs.get('reverse_str')==True:
        return[name[::-1].title() for name in l]
    else:
        return [name.title() for name in l]
names=['harshit ','Mohit']
print(func(names,reverse_str=True))