'''                 Numbers = Intergers, floats

>>> 5
5
>>> type(5)
<class 'int'>
>>> type(3.5)
<class 'float'>
>>> result = 4 + 4
>>> type(result)
<class 'int'>
>>> result
8
>>> result + 4
12
>>> result - 4
4
>>> 5 - 10
-5
>>> abs(-10)
10
>>> 10 * 5
50
>>> 
>>> result = 10/5
>>> type(result)
<class 'float'>
>>> result
2.0
>>> 10/3
3.3333333333333335
>>> 10//3
3
>>> 10 + 2.5
12.5
>>> 10 + 2.0
12.0
>>> 10 % 3
1
>>> 10 % 2
0
>>> 15 % 3
0
>>> 23 % 5
3
>>> 123445678 % 2
0
>>> 34667 % 2
1
>>> 5 ** 2
25
>>> 5 ** 3
125
>>> 10 ** 5
100000
>>> import math
>>> math.pow(10,5)
100000.0
>>> 
>>> math.log2(10000000)
23.253496664211536
>>> import random
>>> random.randint(0,1000)
113
>>> random.randint(0,1000)
484
>>> random.randint(0,1000)
219
>>> random.randint(0,1000)
550
>>> random.randint(0,1000)
357
>>> 



'''                 


                    # Type Casting
# num_1 = "10"
# num_2 = "20"
# result = num_1 + num_2
# print(result)  # 1020

# num_1 = 10
# num_2 = 20
# result = num_1 + num_2
# result = str(result)
# print(result)  # 30
# print(type(result))  # <class 'int'


# num_1 = float("mashrur")
# num_2 = 20
# result = num_1 + num_2
# result = str(result)
# print(type(result))  # Traceback (most recent call last):
#   File "/home/rich/Desktop/MineFarmer/PythonMastrur/ClassFiles/DevelopeEnvironmentSetup/PythonCrashCourse/MathTypeCastingInput.py", line 94, in <module>
#     num_1 = float("mashrur")
# ValueError: could not convert string to float: 'mashrur'



#                   input
# print("Welcome to the multiplication program")
# print("-"*30)
# num_1 = 10
# num_2 = 20
# result = num_1 * num_2
# print(result)  # Welcome to the multiplication program
                # ------------------------------
                # 200


# print("Welcome to the multiplication program")
# print("-"*30)
# num_1 = input("Enter a number to multiply-> ")
# num_2 = input("Enter a second number to multiply-> ")
# result = num_1 * num_2
# print(result) # Enter a number to multiply-> 10
# Enter a second number to multiply-> 20
                                    # Traceback (most recent call last):
                                    # File "/home/rich/Desktop/MineFarmer/PythonMastrur/ClassFiles/DevelopeEnvironmentSetup/PythonCrashCourse/MathTypeCastingInput.py", line 120, in <module>
                                    #     result = num_1 * num_2
                                    # TypeError: can't multiply sequence by non-int of type 'str'


print("Welcome to the multiplication program")
print("-"*30)
num_1 = int(input("Enter a number to multiply-> "))
num_2 = int(input("Enter a second number to multiply-> "))
result = num_1 * num_2
print(result)  # Welcome to the multiplication program
                # ------------------------------
                # Enter a number to multiply-> 10
                # Enter a second number to multiply-> 50
                # 500
