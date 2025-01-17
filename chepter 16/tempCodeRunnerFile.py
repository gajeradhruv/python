class Phone:
   def _init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self._price = price
        self.complete_specification = f"{self.brand} {self.model_name} and price {self._price}"
  
def make_a_call(self, phone_number):
        print(f"calling {phone_number}...")
        
def full_name(self):
       return f"{self.brand} {self.model_name}"

Phone1=Phone('nokia', '1100', 1000)
print(Phone1.brand)
print(Phone1.model_name)
Phone1._price=500
print(Phone1._price)
print(Phone1.complete_specification)