# Name: Your name or you and your partner's name
# Date:
# Per#:
# Title: heor_clash.py
# Pseudocode: Create a program that 

class Character:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def __str__(self):
         return f"{self.name}: Health - {self.health}, Attack - {self.attack}"

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name} took {damage} damage. Current health: {self.health}")

    def attack_enemy(self, enemy):
        print(f"{self.name} attacks {enemy.name}!")
        enemy.take_damage(self.attack)

def main():
    hero = Character("Hero", 100, 20)
    enemy = Character("Enemy", 80, 15)

    print(hero)
    print(enemy)

    hero.attack_enemy(enemy)
    enemy.attack_enemy(hero)

    print(hero)
    print(enemy)

if __name__ == "__main__":
    main()
