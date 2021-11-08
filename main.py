# 1. Fundamental Data Types
# int
# float
# complex
# str
# bool
# list
# dict
# tuple
# set

# 2. Classes -> Custom Types

# 3. Specialized Data Types

# 4. None


# Let's Start
# 1. Fundamental Data Types
# NUMBERS Data Types -> int and float

print(type(3 + 4))
print(type(3 - 4))
print(type(3 * 4))
print(type(3 / 4)) # o.75 This is a Floating Point Number

print(type(0))
print(type(0.00001))

print('---------------------------')
print('NUMBERS -> int and float')
print(2**2) # ** denotes To the Power of
print(2 // 2)  # // denotes Divided by and returns an integer type
print(6 % 4)  # % denoted Modulus and returns remainder 

# Math Functions
print(round(10.98))
print(abs(-20))

# Operator Precedence
print((20 - 3) + 2 ** 2)

# Order of Operators is as follows
# ()
# **
# * /
# + -

print(bin(5))
print(int('0b101', 2))

# STRING Data Type -> str
print('---------------------------')
print('STRING -> str')
print(type("Hi! How are you doing?"))

username = 'supercoder'
password = 'supersecret'
long_string = '''
Wow
O O
---
'''
print(long_string)

first_name = 'Virander'
last_name = 'Singh'
full_name = first_name + ' ' + last_name
print(full_name)

# String Concatenation
print('Virander ' + 'Singh')

# Type Conversion
# print(type(int(str(100))))
a = str(100)
b = int(a)
c = type(b)
print(c)

# Escape Sequence
weather = "\t It\'s \"kind of\" sunny. \n Hope you have a good day."
print(weather)

# Formatted Strings
name = 'Virander'
age = 29
# print('Hi ' + name + '. You are ' + str(age) + ' years old.')
# print('Hi {0}. You are {1} years old.'.format(name, age))    # A Way to do it in Python 2 and 3
print(f'Hi {name}. You are {age} years old.') # Python 3
print('Hello there! My name is %s and my age is %s' %(name, age))  # Hello there Andrei and Sunny --> you can also use %d, %f, %r for integers, floats, string representations of objects respectively

# String Indexes
selfish = '01234567'
        #  01234567

# [start:stop:stepover] # String Slicing
print(selfish[0:8:2])
print(selfish[1:])
print(selfish[:5])
print(selfish[::3])
print(selfish[-1])
print(selfish[::-1])  # Reversing a String

# Immutability
# String in Python are Immutable
selfish = '100'
print(selfish)  # You can change the value of the whole string but you cannot reassign a part of an indiviual string
# selfish[0] = '8' # This isn't possible in Python and hence strings are immutable

naam = 'Virander Singh'
print(naam[0:len(naam)])

# Python String Methods
quote = 'to be or not to be'
print(quote.upper())
print(quote.capitalize())
print(quote.find('be'))
quote2 = quote.replace('be', 'see', 2)
print(quote2)
print(quote)  # String are immutable and hence quote doesnt change. However, a new string quote2 can be created from quote
q = '  I am alone '
print(q.strip())               # Strips all whitespace characters from both ends.
r = 'On an island'
print(r.strip('d'))             # Strips all passed characters from both ends.
s = 'but life is good!'
print(s.split())           # ['but', 'life', 'is', 'good!']
t = 'Need to make fire'
print(t.startswith('Need')) # True
u = 'and cook rice'
print(u.endswith('rice'))      # True
v= 'bye bye'
print(v.index('e'))

# BOOLEAN Data Type -> bool
print('---------------------------')
print('BOOLEAN -> bool')
Name = 'Virander Singh'
is_cool = False
is_cool = True

print(bool(1))
print(bool('True'))

# all of the below evaluate to False. Everything else will evaluate to True in Python.
print(bool(None))
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool([]))
print(bool({}))
print(bool(()))
print(bool(''))
print(bool(range(0)))
print(bool(set()))

# Palindrome check
word = 'reviver'
print(word.find(word[::-1])) # 0
p = bool(word.find(word[::-1]) + 1)
print(p) # True

# Facebook Exercise
User_name = 'Virander Singh'
User_age = 29
relationship_status = 'Single'

