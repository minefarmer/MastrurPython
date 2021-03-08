'''     Sets are optimized for two things
1. Finding information in them.
2. Mathematical operations.
'''
# my_set = {1,6,2,'java','ruby',8,9,10,21,1000,'python'}
# print(my_set)  # Order changes with each rerun
            # {1, 2, 6, 'python', 8, 9, 10, 1000, 'ruby', 'java', 21}
            # $ /usr/bin/python3 /home/rich/Desktop/MatHub/MastrurPython/ClassFiles/PythonCrashCourse/Sets.py
            # {1, 2, 'python', 6, 8, 9, 'ruby', 10, 1000, 21, 'java'}
            # $ /usr/bin/python3 /home/rich/Desktop/MatHub/MastrurPython/ClassFiles/PythonCrashCourse/Sets.py
            # {1, 2, 'java', 6, 8, 9, 10, 'ruby', 1000, 'python', 21}
            # $ /usr/bin/python3 /home/rich/Desktop/MatHub/MastrurPython/ClassFiles/PythonCrashCourse/Sets.py
            # {1, 2, 6, 'ruby', 8, 9, 10, 1000, 'python', 'java', 21}
            # $ /usr/bin/python3 /home/rich/Desktop/MatHub/MastrurPython/ClassFiles/PythonCrashCourse/Sets.py
            # {1, 2, 6, 'java', 8, 9, 10, 1000, 'ruby', 21, 'python'}
            # $ /usr/bin/python3 /home/rich/Desktop/MatHub/MastrurPython/ClassFiles/PythonCrashCourse/Sets.py
            # {1, 2, 'ruby', 'java', 6, 8, 9, 10, 1000, 'python', 21}
            # $ /usr/bin/python3 /home/rich/Desktop/MatHub/MastrurPython/ClassFiles/PythonCrashCourse/Sets.py
            # {1, 2, 6, 8, 9, 10, 1000, 21, 'java', 'python', 'ruby'}
            
'''
No duplicates in a set.

'''
# my_list = [1,6,2,'java','ruby',8,9,10,21,1000,6,'python','java']
# print(my_list)  # [1, 6, 2, 'java', 'ruby', 8, 9, 10, 21, 1000, 6, 'python', 'java']

# # duplicates are eliminated.  # 6


# my_set = set(my_list)
# print(my_set)  # {1, 2, 'java', 6, 8, 9, 10, 1000, 'python', 21, 'ruby'}


# print('java' in my_set)  # True


# print(my_set.) # . shows a drop-down list
my_set = {1, 6, 2, 'java', 'ruby', 8, 9, 10, 21, 1000, 6, 'python', 'java'}
programming_set = {'java','ruby','javascript','python','c'}
print(my_set.intersection(programming_set))  # {'python', 'java', 'ruby'}
print(my_set.union(programming_set))  # {1, 2, 'python', 'java', 6, 8, 9, 10, 1000, 'javascript', 'c', 'ruby', 21}
print(my_set.difference(programming_set))  # {1, 2, 6, 8, 9, 10, 1000, 21}
print(programming_set.difference(my_set))  # {'javascript', 'c'}


for item in my_set:
    print(item)  # 1
                # 2
                # 6
                # 8
                # 9
                # 10
                # 1000
                # python
                # java
                # 21
                # ruby
