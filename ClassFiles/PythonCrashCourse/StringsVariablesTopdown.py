'''                 Variables

Variables are memory location references which store values.
    Address to values in my computer's memory.

my_message               =          'Hello World using single quotes'.
    |                    |                   |       
memory location     assignment operator  string to be referenced



'''

# my_message = 'Hello World using single quotes.'
# print(my_message)  # Hello World using single quotes.




'''                 Strings
        Concatenation, indexing, slicing.
'''

# message = "The price of the stock is:"
# price = "$1100"
# print(message + " " + price)  # The price of the stock is: $1100


# message = "The price of the stock is: "
# price = "$1100"
# print(message + price)  # The price of the stock is: $1100


# new_message = message + price
# print(new_message)  # The price of the stock is: $1100
# print(id(message))  # 2015286636912


# price = "$1100"
# new_message = message + price
# print(new_message)  # The price of the stock is: $1100
# print(id(new_message))  # 2118872002352




'''                 Indexing

I n t e r s t e l l a  r
0 1 2 3 4 5 6 7 8 9 10 11

name = Interstellar
name[0]  # I
name[6]  # t
name[11]  # r
name[-1]  # r


>>> name = "Interstellar"
>>> name
'Interstellar'
>>> name[0]
'I'
>>> name[6]
't'
>>> name[11]
'r'
>>> name[-1]
'r'
>>> name[-1] = "n"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>>

'''



'''                 Slicing

I n t e r s t e l l a  r
0 1 2 3 4 5 6 7 8 9 10 11

name[:5]  # I n t e r
name(5:)  # s t e l l a  r
name[:]  # I n t e r s t e l l a  r


nums = "0123456789"

nums[     :         : 2 ]
    start   Stop+1   Step size
    output: "24"

nums[  2  :    6    : -1 ]
    start   Stop+1   Step size
    output: "9876543210"

'''

