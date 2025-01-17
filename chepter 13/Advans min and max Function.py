# name=['vivek','Mohit','ab','z']
# print(min(name,key=lambda item:len(item)))

student={'vivek': {'socore':'80','age':'24'},
         'vivek1': {'socore':'80','age':'24'}
         }
        


student2= [
         {'name':'vivek','socore':'80','age':'24'},
         {'name':'dhruv','socore':'70','age':'25'},
         {'name':'Mohit','socore':'80','age':'26'},
         {'name':'priyank','socore':'60','age':'30'}
]
print(max(student2,key = lambda item:item.get('age'))['name'])