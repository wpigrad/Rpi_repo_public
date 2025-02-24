# pseudocode: Use the getpass library and function
# to get user input without showing what was entered
# on the screen.

import getpass
import os

os.system("clear")
user = input("Enter your name: ")
password = True
check = False
while password != check:
	password = getpass.getpass("Set Password: ")
	check = getpass.getpass("Re-enter Password: ")
	if password != check:
		os.system("clear")
		print("Did not match. Try again.")

os.system("clear")
print("Welcome " + user + ".") 

tries = 3
access = False
while access == False:

	check = getpass.getpass("Please enter your password: ")
	tries = tries - 1

	if password == check:
		access = True
		os.system("clear")
		print("Access Granted.")
	else:
		os.system("clear")
		if tries > 1:
			print("Acess Denied. You have", tries, "tries remaining.")
		elif tries == 1:
			print("Acess Denied. You have", tries, "try remaining.")
		else:
			while tries == 0:
				os.system("clear")
				print("Please wait for security.")
				input()

