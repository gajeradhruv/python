# for i in range(11):
#     print(f"hello world :{i}")
# total=0
# for i in range(1,11):
#     total +=i
#     print(total)

# n=int(input("Enter the number:-"))
# total=0
# for i in range(1,n+1):
#     total +=i
#     print(total)

# total=0
# num=input("enter the Name:-")
# for i in range(0,len(num)):
#       total +=int(num[i])
#       print(total)

# name=input("Enter the  Name:")
# temp=""
# for i in range(len(name)):
#     print(f"{name[i]}:{name.count(name[i])}")
#     temp +=name[i]

#break statment
 
# for i in range(1,11):
#     if i==5:
#         break
#     print(i)

##continue Function

# for i in range(1,11):
#     if i==5:
#         continue
#     print(i)

 ##Exercise 6 (Game in the Python )
 

# winning_number=43
# guess=1
# number=int(input("Guess a number a between 1 and 100"))
# game_over=False

# while not game_over:
#     if number == winning_number:
#         print(f"you win, and guessed this number in {guess} times")
#         game_over=True
#     else:
#         if number<winning_number:
#             print("too low")
#             # guess +=1
#             # number=int(input("Guess again:"))
#         else:
#             print(" too high")
#             # guess +=1
#             # number=int(input("Guess again:"))
#             guess +=1
#             number=int(input("Guess again:"))

num=input("Enter the number:")
total=0
for i in num:
    total+=int(i)
    print(total)