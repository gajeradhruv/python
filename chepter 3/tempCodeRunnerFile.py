#Function in the python 
# def odd_even(num):
#     if num%2==0: 
#         return "Even"
#     else:
#         return "odd"
# print(odd_even(10))
####sort method:-
# def odd_even(num):
#     if num%2==0: 
#         return "Even"
#     return "odd"
# print(odd_even(9))

###very sort method function in the python 

# def odd_even(num): #<----(num):Parameter:----->
#     return num%2 ==0
# print(odd_even (21))#<----(21):Argument:----->

#function wthout  Parameter in the function in the python

# def song():
#     return "happy birthday song"
# print(song())

#########Exercise 1 in the function in the python

# def greter(a,b):
#     if a > b:
#         return a
#     else:
#         return b
# num1=int(input("Enter the Fast number"))
# num2=int(input("Enter the Second number"))
# bigger=greter(num1,num2)
# print(f"{bigger}is greater")

# def greatest(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>a and b>c:
#         return b
#     else:
#         return c
    
# def new_greatest(a,b,c):
#     bigger=greatest(a,b)
#     return greatest(bigger,c)
# print(greatest(100,200,30))

### palindrom in the using the python 
# def is_palindrom(word):
#     reversed_word=word[::-1]
#     if word==reversed_word:
#         return True
#     else:
#         return False
# print(is_palindrom("naman"))
# print(is_palindrom("horse"))

# ####sort method:-
# def is_palindrom(word): 
#     if word==word[::-1]:
#         return True
#     return False
# print(is_palindrom("naman"))
# print(is_palindrom("horse"))

#### very sort in the function  
# def is_palindrom(word): 
#     return word==word[::-1]        
# print(is_palindrom("naman"))
# print(is_palindrom("horse"))

### fibonacci in the pyhton

# def fibonacci_seq(n):
#     a=0
#     b=1
#     if n==1:
#         print(a)
#     elif n==2:
#         print(a,b)
#     else:
#         print(a,b, end=" ")
#         for i in range(n-2):
#             c=a+b
#             a=b
#             b=c
#             print(b,end=" ")
# fibonacci_seq(20)
        
#scope function in the python 
# x=5 #gloal function

# def func():
#  x=7 #local function
#  return x
# print( x )
# print(func())
# print(x)

##default parameters

def user_info(first_name='unknown',last_name='unknown',age=None):
    print(f"your first name is {first_name}")
    print(f"your last Name is {last_name}")
    print(f"you age is {age}")

    user_info()