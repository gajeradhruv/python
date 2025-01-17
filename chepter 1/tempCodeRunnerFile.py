# #string methods part one

# name="HaRsHit"

# #len()function
# lenth=len(name)
# print(lenth)

# #lower Method
# print(name.lower())

# #upper() method
# print(name.upper())

# #title() method
# print(name.title())

# #count() Method 
# print(name.count("H"))

# #exercise:-
# name,char = input("Enter the Name and Caracter:").split(",")
# print(f"length of your name is {len(name)}")
# print(f"character count :{name.count(char)}")

# #Center Method 
# name=input("Entetr the Name:-")
# print(name.center(len(name)+4,"*"))

##String Inmutable 
# string="string"
# new_string=string.replace('t','T')
# print(new_string)

# #Assignment Operation the add in the articales in the string
# Name="harsh"
# Name +="it"
# print(Name)

# #exercise in the oll chapter 2:-
#string
name="harsh"
#string Indexing
print(name[1])
#string slicing
print(name[1::3])
#take User input
# name=input("Enter the name:-")
#len() function
lenth=len(name)
print(lenth)

#upper method
print(name.upper())

#Title method
print(name.title())
 
#Replece method
string="the apple is the best fruit us full"
print(string.replace("the","this",1))

#Center Method
# name=input("Enter the Number:-")
print(name.center(len(name)+4,"*"))