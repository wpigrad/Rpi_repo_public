import random
import time

def helper_function(number):
	products = []
	print("#################################################")
	for factor in range(13):
		products.append(number*factor) 
		print(f"{number} x {factor} = {products[factor]}")
	print("#################################################")


spacer = "#################################################"
print(spacer)
print("Welcome to Mr. Jacobson's Multiplication Program!")
print(spacer)

again = "y"
while again != "n":
	helper = input("Would you like the helper function? (y or n): ")
	timed = input("Timed Practice? (y or n): ")
	if timed == "y":
		minutes = int(input("How many minutes?: "))
		seconds = minutes * 60
		qty = 1000
	else:
		qty = int(input("Number of Questions?: "))
	number = int(input("What number would you like to practice?: "))
	correct = 0

	start_time = time.time()
	total_time = 0
	while total_time < seconds or timed == "y":
		for _ in range(qty):
			factor = random.randint(0,12)
			product = number * factor
			order = random.randint(0,1)
			if order == 0:
				factors = (number,factor)
			else:
				factors = (factor, number)
			if helper == "y":
				helper_function(number)

			question = f"{factors[0]} x {factors[1]} = "

			for prompt in question, "Try Again: ":
				answer = int(input(prompt))
				if answer == product:
					correct = correct + 1
					print("Correct!")
					print(spacer)
					break

				time.sleep(1)

			else:
				print(f"{question}{product}")
				print(spacer)
				time.sleep(1)

		end_time = time.time()
		total_time = round((end_time - start_time),0)

	percent = round((correct/qty)*100,1)

	print(spacer)
	comments = ["Great job!","Nice Job!","Good Try!"]
	if percent > 75:
		print(comments[0])
	elif percent > 50:
		print(comments[1])
	else:
		print(comments[2])

	print(f"{total_time} seconds for {qty} questions on {number}'s at {percent}%")
	print(spacer)
	again = input("Practice again? (y or n): ")
	print(spacer)

print("Goodbye.")
