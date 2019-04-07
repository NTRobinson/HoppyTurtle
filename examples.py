import random
import sys
import os

print("Hello world, dis Python")
# dis is a comments

name = "Nathan"
print(name)
name = 14 # this is fine because of how variables behave in Python

# Data Types: numbers, strings, lists, tuples, dictionaries/maps
# Arithmetic Operators: + - * / % ** //

# This is how lists work.
sample_list = ['stuff' , 'things', 'objects', 'ideas']
print(sample_list);

sample_list.sort()
removed = sample_list.remove(sample_list[0])
sample_list.insert(0, 'BOOMSHACKALACKA')
print(sample_list)

sample_list.remove('things')
print(sample_list)

sample_list.remove('stuff')
print(sample_list)

sample_list.remove('objects')
print(sample_list)

del sample_list[0]

# tuples - can't be changed after instantiated
tuple = (1, 2, 6, 12)
new_list = list(tuple)

# dictionaries/maps - officially called maps
super_villains = {'Riddler' : 'John Jingle',
                  'Captain Cold' : 'Leonard Snart',
                  'Weather Wizard' : 'Mark Mardon'}

print(super_villains['Captain Cold'])
del super_villains['Riddler']
super_villains['Riddler'] = 'Hartley Rathaway'
print(super_villains.get("Weather Wizard"))

print(super_villains.keys())
print(super_villains.values())

# if else elif == != > >= < <=
age = 21

if age >= 21 :
    print('You are old enough to rent and drive a car')
elif age >= 16 :
    print('You are old enough to drive a car')
else :
    print('You are NOT old enough to drive')

# looping
for x in range(0, 10):
    print(x, ' ', end="")
print('\n')

grocery_list = ['Juice', 'Tomatoes', 'Potatoes']
for y in grocery_list:
    print(y)

rand_num = random.randrange(0, 10)

while(rand_num != 7):
    print(rand_num)
    rand_num = random.randrange(0, 10)