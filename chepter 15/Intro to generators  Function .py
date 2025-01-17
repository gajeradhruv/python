# def nums(n):
#     for i in range(1,n+1):
#          yield(i)
# numbers=nums(10)

# for num in numbers:
#      print(num)
# for num in numbers:
#      print(num) 

def even_generator(n):
    for num in  range(1,n+1):
        if num % 2 == 0:
            yield(num)
print(even_generator)
square= (i**2 for i in range(1,11))
print(next(square))
print(next(square))
print(next(square))