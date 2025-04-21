def heading(my_string):
	print("#"*13)
	print(my_string)
	print("#"*13)

def add_numbers(number1,number2):
	sum_of_numbers = number1 + number2
	heading(f"{number1} + {number2} = {sum_of_numbers}")

def subtract_numbers(number1,number2):
	difference_of_numbers = number1 - number2
	heading(f"{number1} - {number2} = {difference_of_numbers}")

def multiply_numbers(number1,number2):
	product_of_numbers = number1 * number2
	heading(f"{number1} * {number2} = {product_of_numbers}")

def divide_numbers(number1,number2):
	quotient_of_numbers = number1 / number2
	heading(f"{number1} / {number2} = {quotient_of_numbers}")

def main():
	heading("Start Program")
	number1 = int(input("Enter first integer: "))
	number2 = int(input("Enter second integer: "))
	
	operation = input("Enter operation (+, -, *, or /): ")
	if operation == "+":
		add_numbers(number1,number2)
	elif operation == "-":
		subtract_numbers(number1,number2)
	elif operation == "*":
		multiply_numbers(number1,number2)
	elif operation == "/":
		divide_numbers(number1,number2)
	else:
		print("Not a valid choice")

	heading("End Program")

if __name__ == "__main__":
	main()
