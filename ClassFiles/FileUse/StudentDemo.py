class Student:
    
    def __init__(self, first, last, courses=None):  # adding (courses=None) solved the problem of not having the fourth argument.
        self.first_name = first
        self.last_name = last
        if courses == None:
            self.courses = []
        else:
            self.courses = courses

    def add_course(self, course):
        self.courses = courses


courses_1 = ['python', 'rails', 'javascript']
courses_2 = ['java', 'rails', 'c']
rich = Student("rich","matson",courses_1)
carl = Student("carl","matson",courses_2)

