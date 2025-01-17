#loop in the Python

# i=1
# while i<=10:
#     print("hello")
#     i=i+1

#sum of two number

# total=0
# i=1
# while i<=10:
#     total +=i #total=total+1
#     i+=1
#     print(total)

# n=input("Enter the number :-")
# n=int(n)
# total=0
# i=1
# while i <= n:
#     total += i
#     i+=1
#     print(total)

# ##Exercise 4
# number=input("Enter the number:-")
# total=0
# i=1
# while i<len(number):
#     total += int(number[i])
#     i += 1
#     print(total)

 ##Exercise 3

# n=input("Enter the  number:-")
# n=int(n)
# total=0
# i=1
# while i<=n:
#     total +=i
#     i+=1
#     print(total)
 
######### Exercise 5 ########
name="harsh patelh"
# print(text.count(text))
temp_var=""
i=0
while i<len(name):
    if name[i] not in temp_var:
        temp_var +=name[i]
        print(f"{name[i]} : {name.count(name[i])}")
        i+=1