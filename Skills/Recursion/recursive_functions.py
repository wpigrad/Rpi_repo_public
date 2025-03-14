
import sys
sys.path.append("/Users/captain/Python/Rpi_repo_public")
from helper_functions import 	(start_program, end_program, new_function,
															input_validation_greater_or_equal_to,
															input_validation_from_list)

######################################################################
# Matryoshka Dolls
######################################################################

def even_numbers(number):

	# docstring
	# print(my_function.__doc__)
	# or
	# help(my_function)

	'''
	Returns all the positive even integers smaller or
	equal to the entered number using recursion.
	'''	

	# base cases
	if number == 0 or number == 1:
		print(f"No positive even numbers below {number}.")
		return

	if number % 2 == 1:
		number = number - 1
	
	print(number)

	if number == 2:
		return number
	else:
		return even_numbers(number-2)

######################################################################

def fibonacci(index_of_number):
	'''
	Returns the nth number in the Fibonacci sequence.
	'''

	if index_of_number <= 1:
		return index_of_number
	else:
		return fibonacci(index_of_number - 1) + fibonacci(index_of_number-2)

######################################################################

def main():
	condition = "y"
	while condition == "y":

		start_program()
	
		print("Input an integer value >=0:")
		number = input_validation_greater_or_equal_to(0)

		new_function()

		print(f"Even numbers less than or equal to {number}:")
		even_numbers(number)

		new_function()

		print("Fibonacci sequence: 0,1,1,2,3,5,8,13,21,34,55,89...")
		if number == 1:
			print(f"The {number}st Fibonacci number:")
		else:
			print(f"The {number}th Fibonacci number:")
		print(fibonacci(number))

		new_function()

		print("Continue?")
		condition = input_validation_from_list(["y","n"])

	end_program()

######################################################################

if __name__ == "__main__":
	main()
