'''
Example 1  # 10
Example 2  # 45






# Example 1
            # Program
def get_input_from_user():
    return input("response here -> ")

print("question 1")
name_result = get_input_from_user()

print("question 2")
name_result = get_input_from_user()

print("question 3")
name_result = get_input_from_user()

print("summary")




            # Global frame
function object:
get_input_from_user  # AA goes to the first def in my program (((def get_input_from_user():)))


name_result = some_name




            # Function frame    # Is totally separate from the global frame
return input from user  # Returns to (name_result, then to food_result,  then to food_result) in global frame = which ends the function




# Example 2  ** Program
def func_0(start_num):
    start_num += 1
    return func_1(start_num)

def func_1(start_num):
    start_num += 1
    return start_num

start_num = 1
print(f"start_num\t-> {start_num}")  # start_num       -> 1
finish_num = func_0(start_num)
print(f"calc'd_num\t-> {finish_num}")  # calc'd_num      -> 3
print(f"start_num\t-> {start_num}")  # start_num       -> 1


# Example 2 Global frame
function objects:
func_0
func_1

int objects
start_num -> 1   # from line 47


# Example 2 func_0 frame
start_num -> 1   # from line 47

'''


# # Example 3a  ** Program  converted to a list
# def func_0(other_num):
#     other_num[0] += 1
#     return func_1(other_num)

# def func_1(another_num):
#     another_num[0] += 1
#     return another_num

# start_num = [1]
# print(f"start_num\t-> {start_num}")  # start_num       -> [1]
# finish_num = func_0(start_num)
# print(f"calc'd_num\t-> {finish_num}")  # calc'd_num      -> [3]
# print(f"start_num\t-> {start_num}")  # start_num       -> [3]
# print(finish_num == start_num)  # True


# # Example 3b  ** Program  converted to a list
# def func_0(other_num):
#     other_num[0] += 1
#     return func_1(other_num)

# def func_1(another_num):
#     another_num[0] += 1
#     return another_num

# start_num = [1]
# print(f"start_num\t-> {start_num}")  # start_num       -> [1]
# finish_num = func_0(start_num.copy())
# print(f"calc'd_num\t-> {finish_num}")  # calc'd_num      -> [3]
# print(f"start_num\t-> {start_num}")  # start_num       -> [1]
# print(finish_num == start_num)  # False


# Example 3c  ** Program  converted to a list
def func_0(other_num):
    other_num[0] += 1
    return func_1(other_num)

def func_1(another_num):
    another_num[0] += 1
    return another_num

start_num = [1]
print(f"start_num\t-> {start_num}")  # start_num       -> [1]
finish_num = func_0(start_num[:])
print(f"calc'd_num\t-> {finish_num}")  # calc'd_num      -> [3]
print(f"start_num\t-> {start_num}")  # start_num       -> [1]
print(finish_num == start_num)  # False


# Example 3 Global frame
# function objects:
# func_0
# func_1

# int objects
# start_num ->

# finish_num ->




# func_0 frame
# other_num









# def func_0(start_num):
#     start_num[0] += 1
#     return func_1(start_num)

# def func_1(start_num):
#     start_num[0] += 1
#     return start_num

# start_num = [1]
# print(f"start_num\t-> {start_num}")  # start_num       -> 1
# finish_num = func_0(start_num)
# print(f"calc'd_num\t-> {finish_num}")  # calc'd_num      -> 3
# print(f"start_num\t-> {start_num}")  # start_num       -> 1


# # Example 2 Global frame
# function objects:
# func_0
# func_1

# int objects
# start_num -> 1   # from line 79


# # Example 2 func_0 frame
# start_num -> 1   # from line 79