relationship_status = 'It\'s Complicated'
print(relationship_status)

# Age Exercise
# birth_year = input('What year were you born?\n')
# Age = 2021 - int(birth_year)
# print(f'Your age is {Age}.')

# LIST Data Type -> list
# List is the first Data Structure in Python
print('---------------------------')
print('LIST -> list')
li = [1, 2, 3, 4]
li2 = ['a', 'b', 'c']
li3 = [1, 2, 'a', True]

# Amazon Example
# List Slicing
amazon_cart = [
  'notebooks', 
  'sunglasses',
  'toys',
  'grapes'
]
print(amazon_cart[0:2])
print(amazon_cart[0::2])

# Lists are Mutable
# Copying Vs Modifying a list
amazon_cart[0] = 'laptop'
new_cart = amazon_cart[:] # Copying a list
# new_cart = amazon_cart  # Modifying a list
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)

# Matrix -> 2D list
# Matrix is a multi-dimentional list
matrix = [
  [1, 5, 1],
  [0, 1, 0],
  [1, 0, 1]
]

print(matrix[0][1])

# List functions
basket = [1, 2, 3, 4, 5]
print(len(basket))

# List methods
# ADDING
# basket.append(100)  # append just modifys a list and doesn't create a new list
# basket.insert(4, 100) # insert just modifys a list and doesn't create a new list
basket.extend([100, 101, 102]) # extend just modifys a list and doesn't create a new list
new_list = basket
print(basket)
print(new_list)

# REMOVING
basket.pop()
basket.pop(0) # pop removes an object at the given index
print(basket)
New_list = basket.pop(3)  # pop method returns a value
print(New_list)

New_list1 = basket.remove(101)  # remove method doesn't return any value
print(New_list1)
basket.remove(100)  # remove removes the specified object
print(basket)

New_list2 = basket.clear()  # clear method doesn't return any value
print(New_list2)
basket.clear()  # clear removes the all the objects from the list
print(basket)

Basket = ['a', 'x', 'b', 'c', 'd', 'e', 'd']
# print(Basket.index('d', 0, 2))  # yields an error as 'd' is at index 3
print('d' in Basket)
print('i' in 'Hi my name is Virander Singh')
print(Basket.count('d'))

print(sorted(Basket)) # sorted function creates a copy of Basket and doesn't modify it.
print(Basket)
# new_Basket = Basket[:]  # This is same as sorted()
# new_Basket.sort()
# print(new_Basket)
# new_Basket = Basket.copy()  # This is same as above
# new_Basket.sort()
# print(new_Basket)

# Sorted reverse list
Basket.sort()
reverse_Basket = Basket.reverse()
print(Basket)

# sorted list
Basket.sort()
print(Basket)

print(Basket[::-1])

# Range is ussed for iteration
print(list(range (1, 100)))
print(list(range(101)))

# .join() is a string method that iterates a value in the given list
# sentence = '!'
# new_sentence = sentence.join(['Hi', 'my', 'name', 'is', 'Virander'])
new_sentence = '!'.join(['Hi', 'my', 'name', 'is', 'Virander'])  # This is the short hand way of writing the above code
print(new_sentence)

# List Unpacking
a,b,c, *other, d = [1,2,3,4,5,6,7,8,9]
print(a)
print(b)
print(c)
print(other)
print(d)

# NONE Data Type -> None
# None in Python is same as Null in other langauges
# None represents the absence of value
print('---------------------------')
print('NONE -> None')
weapons = None
print(weapons)

# DICTIONARY Data Type -> dict
# Dictionary is the second Data Structure in Python
# A Dictionary is an unordered key-value pair
print('---------------------------')
print('DICTIONARY -> dict')

Dictionary = {
  'a': 1,
  'b': 2,
  'x': 3
}

print(Dictionary['a'])
print(Dictionary)

Dictionary1 = {
  'c': [1,2,3],
  'd': 'hello',
  'e': True
}
print(Dictionary1['c'][1])

My_list = [
  {
  'c': [1,2,3],
  'd': 'hello',
  'e': True
},
{
  'c': [4,5,6],
  'd': 'hello',
  'e': True
}
]
print(My_list[0]['c'][2])

