class Student:

    # adding (courses=None) solved the problem of not having the fourth argument.
    def __init__(self, first, last, courses=None):
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
            # ! This is printed after line 97 is run.
            print(f"{self.first_name} is already enrolled in the {course} course")

    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
        else:
            print(f"{course} not found")

    # def __str__(self):
    #     return f"First name: {self.first_name}\nLast_name: {self.last_name}\nCourses: {self.courses}"


# courses_1 = ['python','rails','javascript']
# courses_2 = ['java','rails','c']
# rich = Student("rich","matson",courses_1)
# carl = Student("carl","matson",courses_2)
# print(rich)  # First name: rich
#             # Last_name: matson
#             # Courses: ['python', 'rails', 'javascript']
# print(carl)  # First name: carl
#             # Last_name: matson
#             # Courses: ['java', 'rails', 'c']


#     def __str__(self):
#         return f"First name: {self.first_name.capitalize()}\nLast_name: {self.last_name.capitalize()}\nCourses: {self.courses}"


# courses_1 = ['python','rails','javascript']
# courses_2 = ['java','rails','c']
# rich = Student("rich","matson",courses_1)
# carl = Student("carl","matson",courses_2)
# print(rich)  # First name: Rich
#             # Last_name: Matson
#             # Courses: ['python', 'rails', 'javascript']
# print(carl)  # First name: Carl
#             # Last_name: Matson
#             # Courses: ['java', 'rails', 'c']


#     def __str__(self):
#         return f"First name: {self.first_name.capitalize()}\nLast_name: {self.last_name.capitalize()}\nCourses: {', '.join(self.courses)}"


# courses_1 = ['python','rails','javascript']
# courses_2 = ['java','rails','c']
# rich = Student("rich","matson",courses_1)
# carl = Student("carl","matson",courses_2)
# print(rich)  # First name: Rich
#             # Last_name: Matson
#             # Courses: ['python', 'rails', 'javascript']
# print(carl)  # First name: Carl
#             # Last_name: Matson
#             # Courses: java, rails, c


#     def __str__(self):
#         return f"First name: {self.first_name.capitalize()}\nLast_name: {self.last_name.capitalize()}\nCourses: {', '.join(map(str.capitalize, self.courses))}"


# courses_1 = ['python','rails','javascript']
# courses_2 = ['java','rails','c']
# rich = Student("rich","matson",courses_1)
# carl = Student("carl","matson",courses_2)
# print(rich) # First name: Rich
#             # Last_name: Matson
#             # Courses: Python, Rails, Javascript
# print(carl) # First name: Carl
#             # Last_name: Matson
#             # Courses: Java, Rails, C
# print(dir(rich))  # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'add_course', 'courses', 'first_name', 'last_name', 'remove_course']


#     def __len__(self):
#         return len(self.courses)

#     def __str__(self):
#         return f"First name: {self.first_name.capitalize()}\nLast_name: {self.last_name.capitalize()}\nCourses: {', '.join(map(str.capitalize, self.courses))}"


# courses_1 = ['python','rails','javascript']
# courses_2 = ['java','rails','c']
# rich = Student("rich","matson",courses_1)
# carl = Student("carl","matson",courses_2)
# print(rich) # First name: Rich
#             # Last_name: Matson
#             # Courses: Python, Rails, Javascript
# print(len(rich))  # 3
# print(carl) # First name: Carl
#             # Last_name: Matson
#             # Courses: Java, Rails, C


#     def __len__(self):
#         return len(self.courses)

#     def __str__(self):
#         return f"First name: {self.first_name.capitalize()}\nLast_name: {self.last_name.capitalize()}\nCourses: {', '.join(map(str.capitalize, self.courses))}"


# courses_1 = ['python','rails','javascript']
# courses_2 = ['java','rails','c']
# rich = Student("rich","matson",courses_1)
# carl = Student("carl","matson",courses_2)
# print(rich) # First name: Rich
#             # Last_name: Matson
#             # Courses: Python, Rails, Javascript
# print(len(rich))  # 3
# print(carl) # First name: Carl
#             # Last_name: Matson
#             # Courses: Java, Rails, C





#     def __len__(self):
#         return len(self.courses)

#     def __repr__(self):
#         return f"Student('{self.first_name}','{self.last_name},{self.courses})"

#     def __str__(self):
#         return f"First name: {self.first_name.capitalize()}\nLast_name: {self.last_name.capitalize()}\nCourses: {', '.join(map(str.capitalize, self.courses))}"


# courses_1 = ['python', 'rails', 'javascript']
# courses_2 = ['java', 'rails', 'c']
# rich = Student("rich", "matson", courses_1)
# carl = Student("carl", "matson", courses_2)
# print(rich)  # First name: Rich
# # Last_name: Matson
# # Courses: Python, Rails, Javascript
# print(repr(rich))  # Student('rich','matson,['python', 'rails', 'javascript'])
# print(carl)  # First name: Carl
# # Last_name: Matson
# # Courses: Java, Rails, C
# print(repr(carl))  # Student('carl','matson,['java', 'rails', 'c'])





    def __len__(self):
        return len(self.courses)

    def __repr__(self):
        return f"Student('{self.first_name}','{self.last_name},{self.courses})"

    # def __str__(self):
    #     return f"First name: {self.first_name.capitalize()}\nLast_name: {self.last_name.capitalize()}\nCourses: {', '.join(map(str.capitalize, self.courses))}"


courses_1 = ['python', 'rails', 'javascript']
courses_2 = ['java', 'rails', 'c']
rich = Student("rich", "matson", courses_1)
carl = Student("carl", "matson", courses_2)
print(rich)  # Student('rich','matson,['python', 'rails', 'javascript'])
print(carl)  # Student('carl','matson,['java', 'rails', 'c'])

