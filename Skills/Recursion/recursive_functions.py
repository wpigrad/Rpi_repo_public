
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

# Subset Sum Exists?
def subsetsum(S,T)-> bool:
	if T == 0:
		return True
	elif S == []:
		return False
	else:
		e = S[0]
		# two choices
		included = subsetsum(S[1:],T-e)
		not_included = subsetsum(S[1:],T)
		return included or not_included

######################################################################

# Subset Sum Solution Count
def subsetsum_count(S,T,count=0):
	if T == 0:
		# a solution was found
		count = count + 1
		return count
	elif S == []:
		# a solution was not found
		return count
	else:
		e = S[0]
		# two choices
		# included 
		new_count = subsetsum_count(S[1:],T-e,count)
		# not_included
		return subsetsum_count(S[1:],T,new_count)

######################################################################

def subsetsum_solution(S,T,solution):
	if T == 0:
		# a solution was found
		print(solution)
		return 
	elif S == []:
		# a solution was not found
		print("No solution found.")
		return
	else:
		e = S[0]
		# included
		print(f"e = {e}")
		print(f"solution = {solution}")
		subsetsum_solution(S[1:],T-e,solution.append(e))
		# not_included
		subsetsum_solution(S[1:],T,solution)
		
######################################################################

# Combination Sum I
# Given an array of distinct integers (candidates) and a target
# integer (target), return a list of all unique combinations of
# candidates where the chosen numbers sum to target. You may return
# the combinations in any order.
# Note: permutation -> order matters, combination -> does not matter
# The same number may be chosen from candidates an unlimited number
# of times. Two combinations are unique if the frequency of at least
# one of the chosen numbers is different.
# It is guaranteed that the number of unique combinations that sum
# up to target is less than 150 combinations for the given input.

# example:
#	Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]

# naive decision tree:
#  [2,3,6,7]---[2]---[2,2]---[2,2,2]---[2,2,2,2]x
#						|			|				+-[2,2,3]v duplicate
#						|			|				+-[2,2,6]x
#						|			|				+-[2,2,7]x
#						|			|
#						|			+-[2,3]---[2,3,2]v duplicate
#						|			|				+-[2,3,6]x
#						|			|				+-[2,3,7]x
#						|			|
#						|			+-[2,6]x
#						|			|
#						|			+-[2,7]x
#						|
#						+-[3]---[3,2]---[3,2,2]v duplicate
#						|			+-[3,3]---[3,3,2]x
#						|			|				+-[3,3,3]x
#						|			|				+-[3,3,6]x
#						|			|				+-[3,3,7]x
#						|			|
#						|			+-[3,6]x
#						|			+-[3,7]x
#						|
#						+-[6]---[6,2]x
#						|			+-[6,3]x
#						|			+-[6,6]x
#						|			+-[6,7]x
#						|
#						+-[7]v

# improved decision tree without duplicates:
# include element or not include element

#							include[2]
#  [2,3,6,7]---[2]---[2,2]---[2,2,2]---[2,2,2,2]x
#						|			|				+-[2,2,3]v
#						|			|				+-[2,2,6]x
#						|			|				+-[2,2,7]x
#						|			|
#						|			+-[2,3]---[2,3,3]x
#						|							+-[2,3,6]x
#						|							+-[2,3,7]x
#						|
#						| include[3]
#		not[2]	+-[3]---[3,3]---[3,3,3]x
#						|			|				+-[3,3,6]x
#						|			|				+-[3,3,7]x
#						|			|
#						|			+-[3,6]x
#						|			+-[3,7]x
#						|
#						| include[6]
#		not[3]	+-[6]---[6,6]x
#						|			+-[6,7]x
#						|
#						| include[7]
#		not[6]	+-[7]v

def cs1(candidates,target,subset):
	pass

######################################################################

# Combination Sum II
# Given a collection of candidate numbers (candidates) and a target
# number (target), find all unique combinations in candidates where
# the candidate numbers su to target.
# Each number in candidates is used only once in the combination.
# Note: The solution set must not contain duplicate combinations.

# Example
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: [[

def cs2():
	pass

#######################################################################

def cs_solution_exists(candidates,target,subset):
	if target == 0:
		# nothing left to pick from
		# backtrack
		return True
	elif candidates == []:
		# nothing to pick from
		# no solution
		# backtrack
		return False
	else:
		# pick from candidates
		e = candidates[0]

		# include element
		cs_solution_exists(candidates[1:],target-e,subset)
		# not include element
		cs_solution_exisits(candidates[1:],target,subset)

	#####################################################################

def cs(candidates,target,subset):
	if target == 0:
		# nothing left to pick from
		# backtrack
		return subset
	elif candidates == []:
		# nothing to pick from
		# no solution
		# backtrack
		return
	else:
		# pick from candidates
		e = candidates[0]

		# include element
		cs(candidates[1:],target-e,subset)
		# not include element
		cs(candidates[1:],target,subset)

	
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
		
#		print("Subset Sum")
#		sets = [[],[1],[1,2],[1,2,3],[1,2,3,4]]
#		targets = [0,1,2,3,4,5,6,7]
#		for S in sets:
#			for T in targets:
#				print(f"S = {S}, T = {T}")
#				answer = subsetsum(S,T)
#				print(f"A subset of S exists that sums to the target T: {answer}") 
#
#		new_function()
		
		S = [1,2,3,4]
		T = 5
		solution = []
		print(f"S = {S}, T = {T}")
		exists = subsetsum(S,T)
		print(f"A subset of S exists that sums to the target T: {exists}") 
		count = subsetsum_count(S,T)
		print(f"The number of subsets of S that sum to the target T: {count}")
		print("The subsets of S that sum to the target T:")
		subsetsum_solution(S,T,solution)
	
		new_function()

		print("Combination Sum")
		candidates = [2,3,6,7]
		print(candidates)
		target = int(input("Target = "))
		subset = []
		solution = cs(candidates,target,subset)
		print(solution)

		new_function()

		print("Continue?")
		condition = input_validation_from_list(["y","n"])

		new_function()

	end_program()

######################################################################

if __name__ == "__main__":
	main()
