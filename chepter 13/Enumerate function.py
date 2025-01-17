
names=['abc','abcdef','vivek']

# for pos,name in enumerate (names):
#       print(f"{pos} ---> {name}")

#########Exercise 1########
def find_pos(l,target):
    for pos, name in enumerate(l):
        if name == target:
            return pos
        return -8
print(find_pos(names,'abcz'))