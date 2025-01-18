# class Phone:
# # base class / parent class
#     def __init__(self, brand, model_name, price):
#         self.brand = brand
#         self.model_name = model_name
#         self._price = max(price,0)
#     def full_name(self):
#         return f"{self.brand} {self.model_name}"
#     def make_a_call(self, number):
#         return f"calling {number}...."
    
# class smartphone(Phone):#derived class/child class
#     def __init__(self, brand, model_name, price,ram,internal_memmory,real_camara):
#         # phone.__init__(self,brand,model_name,price)#uncommon way
#         super().__init__(brand,model_name,price)
#         self.ram=ram
#         self.internal_memmory=internal_memmory
#         self.real_camara=real_camara


# class smartphone2(Phone):#derived class/child class
#     def __init__(self, brand, model_name, price,ram,internal_memmory,real_camara):
#         # phone.__init__(self,brand,model_name,price)
#         super().__init__(brand,model_name,price)
#         self.ram=ram
#         self.internal_memmory=internal_memmory
#         self.real_camara=real_camara
        
        
    
# phone=Phone('nokia','1100',1000)
# smartphone=smartphone2('oneplus','5',30000,'6gb','64gb','20mp')
# print(phone.full_name())
    
###################################### MUltilavel inheritance######################################################################
# class Phone:
# # base class / parent class
#     def __init__(self, brand, model_name, price):
#         self.brand = brand
#         self.model_name = model_name
#         self._price = max(price,0)
#     def full_name(self):
#         return f"{self.brand} {self.model_name}"
#     def make_a_call(self, number):
#         return f"calling {number}...."
    
# class smartphone(Phone):#derived class/child class
#     def __init__(self, brand, model_name, price,ram,internal_memmory,real_camara):
#         # phone.__init__(self,brand,model_name,price)#uncommon way
#         super().__init__(brand,model_name,price)
#         self.ram=ram
#         self.internal_memmory=internal_memmory
#         self.real_camara=real_camara

# class FlagshipPhone(smartphone):
#     def __init__(self, brand, model_name, price,ram,internal_memmory,real_camara,front_camara):
#         super().__init__(brand,model_name,price,ram,internal_memmory,real_camara)
#         self.front_camara=front_camara
        
    
# phone=Phone('nokia','1100',1000)
# smartphone=smartphone('oneplus','5',30000,'6gb','64gb','20mp')
# oneplus=FlagshipPhone('oneplus','5',30000,'6gb','64gb','20mp','16mp')
# print(oneplus.full_name())


############################# Method Resolution Order (MRO) ###################################
# class Phone:
# # base class / parent class
#     def __init__(self, brand, model_name, price):
#         self.brand = brand
#         self.model_name = model_name
#         self._price = max(price,0)
#     def full_name(self):
#         return f"{self.brand} {self.model_name}"
#     def make_a_call(self, number):
#         return f"calling {number}...."
    
# class smartphone(Phone):#derived class/child class
#     def __init__(self, brand, model_name, price,ram,internal_memmory,real_camara):
#         # phone.__init__(self,brand,model_name,price)#uncommon way
#         super().__init__(brand,model_name,price)
#         self.ram=ram
#         self.internal_memmory=internal_memmory
#         self.real_camara=real_camara

# class FlagshipPhone(smartphone):
#     def __init__(self, brand, model_name, price,ram,internal_memmory,real_camara,front_camara):
#         super().__init__(brand,model_name,price,ram,internal_memmory,real_camara)
#         self.front_camara=front_camara
        
    
# phone=Phone('nokia','1100',1000)
# smartphone=smartphone('oneplus','5',30000,'6gb','64gb','20mp')
# oneplus=FlagshipPhone('oneplus','5',30000,'6gb','64gb','20mp','16mp')
# print(oneplus.full_name())
# print(help(FlagshipPhone))#Method Resolution Order (MRO)

############################# Method Overriding ########################################
# class Phone:
# # base class / parent class
#     def __init__(self, brand, model_name, price):
#         self.brand = brand
#         self.model_name = model_name
#         self._price = max(price,0)
#     def full_name(self):
#         return f"{self.brand} {self.model_name}"
#     def make_a_call(self, number):
#         return f"calling {number}...."
    
# class smartphone(Phone):#derived class/child class
#     def __init__(self, brand, model_name, price,ram,internal_memmory,real_camara):
#         # phone.__init__(self,brand,model_name,price)#uncommon way
#         super().__init__(brand,model_name,price)
#         self.ram=ram
#         self.internal_memmory=internal_memmory
#         self.real_camara=real_camara

#     def full_name(self):
#         return f"{self.brand} {self.model_name} and price is {self._price} and front camera is ={self.real_camara}"
    
    
# class FlagshipPhone(smartphone):
#     def __init__(self, brand, model_name, price,ram,internal_memmory,real_camara,front_camara):
#         super().__init__(brand,model_name,price,ram,internal_memmory,real_camara)
#         self.front_camara=front_camara
        
    
# phone=Phone('nokia','1100',1000)
# smartphone=smartphone('oneplus','5',30000,'6gb','64gb','20mp')
# oneplus=FlagshipPhone('oneplus','5',30000,'6gb','64gb','20mp','16mp')
# print(oneplus.full_name())



################################# isinstance() and issubclass() ########################################
# class Phone:
# # base class / parent class
#     def __init__(self, brand, model_name, price):
#         self.brand = brand
#         self.model_name = model_name
#         self._price = max(price,0)
#     def full_name(self):
#         return f"{self.brand} {self.model_name}"
#     def make_a_call(self, number):
#         return f"calling {number}...."
    
# class smartphone(Phone):#derived class/child class
#     def __init__(self, brand, model_name, price,ram,internal_memmory,real_camara):
#         # phone.__init__(self,brand,model_name,price)#uncommon way
#         super().__init__(brand,model_name,price)
#         self.ram=ram
#         self.internal_memmory=internal_memmory
#         self.real_camara=real_camara

#     def full_name(self):
#         return f"{self.brand} {self.model_name} and price is {self._price} and front camera is ={self.real_camara}"
    
    
# class FlagshipPhone(smartphone):
#     def __init__(self, brand, model_name, price,ram,internal_memmory,real_camara,front_camara):
#         super().__init__(brand,model_name,price,ram,internal_memmory,real_camara)
#         self.front_camara=front_camara
        
    
# phone=Phone('nokia','1100',1000)
# oneplus5=smartphone('oneplus','5',30000,'6gb','64gb','20mp')
# oneplus5t=FlagshipPhone('oneplus','5',30000,'6gb','64gb','20mp','16mp')
# # print(oneplus.full_name())
# # print(isinstance(oneplus5,smartphone))#True