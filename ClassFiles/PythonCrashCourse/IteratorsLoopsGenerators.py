from random import randint, choice
from string import ascii_lowercase
'''
lists  # 8
Dicts  # 110
Generate 100 random integers  # 135
# Using list comprehension to Generate 100 random integers between 1 and 100  # 145
'''
l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
my_dict = {'py': 'python', 'rb': 'ruby', 'js': 'javascript'}

# sum of all ints useing a for loop
# sum = 0
# for num in l:
#     sum = sum + num

# print(f"Sum using list: {sum}")  # Sum using list: 63



''' Using a range generator
>>> range(10)
range(0, 10)
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> my_list =_
>>> my_list
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> type(my_list)
<class 'list'>
>>> type(range(10))
<class 'range'>
>>> 

'''
# for num in range(10):
#     print(num)  # 0
                # 1
                # 2
                # 3
                # 4
                # 5
                # 6
                # 7
                # 8
                # 9


# for num in range(10):
#     print("Hello")  # Hello
                    # Hello
                    # Hello
                    # Hello
                    # Hello
                    # Hello
                    # Hello
                    # Hello
                    # Hello
                    # Hello

# for num in range(10):
#     print(l[num])  # 6
#                     # 8
#                     # 1
#                     # 4
#                     # 10
#                     # 7
#                     # 8
#                     # 9
#                     # 3
#                     # 2

# for num in range(5):
#     print(l[num])  # 6
#                     # 8
#                     # 1
#                     # 4
#                     # 10

# sum = 0
# for num in range(len(l)):
#     sum = sum + l[num]
# print(f"Sum using range generator: {sum}")  # Sum using range generator: 63



# run_times = int(input("How many times do you want to run? "))  # How many times do you want to run? 5
# for num in range (run_times):
#     print(f"Run: {num+1}")  # Run: 1  ## +1 is used so I don't have a run 0
#                             # Run: 2
#                             # Run: 3
#                             # Run: 4
#                             # Run: 5


'''
>>> list(range(0,10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(1,11))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> list(range(1,20,2))
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
>>> 
'''

# run_times = int(input("How many times do you want to run? "))  # How many times do you want to run? 5
# for num in range (run_times):
#     print(f"Run: {num+1}")  # 


# Dictionaries
# for item in my_dict:
#     print(item)  # py
                # rb
                # js
                
# print(my_dict.items())  # dict_items([('py', 'python'), ('rb', 'ruby'), ('js', 'javascript')])


# for item in my_dict.items():
#     print(item)  # ('py', 'python')
                # ('rb', 'ruby')
                # ('js', 'javascript')


# for key, value in my_dict.items():
#     print(f"key is {key}. value is {value}")  # key is py. value is python
                                            # key is rb. value is ruby
                                            # key is js. value is javascript
                                            




#  Generate 100 random integers between 1 and 100
# l1 = []
# for num in range(100):
#     l1.append(randint(1,100))
# print(l1)  # [52, 97, 55, 56, 35, 39, 96, 5, 18, 20, 2, 24, 91, 11, 87, 75, 35, 55, 14, 38, 66, 90, 55, 95, 31, 31, 37, 18, 89, 96, 48, 11, 60, 83, 89, 97, 76, 63, 53, 13, 7, 25, 56, 49, 34, 75, 83, 67, 45, 42, 96, 7, 11, 41, 56, 94, 97, 75, 19, 17, 88, 37, 14, 26, 34, 74, 2, 93, 96, 10, 23, 16, 78, 60, 31, 25, 81, 55, 53, 61, 75, 8, 85, 61, 44, 78, 17, 82, 43, 21, 78, 93, 58, 46, 10, 74, 74, 42, 100, 90]





# Using list comprehension to Generate 100 random integers between 1 and 100
# l1 = [randint(1,100) for num in range(100)]

# print(l1)  # [7, 60, 54, 96, 28, 83, 32, 55, 88, 20, 96, 25, 6, 1, 19, 53, 6, 51, 33, 2, 77, 10, 20, 10, 70, 100, 39, 57, 67, 99, 78, 83, 16, 93, 29, 90, 78, 98, 37, 65, 66, 22, 2, 22, 83, 60, 63, 74, 9, 7, 97, 5, 73, 98, 78, 31, 6, 61, 21, 29, 8, 17, 44, 8, 11, 67, 85, 91, 50, 32, 51, 19, 18, 85, 45, 2, 88, 60, 49, 25, 22, 85, 58, 91, 68, 83, 83, 28, 81, 69, 72, 79, 86, 93, 30, 46, 24, 16, 79, 7]




# l1 = [num for num in range(100)]

# print(l1)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]




# l1 = [num**2 for num in range(100)]

# print(l1)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900, 961, 1024, 1089, 1156, 1225, 1296, 1369, 1444, 1521, 1600, 1681, 1764, 1849, 1936, 2025, 2116, 2209, 2304, 2401, 2500, 2601, 2704, 2809, 2916, 3025, 3136, 3249, 3364, 3481, 3600, 3721, 3844, 3969, 4096, 4225, 4356, 4489, 4624, 4761, 4900, 5041, 5184, 5329, 5476, 5625, 5776, 5929, 6084, 6241, 6400, 6561, 6724, 6889, 7056, 7225, 7396, 7569, 7744, 7921, 8100, 8281, 8464, 8649, 8836, 9025, 9216, 9409, 9604, 9801]




l1 = [choice(ascii_lowercase) for num in range(100)]

print(l1)  # ['l', 'c', 'n', 'j', 't', 'f', 'j', 'p', 'y', 'c', 'w', 's', 'n', 'g', 'g', 'a', 'a', 'c', 'c', 'd', 'e', 'n', 'x', 'v', 'z', 'e', 'n', 'l', 'j', 'v', 'g', 's', 'y', 'r', 'r', 'h', 'h', 'e', 'k', 'n', 'w', 'n', 'y', 'a', 'd', 'l', 'y', 'l', 'q', 'q', 'x', 'p', 'c', 'q', 'm', 'f', 'a', 'k', 's', 's', 'l', 'h', 'b', 'z', 'b', 'h', 'u', 'u', 'w', 'c', 'k', 'i', 'i', 'o', 'c', 'c', 'o', 'c', 'g', 'f', 'p', 'a', 'q', 'h', 'j', 'w', 'r', 's', 'm', 'v', 'i', 'h', 'b', 'u', 'z', 'q', 'i', 'i', 'w', 'x']

TODO: 26