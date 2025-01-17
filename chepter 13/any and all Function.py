def my_sum(*args):
    if all([(type(args)== int or type(args)==float) for  arg in args]):
        total=0
        for num in args:
            total +=sum
        return total
    return "wrong ans"
print(my_sum(1,2,3,4,5,8.9))