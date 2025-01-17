import random

class Robot:
	def __init__(self,name,power,defense,health,initiative,move):
		self.name = name
		self.power = power
		self.defense = defense
		self.health = health
		self.initiative = initiative
		self.move = move
		self.die_roll = 0

def battle(bot1,bot2):
	die = 6
	while bot1.health > 0 and bot2.health > 0:
		bot1.die_roll = random.randint(1,die)
		bot2.die_roll - random.randint(1,die)

		if bot1.initiative > bot2.initiative:
			starting_move = input(f"{bot1.name}, attack or defend? (a or d): ")
			if starting_move == "a":
				attack_move = bot1.
			else:

		else:
			

robot1 = Robot("Trish",7,1,1,1,10)
robot2 = Robot("Nathaniel",10,1,1,1,7)

print(robot1.__dict__)


battle(robot1,robot2)
