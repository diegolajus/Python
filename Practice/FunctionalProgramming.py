
from functools import reduce

#1 Capitalize all of the pet names and print the list

my_pets = ['sisi', 'bibi', 'titi', 'carla']

upper_list=[char.upper() for char in my_pets]
print('Question 1 -> ', upper_list)


#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.

my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

zip_item = zip(my_strings, sorted(my_numbers))

print('Question 2 -> ' , list(zip_item))


#3 Filter the scores that pass over 50%

scores = [73, 20, 65, 19, 76, 100, 88]

def over_fifty(scores):
  return scores>50

print('Question 3 -> ',list(filter(over_fifty,scores)))
  

#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

def sum(a,b):
  return a+b

print('Question 4 -> ' ,reduce(sum,my_numbers) + reduce(sum,scores))