# Keys in Dictionary should be Unique can be anything thats Immutable. It cannot be a list as list is mutable
Dictionary2 = {
  123: [1,2,3],
  True: 'Hello',
  '[100]': True   # List is mutable and hence cannot be used as a key in a Dictionary
}
print(Dictionary2[123])

# Dictionary Methods
user = {
  'basket': [1,2,3],
  'greet': 'Hello',
  'age': 20
}
# print(user['age'])  # This gives an error if age isn't present in the Dictionary.
# So we use .get() method to avoid the error and to check if a key is present in the Dictionary or not
print(user.get('age'))  # Gives None as it isn't present in the Dictionary
print(user.get('age', 55)) # This checks if the key 'age' is present in the Dictionary or not. If not, then it creates this key in the dictionary with the given value
# However, if the key already exists, then it returns the value corresponding to it and ignores the override

# Creating a Dictionary usign a built-in function dict
user1 = dict(name= 'Virander')
print(user1)

# To check if a key or value or an item exists in a Dictionary or not using Dictionary Methods
print('size' in user)
print('age' in user.keys())
print('Hello' in user.values())
print(user.items())

user.clear()  # Clears the whole dictionary
print(user)

# After creating a copy of a dictionary and then clearing it, the copy of the Dictionary still exists
user2 = user1.copy()
print(user1.clear())
print(user2)

user3 = {
  'basket': [1,2,3],
  'greet': 'Hello',
  'age': 20
}
print(user3.pop('age'))
print(user3)

print(user3.popitem())  # popitem() removes a random item from the dictionary
print(user3)

print(user3.update({'age': 55})) # adds or updates the dictionary with additional key value pair
print(user3)

# TUPLE Data Type -> tuple
# Tuple is the third Data Structure in Python
# A Tuple is an immutable list. you cannot sort or reverse or modify a tuple unlike list. This makes code safe but less flexible
# Tuple is better than List in terms of Performance
print('---------------------------')
print('TUPLE -> tuple')
my_tuple = (1,2,3,4,5,5)
# my_tuple[0] = 'z' # You cannot do this like list as a tuple is immutable
print(my_tuple)
print(my_tuple[0])
print(5 in my_tuple)

user4 = {
  (1,2): [1,2,3],
  'greet': 'Hello',
  'age': 20
}
print(user4.items())
print(user4[(1,2)])

new_tuple = my_tuple[1:4]
print(new_tuple)

x,y,z, *other = (1,2,3,4,5)
print(x)
print(other)

# Tuple has only two methods and they are count() and index()  
print(my_tuple.count(5))
print(my_tuple.index(5))

# Built in function in Tuple
print(len(my_tuple))

# SET Data Type -> set
# Set is the fourth Data Structure in Python
# A Set is unordered collections of unique objects
print('---------------------------')
print('SET -> set')

my_set = {1,2,3,4,5,5}
print(my_set)
# print(my_set[0])  # indexes aren't present in sets
print(1 in my_set)
print(len(my_set))
print(list(my_set))

my_set.add(100)
my_set.add(2) # 2 doesn't get added as a set can contain just unique items
print(my_set)

my_list = [1,2,3,4,5,5]
print(set(my_list))

# Methods in Set
new_set = my_set.copy()
my_set.clear()
print(new_set)
print(my_set)

my_set1 = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}

# print(my_set1.difference(your_set)) # it finds difference of my_set1 from your_set

# my_set1.discard(5)
# print(my_set1)

# my_set1.difference_update(your_set) # this updates the my_set1 with the difference between my_set1 and your_set
# print(my_set1)

# print(my_set1.intersection(your_set)) # shows the common items between two sets
# print(my_set1 & your_set) # this is same as the above

#print(my_set1.isdisjoint(your_set)) # validates if there are common items in two sets and returns false if there are common items available

#print(my_set1.union(your_set))  # it unites two sets by eliminating the duplicates
# print(my_set1 | your_set) # this is same as the above

# print(my_set1.issubset(your_set)) # it is True if my_set has only 4 and 5 as items in it. As it vaidates if my_set1 is a part of your_set

# print(your_set.issuperset(my_set1)) # it is True if my_set has 4 and 5 as items in it. As it validates if your_set incorporates my_set1 in it 
