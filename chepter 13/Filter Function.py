# filter Function
def is_enven(a):
    return a%2==0
number=[3,4,2,1,5,6,9,8,10]

evens=filter(lambda a:a%2==0,number)
new_evens=[i for i in number if i%2==0] 
print(list(evens))
print(new_evens)