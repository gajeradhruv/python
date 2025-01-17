# number=[1,2,3,4,5,]
# print(number)

# Name=[1,"krishna",2,3,4]
# print(Name)

##### append Method in the python ####
# fruits=[]
# fruits.append("mango")
# fruits.append("apple")
# fruits.append("bnana")
# print(fruits)

#insert method

# fruits1=['mango','apple']
# fruits.insert(1,"banana")
# print(fruits)

###concatenate ###
# fruits2=['banana','grapes']
# fruits=fruits1+fruits2
# print(fruits)

######extend method######
# fruits1.extend(fruits2)
######append method ######
# fruits1.append(fruits2)
# print(fruits1)

##### pop method #####
# fruits=['apple','banana','kiwi',]
# fruits.pop(1)
##delet method
# del fruits[1]

####remove######
# fruits.remove('banana')

# print(fruits)

###in keyword in the list in the pyhon

# fruits=['orange','apple','pear','banana','kiwi']
# if 'mango' in fruits:
#  print("mango is the present")
# else:
#  print("mango is the not present")

##### List Compare lists #####
#==,is
# fruits1=['orange','apple','pear','banana','kiwi']
# fruits3=['orange','apple','pear','banana','kiwi']
# fruits2=['orange','banana','kiwi']
# print(fruits1==fruits3)
# print(fruits1 is fruits3)

##split Method
# user_info='krishna 21'.split()
# print(user_info)

##join method
# user_info=['krishna','21']
# print(','.join(user_info))

####List vs String
# s= "string"
# t=s.title()
# print(t)

#List

# I=['word1','word2','word3','word4']
# I.append("word5")
# print(I)

# fruits1=['orange','apple','pear','banana','kiwi']

# for fruits in fruits1:
#     print(fruits)

#use in the while loop using

# i=0
# while i<len(fruits1):
#     print(fruits1[i])
#     i+=1

##Negative List in the print ####

# numbers=[1,2,3,4,5,6,7,8,9,10]
# def negative_list(l):
#     negative=[]
#     for i in l:
#         negative.append(-i)
#     return negative
# print(negative_list(numbers))

####min and max Function  #####
# numbers=[6,60,2]

# def greateat_diff(l):
#     return max(l)-min(l)
# print(greateat_diff(numbers))

######Exercise 1 #####
# def squre_list(l):
#     sequre=[]
#     for i in l:
#         sequre.append(i**2)
#     return sequre
# number=list(range(1,11))
# print(squre_list(number))


######Exercise 2 #####
# def reverse_list(l):
#     return l[::-1]
#     # l.reverse()
#     # return l
# number=[1,2,3,4,5,6]
# print(reverse_list(number))

       
######Exercise 3 #####
# def reverse_elements(l):
#     elements=[]
#     for i in l:
#       elements.append(i[::-1])
#     return elements
    
# words=['abc','tuv','xyz']
# print(reverse_elements(words))

######Exercise 4 #####
# def filter_odd_even(l):
#     odd_nums=[]
#     even_nums=[]
#     for i in l:
#         if i%2 ==0:
#        even_nums.append(i)
#         else:
#    odd_nums.append(i)
#     output=[odd_nums,even_nums]
#     return output
# nums=[1,2,3,4,5,6,7]

# print(filter_odd_even(nums))

######Exercise 5 #####

# def common_finder(l1,l2):
#     output=[]
#     for i in l1:
#      if  i in l2:
#         output.append(i)
#     return output
# print(common_finder([1,2,5,8],[1,2,7,6]))

######Exercise 6 #####

# def sublist_counter(l):
#     count=0
#     for i in l:
#         if type(i)==list:
#             count+=1
#         return count
# mixed=[1,2,3,[3,4]]
# print(sublist_counter(mixed))






