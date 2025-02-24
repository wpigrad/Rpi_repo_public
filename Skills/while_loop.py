print("Start While Loop1 with Flags (set/check(+)/reset)")
flag = "yes"
while flag == "yes":
	print("In the While Loop.")
	flag = input("Continue While Loop? (yes or no): ")

print("End of While Loop1")
print("###################")
print("Start While Loop2 with Flags (set/check(-)/reset)")
flag = ""
while flag != "yes":
	print("In the While Loop.")
	flag = input("Quit While Loop? (yes or no): ")

print("End of While Loop2")
print("###################")
print("Start While Loop3 with If+break")
while True:
	print("In the While Loop.")
	flag = input("End program? (yes or no): ")
	if flag == "yes":
		break

print("End of While Loop3")
print("###################")
print("Start of While Loop4 for Input Validation")
while True:
	print("In the While Loop.")
	flag = input("Enter yes or no: ")
	if flag in ("yes","no"):
		print("Valid Input")
		break
	else:
		print("Invalid Input, Try Again.")

print("End of While Loop4")
print("###################")

