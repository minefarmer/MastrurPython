# truth_condition = True

# if truth_condition:
#     print("Truth")  # Truth



# choice = '1'

# if choice == '1':
#     print("You have chosen option 1")  # You have chosen option 1



# choice = '2'

# if choice == '1':
#     print("You have chosen option 1")
# else:
#     print("You have an invalid choice")  # You have an invalid choice



# choice = '2'

# if choice == '1':
#     print("You have chosen option 1")
# elif choice == '2':
#     print("You have chosen option 2")  # You have chosen option 2
# else:
#     print("You have an invalid choice")



'''
>>> True and True
True
>>> True and False
False
>>> False and False
False
>>> 
'''



# choice = '1'
# made_payment = False

# if choice == '1'and made_payment:
#     print("You have chosen option 1")
# elif choice == '2':
#     print("You have chosen option 2")
# else:
#    print("You have an invalid choice")  # You have an invalid choice



# made_payment = True
# a = 'Please pay monthly premium'
# b = 'Welcome to your homepage'

# if made_payment:
#     print(a)  # Please pay monthly premium
# else:
#     print(b)



# made_payment = True
# a = 'Please pay monthly premium'
# b = 'Welcome to your homepage'

# if not made_payment:
#     print(a)
# else:
#     print(b)  # Welcome to your homepage



# i = 20
# j = 10
# k = 30

# if i < j and i < k:
#     print("i is less than j and k")  # nothing printed



# i = 5
# j = 10
# k = 30

# if i < j and i < k:
#     print("i is less than j and k")  # i is less than j and k



# i = 10
# j = 10
# k = 10

# if i < j and i < k:
#     print("i is less than j and k")
# elif i == j and i == k:
#     print("i is equal to j and k")  # i is equal to j and k
# elif i == j or i == k:
#     print("i is equal to either j or k")
# else:
#     print("something else")



# i = 10
# j = 10
# k = 10

# if i < j and i < k:
#     print("i is less than j and k")
# elif i == j or i == k:
#     print("i is equal to either j or k")  # i is equal to either j or k
# elif i == j and i == k:
#     print("i is equal to j and k")
# else:
#     print("something else")



# Ternary operator
# course = 'python'
# a = 'enrolled in python course'
# b = 'enrolled in some other course'

# print(a) if course == 'python' else print(b)  # enrolled in python course


course = 'java'
a = 'enrolled in python course'
b = 'enrolled in some other course'

print(a) if course == 'python' else print(b)  # enrolled in some other course


made_payment = True
a = 'Please pay monthly premium'
b = 'Welcome to your homepage'

print(a) if not made_payment else print(b) # Welcome to your homepage