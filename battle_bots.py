import random

class Robot:
	def __init__(self,name="Tim",attack=5,defense=5,health=5,speed=5):
		self.name = name
		self.attack = attack
		self.defense = defense
		self.health = health
		self.speed = speed
		self.die_roll = 0

def battle(bot1,bot2):
	die = 6
	while bot1.health > 0 and bot2.health > 0:
		bot1.die_roll = random.randint(1,die)
		bot2.die_roll - random.randint(1,die)

		if bot1.speed >= bot2.speed:
			if bot2.defense > 0:
				bot2.defense = bot2.defense - 1
			else:
				bot2.health = bot2.health - bot1.attack

		else:
			if bot1.defense > 0:
				bot1.defense = bot1.defense - 1
			else:
				bot1.health = bot1.health - bot1.attack

	print("Game Over!")
	if bot1.health >= bot2.health:
		print("Player 1 Wins!")
	else:
		print("Player 2 Wins!")


print("Welcome to Battle Bots!")
play = input("Would you like to play? (y or n): ")
while play == "y":
	bot1 = Robot()
	bot2 = Robot()

	print("Player 1:")
	bot1.name = input("Enter name: ")
	print("You have 20 points total for 4 stats:")
	print("Attack, defense, health, and speed.")
	print("Choose wisely and good luck!")

	points = 20
	while points != 0:
		points = 20
		bot1.attack = int(input("Enter attack: "))
		bot1.defense = int(input("Enter defense: "))
		bot1.health = int(input("Enter health: "))
		bot1.speed = int(input("Enter speed: "))
		print(bot1.attack+bot1.defense+bot1.health+bot1.speed)
		points = points - bot1.attack - bot1.defense - bot1.health - bot1.speed
		print(points)

	print("Player 2:")
	bot2.name = input("Enter name: ")
	print("You have 20 points total for 4 stats:")
	print("Attack, defense, health, and speed.")
	print("Choose wisely and good luck!")

	points = 20
	while points != 0:
		points = 20
		bot2.attack = int(input("Enter attack: "))
		bot2.defense = int(input("Enter defense: "))
		bot2.health = int(input("Enter health: "))
		bot2.speed = int(input("Enter speed: "))
		print(bot2.attack+bot2.defense+bot2.health+bot2.speed)
		points = points - bot2.attack - bot2.defense - bot2.health - bot2.speed

	die = 6
	while bot1.health > 0 and bot2.health > 0:
		bot1.die_roll = random.randint(1,die)
		bot2.die_roll - random.randint(1,die)

		if bot1.speed >= bot2.speed:
			if bot2.defense > 0:
				bot2.defense = bot2.defense - 1
			else:
				bot2.health = bot2.health - bot1.attack

		else:
			if bot1.defense > 0:
				bot1.defense = bot1.defense - 1
			else:
				bot1.health = bot1.health - bot1.attack

	print("Game Over!")
	if bot1.health >= bot2.health:
		print("Player 1 Wins!")
	else:
		print("Player 2 Wins!")


	play = input("Play again? (y or n): ")
