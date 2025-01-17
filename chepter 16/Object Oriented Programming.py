# # class person:
# #     def __init__(self,Fast_name,last_name,age):
# #         self.Fast_name=Fast_name
# #         self.last_name=last_name
# #         self.age=age
# # p1=person('vivek','s','21')
# # p2=person('dhruv','a','21')

# # print(p1.Fast_name)
# # print(p2.last_name)

#  ######Exercise 1 & 2 #########

# # class laptop:
# #     def __init__(self,brand,model_name,price):
# #         self.brand=brand
# #         self.name=model_name
# #         self.price=price
# #         self.laptop_name=brand+ ' '+model_name

# #     def apply_discount(self,num):
# #         off_price = (num/100)*self.price
# #         return self.price-off_price    
                    
# # laptop1=laptop('HP','ax114x',63000)
# # print(laptop1.apply_discount(10))


# #class method in the python 

# class person:
#     count_instance=0
#     def __init__(self,Fast_name,last_name,age):
#         person.count_instance +=1
#         self.Fast_name=Fast_name
#         self.last_name=last_name
#         self.age=age
#     @classmethod
#     def count_instance(cls):
#         first,last,age = string.split()
#         return  cls(first,last,age)  
#     @classmethod
#     def get_count_instance(cls):
#         return f"you have created {cls.count_instance} instances of {cls.__name__} class"
#     def fast_name(self):
#         return f"{self.Fast_name} {self.last_name}"
#     def is_above_18(self):
#         return self.age>18
    
# p1=person('vivek','gohel','20')
# p2=person('dhruv','gohel','21')
# p3=person.from_string('vivek','visawliya','20')
# print(p3.full_name())       