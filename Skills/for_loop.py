# Name: Your name or you and your partner's names
# Date: 
# Per#: 
# title: for_loop.py

# pseudocode: Learn to use different types of for loops
# For loops are used when you know how many times to
# loop through or there is a clear end to the loop.
# A function uses parameters like start, stop, and step, 
# but the values passed are called arguments. 
# Note: Pay close attention to when the for loop ends 
# based on the 'stop' parameter.

print('\n*****\n')

# passing 3 arguments to the function range(start,stop,step)
for number in range(3,10,2):
	print(number)

print('\n*****\n')

# passing 2 arguments to the function range(start,stop)
for number in range(6,12):
	print(number)

print('\n*****\n')

# passing 1 argument to the function range(stop)
for number in range(5):
	print(number)

print('\n*****\n')

# looping through a list
my_list = ['x',13, 3.14, True]
for element in my_list:
	print(element)

print('\n*****\n')

# looping through a character string
string1 = 'string of characters'
for letter in string1:
	print(letter)

print('\n*****\n')

# looping through a list of names and numbering the names
names = ['Tim','Sue','Joe']
for number,name in enumerate(names):
	print(number,name)

# On your own, try to create a new for loop that will 
# enumberate the names starting at 1.

# On your own, try to create a countdown timer using 
# the time library and the sleep function
