# Name: Your name or your name and your partner's name
# Date: 
# Per#: 
# Title: decorator_and_wrapper.py
# Pseudocode: Using a decorator and a wrapper to 
# modify the functionality of functions.

def my_decorator(func):
	def wrapper():
		print("Before calling the function.")
		func()
		print("After calling the function.")
	return wrapper

@my_decorator
def say_hello():
	print("Hello!")

def main():
	say_hello()

if __name__ == "__main__":
	main()
