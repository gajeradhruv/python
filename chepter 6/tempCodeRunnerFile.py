#dictionaries in the simple program

# user={'name':'krishna','age':'24'}
# print(user)
# print(type(user))

# for i,j in user_info.items():
#     print(f"key is {i} and value is {j}")

####Add two the data 
# user_info['fav_song']=['song1','song2']
# print(user_info)

# ##HOW two use in the pop method
# popped_item=user_info.pop('fav_tunes')
# print(f"popped items is {popped_item}")
# print(type(popped_item))
# print(user_info)

# ##popitem method
# popped_item=user_info.popitem()
# print(user_info)
# print(type(popped_item))

####dictionaries in the update method in the use
# user_info = {
# 'name':
# 'harshit',
# 'age' :
# 24,
# 'fav_movies': [
# 'coco', 'kimi no na wa'],'fav_tunes': ['awakening', 'fairy tale'],
# }
# more_info={'state':'haryana','hobies':['coding','reding','gujrat']}
# user_info.update(more_info)
# print(user_info)

#fromkeys in the python in method
# d=dict.fromkeys(('name','age','height'),'unknown')
# print(d)

# ###get Method (userfull)
d={'name': 'unknown','age':'unknown'}
print(d.get('name'))
#get method in the more items
user={'name':'Harshit','age':24}
print(user.get('ageS'))

######Exercise 1 #####
# def cube_finder(n):
#     cube={}
#     for i in range(1,n+1):
#        cube[i]=i**3
#     return cube
# print(cube_finder(10))

# ###word counter in the python 
# def word_counter(s):
#     count={}
#     for char in s:
#         count[char]=s.count(char)
#     return count
# print(word_counter('krishna'))

######Exercise 2 #####

# user={}
# Name=input('Enter the Name:-')
# age=input('Enter your Age:-')
# fav_movies=input('Enter the fav_movies seprated by:,').split(',')
# fav_song=input('Enter the fav_song seprated by:,').split(',')

# user['name']=Name
# user['age']=age
# user['fav_movies']=fav_movies
# user['fav_song']=fav_song
# print(user)

