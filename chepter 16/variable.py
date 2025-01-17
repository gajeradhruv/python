# class laptop:
#     discount_percent=10 
#     def __init__(self,brand,model_name,price):
#         self.brand=brand
#         self.name=model_name
#         self.price=price
#         self.laptop_name=brand+ ' '+model_name

#     def apply_discount(self):
#         off_price = (laptop.discount_percent/100)*self.price
#         return self.price-off_price    

# laptop.discount_percent=100
# laptop1=laptop('HP','ax114x',63000)
# laptop1=laptop('Apple mac','a495x',100000)
# print(laptop1.apply_discount())

 ######Exercise 3 #########

# class person:
#     count_instance=0
#     def __init__(self,Fast_name,last_name,age):
#         self.Fast_name=Fast_name
#         self.last_name=last_name
#         self.age=age

# p1=person('vivek','gohel','21')
# print(person.count_instance)