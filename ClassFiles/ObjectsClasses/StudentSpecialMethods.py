'''             Build student class
Dunder methods  # 30
Add courses to student class  # 45






'''
# class Student:
#     pass

# rich = Student()
# rich.first_name = "rich"
# rich.last_name = "matson"

# carl = Student()
# carl.first_name = "carl"
# carl.last_name = "matson"

# print(rich)  # <__main__.Student object at 0x7f3df9257f70>
# print(rich.first_name, rich.last_name)  # rich matson
# print(carl)  # <__main__.Student object at 0x7f202b121ac0>
# print(carl.first_name, carl.last_name)  # carl matson




#  Dunder methods
# class Student:
    
#     def __init__(self, first, last):  # methods with two underscores on each side are (special methods) or (dunder methods)
#         self.first_name = first
#         self.last_name = last

# rich = Student("rich","matson")
# carl = Student("carl","matson")

# print(rich.first_name, rich.last_name)  # rich matson
# print(carl.first_name, carl.last_name)  # carl matson



# Add courses to student class
class Student:
    
    def __init__(self, first, last):  # methods with two underscores on each side are (special methods) or (dunder methods)
        self.first_name = first
        self.last_name = last


courses_1 = ['python', 'rails', 'javascript']
courses_2 = ['java','rails','c']
rich = Student("rich","matson",courses_1)

# print(rich.first_name, rich.last_name, rich.courses)  # rich matson
# print(carl.first_name, carl.last_name, carl.courses)  # carl matson
