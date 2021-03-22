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










file_name = "data.txt"
rich = Student("carl","matson",['python', 'rails', 'javascript'])
print(carl.find_in_file(file_name))
print(carl.add_to_file(file_name))
rich = Student("carl","matson",['python', 'rails', 'javascript'])
print(rich.find_in_file(file_name))
print(rich.add_to_file(file_name))
