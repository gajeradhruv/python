class phone:
    def __init__(self, brand, model_name, price):
        self.brand=brand
        self.model_name=model_name
        self._price=max(price,0)
    def full_name(self):
        return f"{self.brand} {self.model_name}"
    def make_a_call(self, number):
        return f"calling {number}..."
    
class smartphone(phone):
    def __init__(self, brand, model_name, price,ram,internal_memmory,real_camara):
        phone.__init__(self,brand,model_name,price)
        self.ram=ram
        self.internal_memmory=internal_memmory
        self.real_camara=real_camara
    #
    
    
    
phone=phone('nokia','1100',1000)
smartphone=smartphone('oneplus','5',30000,'6GB','64GB','20MP')
print(phone.full_name())
print(smartphone.full_name())