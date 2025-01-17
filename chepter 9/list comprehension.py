# # # square2=[i**2 for i in range(1,11)]
# # # print(square2)

# # new_nagative=[-i for i in range(1,11)]
# # print(new_nagative)


# ######Exercise 1 #####

# # def reverse_string(l):
# #     return[name[::-1] for name in l]
# # print(reverse_string(['abc','tuv','xyz']))

# ########odd and Even number #######
# # numbers=list(range(1,11))

# # even_number=[i for i in numbers if i%2 == 0]  
# # even_number=[i for i in numbers if i%2 != 0]

# # print(even_number)

# ######Exercise 2 #####

# # def num_to_string(l):
# #     return[str(i) for i in l if(type(i) == int or type(i)==float)]
# # print(num_to_string([True,False,[1,2,3],1,1.0,3]))

# #########list comprehension with if False ###########
# # nums=[1,2,3,4,5,6,7,8,9,10]
# # new_list2=[i*2 if (i%2==0)else -i for i in nums]
# # print(new_list2)

# #####list comprehension in nested Function ######

# example=[[1,2,3],[1,2,3],[1,2,3]]
# nested_comp=[[i for i in range(1,4)] for j in range(3)]
# print(nested_comp)