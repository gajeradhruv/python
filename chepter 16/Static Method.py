# class Person:
#     count_instance = 0  # Class variable

#     def __init__(self, first_name, last_name, age):
#         Person.count_instance += 1
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age

#     @staticmethod
#     def from_string(string):
#         first, last, age = string.split()
#         return Person(first, last, int(age))  # Create a new instance of Person

#     @staticmethod
#     def get_count_instance():
#         return f"You have created {Person.count_instance} instances of Person class"

#     def full_name(self):
#         return f"{self.first_name} {self.last_name}"

#     def is_above_18(self):
#         return self.age > 18


# # Creating instances
# p1 = Person("vivek", "gohel", 20)
# p2 = Person("dhruv", "gohel", 21)
# p3 = Person.from_string("vivek visawliya 20")

# # Output
# print(p3.full_name())  # Output: vivek visawliya
# print(Person.get_count_instance())  # Output: You have created 3 instances of Person class
