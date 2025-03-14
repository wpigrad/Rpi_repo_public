#####################################################################

def start_program():
	print("\n" + "#"*13)
	print("Start Program")
	print("#"*13 +"\n")


def end_program():
	print("\n" + "#"*13)
	print("End Program")
	print("#"*13 + "\n")


def new_function():
	print("\n" + "#"*13)
	print("New Function")
	print("#"*13 + "\n")

######################################################################

def input_validation_greater_or_equal_to(valid_input):
	choice = "not valid"
	while choice != "valid":
		value = input(f"Enter value >={valid_input}: ")
	
		if value.isdigit() == False:
			print("Invalid value, try again.")
		elif int(value) < valid_input:
			print("Invalid value, try again.")
		else:
			value = int(value)
			choice = "valid"
	return value

######################################################################

def input_validation_from_list(valid_list):
	choice = input(f"Enter choice:{valid_list}: ")
	while choice not in valid_list:
		print("Invalid choice, try again.")
		choice = input(f"Enter choice:{valid_list}: ")
	return choice

######################################################################

def main():

	condition = "y"
	while condition == "y":

		start_program()
	
		new_function()

		print("Continue?")
		condition = input_validation_from_list(["y","n"])

	end_program()

######################################################################

if __name__ == "__main__":
	main()
