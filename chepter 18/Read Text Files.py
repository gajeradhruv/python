# read file
# open function file
# read method
# seek method
# tell method
# readline method
# readlines method
# close method

# f=open('file1.txt')
# print(f.read())
# print(f.read())
# f.close()

# file1 = open("file1.txt")
# print(file1.read())   # Read whole content
# file1.seek(0)         # Go back to the beginning
# print(file1.readline())  # Read first line
# file1.close()         # Close the file


########### with blocking #####

# with open('file1.txt') as f:
#     data=f.read() 
#     print(data)

# with open('file1.txt') as f:
#     f.write('hello')

# with open("Demo.txt",'w') as f:
#     data=f.read()
#     print(data) 
# Open the file in read mode
with open("Demo.txt", "w") as file:
    content = file.write()  
    print(content)         

   