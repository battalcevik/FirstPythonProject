# A Python Tuple
x_tuple = ('a', 'p', 'p', 'l', 'e')
y_tuple = tuple('apple')
z_tuple = ('apple', [1, 2], {1: 'NY', 2: 'LA'})

# A Python List
x_list = ['a', 'p', 'p', 'l', 'e']
y_list = list('apple')
z_list = ['apple', [1, 2], {1: 'NY', 2: 'LA'}]

# Show two different ways to construct x_list and x_tuple from x_str:
x_str = "apple"
# 1st way
x_list1 = list(x_str)
x_tuple1 = tuple(x_str)

# 2nd way
x_list2 = list()
for e in x_str:
    x_list2 = x_list2 + [e]

x_tuple2 = tuple()
for e in x_str:
    x_tuple2 = x_tuple2 + (e,)

print(x_list1, x_tuple1, x_list2, x_tuple2)

# Python Set and Dictionary
"""
A Python set is un-ordered, unique elements.
There are restrictions on elements.
"""

x_set = {'a', 'p', 'p', 'l', 'e'}
print("value of x_set: ", x_set)

y_set = set('apple')
z_set = set(x_str)
print("\n", x_set, y_set, z_set)
"""
A Python dictionary is a collection of (key, value) pairs.
Such pairs are called items.
There are built-in functions for keys, values and items.
"""
x_dict = {1: 'NY', 2: 'LA'}
target_key = 1
target_value = x_dict[target_key]
print(target_value)

"""
Iteration in Collections
"""
VOWELS = 'aeoiuy'
x_string = 'apple'
x_list = ['a', 'p', 'p', 'l', 'e']
x_tuple = ('a', 'p', 'p', 'l', 'e')
x_set = {'a', 'p', 'p', 'l', 'e'}
for e in x_string:
    if e in VOWELS:
        print(e, end='')
for e in x_list:
    if e in VOWELS:
        print(e, end='')
for e in x_tuple:
    if e in VOWELS:
        print(e, end='')
for e in x_set:
    if e in VOWELS:
        print(e, end='')

