class person:
    def __init__(self,Fast_name,last_name,age):
        self.Fast_name=Fast_name
        self.last_name=last_name
        self.age=age
    
    def full_name(self):
        return f"{self.Fast_name} {self.last_name}"
    
p1=person('vivek','gohel','20')
print(p1.full_name())
# person.full_name(p1)