"""
Lists ## 30
Using sorted  ## 50
Finding information about the list and working with it.  ## 100
Adding items to and removing items from a list.  ## 139





my_list = [4,6,7,8, 10, 12, 14, 15, 35]
my_list = ["comp sci", "physics", "elec engr", "philosophy"]

        Examples of things I could want to do with lists:
1. Sort the values in ascending order, descending order.
    Sort  -sort(), sorted()-nice prep for algorithms section.
2. Find values in the list or details about the list.
    Find -len(), min(), max(), in indexing, slicing count().
3. Find values in the list or details about the list.
4. Grab sub-lists from the list to work with.
5. Iterate through and perform functions/checks on each item.
6. Insert/remove - append(), insert(), extent(), remove(), pop().
7. Sub-lists - slicing, inplace, copying.
8. Iteration - for loops, while loops (covered in later video).




"""
# Lists

# my_list = [15, 6, 7, 8, 35, 12, 14, 4, 10]
# my_strings_list = ["comp sci", "physics", "elec engr", "philosophy"]
# print(f"Ints: {my_list}")  # Ints: [15, 6, 7, 8, 35, 12, 14, 4, 10]
# print(f"strings: {my_strings_list}")  # strings: ['comp sci', 'physics', 'elec engr', 'philosophy']
# # sorted(my_list)  ## This was not used **********************************
# print("Sorting...")  # Sorting...
# print(f"Sorted Ints: {my_list}")  # Sorted Ints: [15, 6, 7, 8, 35, 12, 14, 4, 10]


# Using sorted
# my_list = [15, 6, 7, 8, 35, 12, 14, 4, 10]
# my_strings_list = ["comp sci", "physics", "elec engr", "philosophy"]
# print(f"Ints: {my_list}")  # Ints: [15, 6, 7, 8, 35, 12, 14, 4, 10]
# print(f"strings: {my_strings_list}")  # strings: ['comp sci', 'physics', 'elec engr', 'philosophy']
# print("Sorting...")  # Sorting...
# print(sorted(my_list))  # [4, 6, 7, 8, 10, 12, 14, 15, 35]
# print(f"Sorted Ints: {my_list}")  # Sorted Ints: [15, 6, 7, 8, 35, 12, 14, 4, 10]

# my_list = [15, 6, 7, 8, 35, 12, 14, 4, 10]
# my_strings_list = ["comp sci", "physics", "elec engr", "philosophy"]
# print(f"Ints: {my_list}")  # Ints: [15, 6, 7, 8, 35, 12, 14, 4, 10]
# print(f"strings: {my_strings_list}")  # strings: ['comp sci', 'physics', 'elec engr', 'philosophy']
# print("Sorting...")  # Sorting...
# sorted_list = sorted(my_list)
# print(sorted(my_list))  # [4, 6, 7, 8, 10, 12, 14, 15, 35]
# print(f"Sorted Ints: {my_list}")  # Sorted Ints: [15, 6, 7, 8, 35, 12, 14, 4, 10]

# my_list = [15, 6, 7, 8, 35, 12, 14, 4, 10]
# my_strings_list = ["comp sci", "physics", "elec engr", "philosophy"]
# print(f"Ints: {my_list}")  # Ints: [15, 6, 7, 8, 35, 12, 14, 4, 10]
# print(f"strings: {my_strings_list}")  # strings: ['comp sci', 'physics', 'elec engr', 'philosophy']
# print("Sorting...")  # Sorting...
# my_list.sort()
# sorted_list = sorted(my_list)
# print(sorted_list)  # Sorted Ints: [4, 6, 7, 8, 10, 12, 14, 15, 35]
# print(id(sorted_list))  # 139924571559808
# print(f"Sorted Ints: {my_list}")  # Sorted Ints: [4, 6, 7, 8, 10, 12, 14, 15, 35]

# my_list = [15, 6, 7, 8, 35, 12, 14, 4, 10]
# my_strings_list = ["comp sci", "physics", "elec engr", "philosophy"]
# print(f"Ints: {my_list}")  # Ints: [15, 6, 7, 8, 35, 12, 14, 4, 10]
# print(f"strings: {my_strings_list}")  # strings: ['comp sci', 'physics', 'elec engr', 'philosophy']
# print(id(my_list))  # 139798987163136
# print("Sorting...")  # Sorting...
# my_list.sort()
# sorted_list = sorted(my_list)
# print(sorted_list)  # Sorted Ints: [4, 6, 7, 8, 10, 12, 14, 15, 35]
# print(id(sorted_list))  # 139798985787584
# print(id(my_list))  # 139798987163136
# print(f"Sorted Ints: {my_list}")  # Sorted Ints: [4, 6, 7, 8, 10, 12, 14, 15, 35]


# Finding information about the list and working with it.
# my_list = [15, 6, 7, 8, 35, 12, 14, 4, 10]
# my_strings_list = ["comp sci", "physics", "elec engr", "philosophy"]
# print(f"Ints: {my_list}")  # Ints: [15, 6, 7, 8, 35, 12, 14, 4, 10]
# print(f"strings: {my_strings_list}")  # strings: ['comp sci', 'physics', 'elec engr', 'philosophy']
# print("Finding info...")  #
# print("physics" in my_strings_list)  # True
# print(50 in my_list)  # False
# print(my_strings_list.index("physics"))  # 10
# print(len(my_list))  # 9
# print(len(my_strings_list))  # 4
# print(my_list[len(my_list)-1])  # 10
# print(my_list[-1])  # 10
# print(min(my_list))  # 4
# print(max(my_list))  # 35
# print(dir(my_list))  # ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']


