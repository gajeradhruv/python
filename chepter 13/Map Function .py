numbers=[ 1,2,3,4,5]

squres=list(map(lambda a:a*2,numbers))
print(squres)

squres_new=[i**2 for i in numbers]
print(squres_new)