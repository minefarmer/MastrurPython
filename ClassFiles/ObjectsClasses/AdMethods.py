'''
.add_course("java)  # 13
.add_course("rails") again  # 14
preventing = .add_course("rails")  # 72
removing already in rolled courses  # 102
streamlined  # 143





'''
# class Student:
    
#     def __init__(self, first, last, courses=None):  # adding (courses=None) solved the problem of not having the fourth argument.
#         self.first_name = first
#         self.last_name = last
#         if courses == None:
#             self.courses = []
#         else:
#             self.courses = courses

#     def add_course(self, course):
#         self.courses = courses

# courses_1 = ['python','rails','javascript']
# courses_2 = ['java','rails','c']
# rich = Student("rich","matson",courses_1)
# carl = Student("carl","matson",courses_2)

# print(rich.first_name, rich.last_name, rich.courses)  # rich matson []
# print(carl.first_name, carl.last_name, carl.courses)  # carl matson ['java', 'rails', 'c']
# # .add_course("java")








# # .add_course("rails")
# class Student:
    
#     def __init__(self, first, last, courses=None):  # adding (courses=None) solved the problem of not having the fourth argument.
#         self.first_name = first
#         self.last_name = last
#         if courses == None:
#             self.courses = []
#         else:
#             self.courses = courses

#     def add_course(self, course):
#         self.courses.append(course)

# courses_1 = ['python','rails','javascript']
# courses_2 = ['java','rails','c']
# rich = Student("rich","matson",courses_1)
# carl = Student("carl","matson",courses_2)

# print(rich.first_name, rich.last_name, rich.courses)  # rich matson ['python', 'rails', 'javascript']
# print(carl.first_name, carl.last_name, carl.courses)  # carl matson ['java', 'rails', 'c']
# # .add_course("java")
# rich.add_course("rails")
# print(rich.first_name, rich.last_name, rich.courses)  # rich matson ['python', 'rails', 'javascript', 'rails']






# preventing = .add_course("rails")
# class Student:
    
#     def __init__(self, first, last, courses=None):  # adding (courses=None) solved the problem of not having the fourth argument.
#         self.first_name = first
#         self.last_name = last
#         if courses == None:
#             self.courses = []
#         else:
#             self.courses = courses

#     def add_course(self, course):
#         if course not in self.courses:  # This is the code  **************
#             self.courses.append(course)
#         else:
#             print(f"{self.first_name} is already enrolled in the {course} course")  #! This is printed after line 97 is run.

# courses_1 = ['python','rails','javascript']
# courses_2 = ['java','rails','c']
# rich = Student("rich","matson",courses_1)
# carl = Student("carl","matson",courses_2)

# print(rich.first_name, rich.last_name, rich.courses)  # rich matson ['python', 'rails', 'javascript']
# print(carl.first_name, carl.last_name, carl.courses)  # carl matson ['java', 'rails', 'c']
# # .add_course("java")
# rich.add_course("rails")  # rich is already enrolled in the rails course  #! This is printed after line 97 is run.
# print(rich.first_name, rich.last_name, rich.courses)  # rich matson ['python', 'rails', 'javascript', 'rails']



# # removing already in rolled courses  #! starts line 120
# class Student:
    
#     def __init__(self, first, last, courses=None):  # adding (courses=None) solved the problem of not having the fourth argument.
#         self.first_name = first
#         self.last_name = last
#         if courses == None:
#             self.courses = []
#         else:
#             self.courses = courses

#     def add_course(self, course):
#         if course not in self.courses:  # This is the code  **************
#             self.courses.append(course)
#         else:
#             print(f"{self.first_name} is already enrolled in the {course} course")  #! This is printed after line 97 is run.


#     def remove_course(self, course):
#         if course in self.courses:
#             self.courses.remove(course)
#         else:
#             print(f"{course} not found")

# courses_1 = ['python','rails','javascript']
# courses_2 = ['java','rails','c']
# rich = Student("rich","matson",courses_1)
# carl = Student("carl","matson",courses_2)

# print(rich.first_name, rich.last_name, rich.courses)  # rich matson ['python', 'rails', 'javascript']
# print(carl.first_name, carl.last_name, carl.courses)  # carl matson ['java', 'rails', 'c']
# # .add_course("java")
# rich.add_course("rails")  # rich is already enrolled in the rails course  #! This is printed after line 97 is run.
# print(rich.first_name, rich.last_name, rich.courses)  # rich matson ['python', 'rails', 'javascript', 'rails']
# carl.remove_course("c")
# carl.remove_course("c")  # c not found
# carl.remove_course("python")  # python
# print(carl.first_name, carl.last_name, carl.courses)  # carl matson ['java', 'rails']



# removing already in rolled courses
class Student:
    
    def __init__(self, first, last, courses=None):  # adding (courses=None) solved the problem of not having the fourth argument.
        self.first_name = first
        self.last_name = last
        if courses == None:
            self.courses = []
        else:
            self.courses = courses

    def add_course(self, course):
        if course not in self.courses:  # This is the code  **************
            self.courses.append(course)
        else:
            print(f"{self.first_name} is already enrolled in the {course} course")  #! This is printed after line 97 is run.


    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
        else:
            print(f"{course} not found")

courses_1 = ['python','rails','javascript']
courses_2 = ['java','rails','c']
rich = Student("rich","matson",courses_1)
carl = Student("carl","matson",courses_2)




# print(rich)  # <__main__.Student object at 0x7f508b348370>
# print(carl)  # <__main__.Student object at 0x7f508b348310>

# print(rich.first_name, rich.last_name, rich.courses)  # rich matson ['python', 'rails', 'javascript']
# print(carl.first_name, carl.last_name, carl.courses)  # carl matson ['java', 'rails', 'c']
# # .add_course("java")
# rich.add_course("rails")  # rich is already enrolled in the rails course  #! This is printed after line 97 is run.
# print(rich.first_name, rich.last_name, rich.courses)  # rich matson ['python', 'rails', 'javascript', 'rails']
# carl.remove_course("c")
# carl.remove_course("c")  # c not found
# carl.remove_course("python")  # python
# print(carl.first_name, carl.last_name, carl.courses)  # carl matson ['java', 'rails']