# my_list = [15, 6, 7, 8, 35, 12, 14, 4, 10, 15]
# my_strings_list = ["comp sci", "physics", "elec engr", "philosophy"]
# print(f"Ints: {my_list}")  # Ints: [15, 6, 7, 8, 35, 12, 14, 4, 10]
# print(f"strings: {my_strings_list}")  # strings: ['comp sci', 'physics', 'elec engr', 'philosophy']
# print("Finding info...")  # Finding info...
# print(my_list.count(15))  # 2


# Adding items to and removing items from a list.
# append(). insert(), extend()
# my_list = [15, 6, 7, 8, 35, 12, 14, 4, 10, 15]
# my_strings_list = ["comp sci", "physics", "elec engr", "philosophy"]
# my_new_list = ["art", "econ"]
# print(f"Ints: {my_list}")  # Ints: [15, 6, 7, 8, 35, 12, 14, 4, 10]
# print(f"strings: {my_strings_list}")  # strings: ['comp sci', 'physics', 'elec engr', 'philosophy']
# print("Add/remove...")  # Add/remove...
# my_list.append(25)
# print(my_list)  # [15, 6, 7, 8, 35, 12, 14, 4, 10, 15, 25]
# my_list.insert(4, 25)
# print(my_list)  # [15, 6, 7, 8, 25, 35, 12, 14, 4, 10, 15, 25]
# my_strings_list.append(my_new_list)
# print(my_strings_list)  # ['comp sci', 'physics', 'elec engr', 'philosophy', ['art', 'econ']]  # a list inside a list


my_list = [15, 6, 7, 8, 35, 12, 14, 4, 10, 15]
my_strings_list = ["comp sci", "physics", "elec engr", "philosophy"]
my_new_list = ["art", "econ"]
print(f"Ints: {my_list}")  # Ints: [15, 6, 7, 8, 35, 12, 14, 4, 10]
# strings: ['comp sci', 'physics', 'elec engr', 'philosophy']
print(f"strings: {my_strings_list}")
print("Add/remove...")  # Add/remove...
my_list.append(25)
print(my_list)  # [15, 6, 7, 8, 35, 12, 14, 4, 10, 15, 25]
my_list.insert(4, 25)
print(my_list)  # [15, 6, 7, 8, 25, 35, 12, 14, 4, 10, 15, 25]
my_strings_list.extend(my_new_list)
# ['comp sci', 'physics', 'elec engr', 'philosophy', 'art', 'econ']
print(my_strings_list)
my_strings_list.remove("comp sci")
print(my_strings_list)  # ['physics', 'elec engr', 'philosophy', 'art', 'econ']
print(my_strings_list.pop())
print(my_strings_list)  # ['physics', 'elec engr', 'philosophy', 'art']
print("Sublists...")  # Sublists...
print(my_strings_list.pop())
print(my_strings_list) # ['physics', 'elec engr', 'philosophy']
print(my_list[-1])  # 25
print(my_list)  # [15, 6, 7, 8, 25, 35, 12, 14, 4, 10, 15, 25]
my_list[-1] = 1000
print(my_list) # [15, 6, 7, 8, 25, 35, 12, 14, 4, 10, 15, 1000]
print(my_list[4]) # 25
print(my_list[0:4])  # [15, 6, 7, 8]
print(my_list)  # [15, 6, 7, 8, 25, 35, 12, 14, 4, 10, 15, 1000]
print(my_list[:5])  # [15, 6, 7, 8, 25]
print(my_list)  # [15, 6, 7, 8, 25, 35, 12, 14, 4, 10, 15, 1000]
print(my_list[5:])  # [35, 12, 14, 4, 10, 15, 1000]
print(my_list)  # [15, 6, 7, 8, 25, 35, 12, 14, 4, 10, 15, 1000]
print(my_list[::])  # [15, 6, 7, 8, 25, 35, 12, 14, 4, 10, 15, 1000]
print(my_list)  # [15, 6, 7, 8, 25, 35, 12, 14, 4, 10, 15, 1000]
print(my_list[::2]) # [15, 7, 25, 12, 4, 15]
print(my_list)  # [15, 6, 7, 8, 25, 35, 12, 14, 4, 10, 15, 1000]
print(my_list[::-1])  # [1000, 15, 10, 4, 14, 12, 35, 25, 8, 7, 6, 15]
print(my_list)  # [15, 6, 7, 8, 25, 35, 12, 14, 4, 10, 15, 1000]
my_list.reverse()  # [15, 6, 7, 8, 25, 35, 12, 14, 4, 10, 15, 1000]
print(my_list)  # [1000, 15, 10, 4, 14, 12, 35, 25, 8, 7, 6, 15]
for item in my_list:
    print(item) # 1000
                # 15
                # 10
                # 4
                # 14
                # 12
                # 35
                # 25
                # 8
                # 7
                # 6
                # 15
