# Tuples are immutable, which is the most important thing for them.

my_random_tuple = ('first',1,7,6,4,5,8, 'hi there',2,3,1,5,2,1,9,10)
my_tuple = ('first_value','third_value')

print(my_random_tuple[::-1])  # (10, 9, 1, 2, 5, 1, 3, 2, 'hi there', 8, 5, 4, 6, 7, 1, 'first')

print(dir(my_random_tuple))  # ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']

print(len(my_random_tuple))  # 16

print(my_random_tuple.index(5))  # 5

print(my_random_tuple.index('hi there'))  # 7


# first_var, second_var, third_var = my_tuple
# print(third_var)


print('first' in my_random_tuple)  # True


for item in my_random_tuple:
    print(item)  # first
                # 1
                # 7
                # 6
                # 4
                # 5
                # 8
                # hi there
                # 2
                # 3
                # 1
                # 5
                # 2
                # 1
                # 9
                # 10
