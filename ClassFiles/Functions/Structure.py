#                   Structure of Function
'''

Notes on functions

def name_of_func():
    code to perform function operations
    must be indented to be considered
    part of the function


1. May or may not include parameters

includes parameters:
def add_two_nums(num_1. num_2):
    print(num_1, + num_2)

does not include parameters:
def say_hello():
    print("Hello World!)


'''
def add_two_nums(num_1, num_2):
    return num_1 + num_2
#        >  
# return | value none:
def say_hello():
    print("Hello World!")



''' 2. Might have return value specified, otherwise
returns None by default

return integer value:
def add_two_nums(num_1, num_2):
    return num_1 + num_2
       ^  
return | value none:
'''
def say_hello():
    print("Hello World!")  # Python is going to return None = so print("Hello World!")
def add_two_nums(num_1, num_2):
    return num_1 + num_2

print(add_two_nums(5,6))  # 11
# or
result = add_two_nums(5,6) # 11
print(result)



def say_hello():
    print("Hello World!")
say_hello()  # Hello World!

print(say_hello())  # Hello World!
                    # None



'''  3. Good to include a docstring in the function to provide information about it. (Optional)

including docstring:
def say_hello():
    # This function prints Hello World
    print("Hello World!")

including docstring
def add_two_nums(num_1,num_2):
    # This function adds two numbers
    # Input: Two interger values to add
    # Output: The sum of the two input integers

'''


'''  4. Try to limit a function to perform only 1 defined function, for example: an add function should only perform addition, not addition and multiplication.  # This may not be possible in some situations. But is helpful for having nice clean code.
'''


''' 5. Functions can return multiple values (as tuples).

def ints_and_dict(some_parameters);
# This function performs some operation and returns the integer list and a dictionary as output of the operation.

some function code
return ints_list, custom_dict
'''
