#####################################
# for vs while vs recursion
#####################################

import os

os.system("clear")

#####################################

def print_header(string_to_print: str, n=33) -> None:

	print("#"*n)
	print(string_to_print)
	print("#"*n)

#####################################

def count_to_the_number_n(n: int) -> None:

	count = 0
	for _ in range(0,n,1):
		count = count + 1
	print(f"for count to n = {count}")

	#-----------------------------------#

	count = 0
	while count < n:
		count = count + 1
	print(f"while count to n = {count}")

	#-----------------------------------#

	count = 0
	count = count_elements(n)
	print(f"recursion count to n = {count}")


#####################################

def count_to_n(n: int) -> int:
	if n == 0:
		return 0
	else:
		return count_to_n(n-1) + 1


#####################################

def count_the_elements(value_list: list[int]) -> None:

	count = 0
	for element in value_list:
		count = count + 1
	print(f"for count elements = {count}")

	#-----------------------------------#

	n = len(value_list)
	count = 0
	while count < n:
		count = count + 1
	print(f"while count elements = {count}")

	#-----------------------------------#

	count = 0
	n = len(value_list)
	count = count_elements(n)
	print(f"recursion count elements = {count}")


#####################################

def count_elements(n: int) -> int:

	if n == 0:
		return 0
	else:
		return count_elements(n-1) + 1

#####################################

def count_the_ones(value_list: list[int]) -> None:

	result = 0
	for element in value_list:
		if element == 1:
			result = result + 1

	print(f"for count ones = {result}")

	#-----------------------------------#

	result = 0
	n = len(value_list)
	index = 0
	while index < n:
		if value_list[index] == 1:
			result = result + 1
		index = index + 1

	print(f"while count ones = {result}")
 
	#-----------------------------------#

	result = count_ones_front_to_back(value_list)
	print(f"recursive count ones front to back = {result}")
	result = count_ones_back_to_front(value_list)
	print(f"recursive count ones back to front = {result}")

#####################################

def count_ones_front_to_back(value_list: list[int]) -> int:

	# base case: if the list is empty, return 0
	if not value_list:
		return 0
	# recursive case: check the first element and recurse on the rest
	return (1 if value_list[0] == 1 else 0) + count_ones_front_to_back(value_list[1:])

#####################################

def count_ones_back_to_front(value_list: list[int]) -> int:

	# base case: if the list is empty, return 0
	if not value_list:
		return 0
	# recursive case: check the first element and recurse on the rest
	return (1 if value_list[-1] == 1 else 0) + count_ones_back_to_front(value_list[:-2])


#####################################

def main():

	key_list    = [1,2,3,4,5]

	value_list0 = [1,2,3,4,5]			# in order
	value_list1 = [5,4,3,2,1]			# out of order
	value_list2 = [1,0,0,1,1]			# on/off
	value_list3 = [3,4,5,6,7]			# odd/even
	value_list4 = [True,False,True,True,False]	# is black
	value_list5 = [-1,3,2,-1,-1]			# has ramp

	index_list  = [0,1,2,3,4]

	my_dict0 = dict(zip(key_list,value_list0))

	n = len(index_list)

	print_header("Variables:")
	print(f"key   = {key_list}")
	print(f"value = {value_list0}")
	print(f"index = {index_list}")
	print(f"dictionary = {my_dict0}")
	print(f"n = {n}")

	print_header(f"Count to the number n: {n}")
	count_to_the_number_n(n)

	print_header(f"Count Elements: {value_list0}")
	count_the_elements(value_list0)

	print_header(f"Count Ones: {value_list2}")
	count_the_ones(value_list2)

#####################################

if __name__ == "__main__":
	main()
