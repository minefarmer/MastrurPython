greeting = "hello"
user = "richard"
message = "Welcome to the Algorithms course."
print(greeting, user, message)  # ('hello', 'richard', 'Welcome to the Algorithms course.')
print(greeting, user.capitalize(), message)  # ('hello', 'Richard', 'Welcome to the Algorithms course.')
# print(len(greeting))  # 5
# print(len(user))  # 7
# print(len(message))  # 33  ## includes white space
# print(type(message))  # <type 'str'>
# print(type(5))  # <type 'int'>
# print(id(greeting))  # 139991796219504
# print(id(user))  # 139991796219600
# print(dir(user))  # ['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

print(greeting.upper(), user.capitalize(), message)  # HELLO Richard Welcome to the Algorithms course.

print(greeting.upper(), user.capitalize(), message.lower())  # HELLO Richard welcome to the algorithms course.



# message = "       Welcome to the Algorithms course      ."
# print(greeting.upper(), user.capitalize(), message.lower())  # HELLO Richard        welcome to the algorithms course      .
# print(greeting.upper(), user.capitalize(), message.strip())  # HELLO Richard Welcome to the Algorithms course      .



print(greeting.upper(), user.capitalize(), message.lower())  # HELLO Richard        welcome to the algorithms course      .

print(message.find('course'))  # 26


print(greeting.upper(), user.capitalize(), message.strip())  # HELLO Richard Welcome to the Algorithms course      .

print(message.find('z'))  # -1 # There is no 'z' so it shows [  -1  ]

print(message.split())  # ['Welcome', 'to', 'the', 'Algorithms', 'course.']  # created a list of words.

# message = "Welcome-to-the-Algorithms-course."
# print(message.split())  # ['Welcome-to-the-Algorithms-course.']  # one string list.

# message = "Welcome-to-the-Algorithms-course."
# print(message.split("-"))  # ['Welcome', 'to', 'the', 'Algorithms', 'course.']


my_languages = ['Python', "Ruby", 'Javascript']
# print(" ".join(my_languages))  # Python Ruby Javascript  # a string, not a list.

import string
my_languages = ['Python', "Ruby", 'Javascript']
print(string.ascii_lowercase) # abcdefghijklmnopqrstuvwxyz

from string import ascii_lowercase
print(ascii_lowercase)  # abcdefghijklmnopqrstuvwxyz
