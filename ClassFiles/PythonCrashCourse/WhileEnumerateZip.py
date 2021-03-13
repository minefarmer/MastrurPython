from random import randint

''' While loops
Break (and pass) keyword
Generator - zip function

Enumerate  # 92
While loop  # 103
Generator called zip  # 130
'''
truth_condition = True

# while truth_condition:
#     print('Hello')  # Hello
#     break  # stops infinate loop

# i = 0
# while i < 10:
#     print(i)  # 0
#             # 1
#             # 2
#             # 3
#             # 4
#             # 5
#             # 6
#             # 7
#             # 8
#             # 9
#     i += 1



# l1 = [randint(1,100) for num in range(1000)]
# i = 0
# while i < 10:
#     print(i)  # 0
#             # 1
#             # 2
#             # 3
#             # 4
#             # 5
#             # 6
#             # 7
#             # 8
#             # 9
#     i += 1




# l1 = [randint(1,100) for num in range(1000)]
# i = 0
# num_to_search = 25
# while i < len(l1):
#     if l1[i] == num_to_search:
#         print(f"{num_to_search} found at index {i}")  # 25 found at index 2
#                                                     # 25 found at index 67
#                                                     # 25 found at index 342
#                                                     # 25 found at index 438
#                                                     # 25 found at index 871
#                                                     # 25 found at index 921
#                                                     # 25 found at index 998
#     i += 1




# l1 = [randint(1,100) for num in range(1000)]
# i = 0
# num_to_search = 25
# while i < len(l1):
#     if l1[i] == num_to_search:
#         print(f"{num_to_search} found at index {i}")  # 25 found at index 142
#         break
#     i += 1




# l1 = [randint(1,100) for num in range(1000)]
# i = 0
# num_to_search = 25
# for num in l1:
#     i += 1
#     if num == num_to_search:
#         print(f"{num_to_search} found at index {i}")  # 25 found at index 167
#         break




# l1 = [randint(1,100) for num in range(1000)]

# num_to_search = 25
# for index, num in enumerate(l1):
#     if num == num_to_search:
#         print(f"{num_to_search} found at index {index}")  # 25 found at index 178
#         break




# While loop
# while True:
#     print("Please chose an option from the list below:")
#     print("Press 1 for selection 1")
#     print("Press 2 for selection 2")
#     print("Press 3 to quit")
#     selection = input("Enter your choice-> ")  # Please chose an option from the list below:
#                                     # Press 1 for selection 1
#                                     # Press 2 for selection 2
#                                     # Press 3 to quit
#                                     # Enter your choice-> 1
#                                     # Please chose an option from the list below:
#                                     # Press 1 for selection 1
#                                     # Press 2 for selection 2
#                                     # Press 3 to quit
#                                     # Enter your choice-> 5
#                                     # Please chose an option from the list below:
#                                     # Press 1 for selection 1
#                                     # Press 2 for selection 2
#                                     # Press 3 to quit
#                                     # Enter your choice-> 3
    #  if int(selection) == 3:
#         break




# Generator called zip
# l1 = ['.py','.js','.rb','.java','c']
# l2 = ['python','javascript','ruby','java','c']
# tupled_list = zip(l2,l1)
# print(tupled_list)  # <zip object at 0x00000241E569E700>


l1 = ['.py','.js','.rb','.java','c']
l2 = ['python','javascript','ruby','java','c']
tupled_list = list(zip(l2,l1))  # [('python', '.py'), ('javascript', '.js'), ('ruby', '.rb'), ('java', '.java'), ('c', 'c')]
print(tupled_list)
