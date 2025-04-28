import random

def combat_scenario():
    player_health = 100
    enemy_health = 75
    
    print("A wild beast appears!")
    
    while player_health > 0 and enemy_health > 0:
        print(f"\nYour health: {player_health}")
        print(f"Enemy health: {enemy_health}")
        
        action = input("Choose your action (attack/defend/run): ").lower()
        
        if action == "attack":
            player_damage = random.randint(10, 20)
            enemy_damage = random.randint(5, 15)
            
            player_health = player_health - enemy_damage
            enemy_health = enemy_health - player_damage
            
            print(f"You attack for {player_damage} damage.")
            print(f"The beast attacks for {enemy_damage} damage.")
            
        elif action == "defend":
            player_damage = 0
            enemy_damage = random.randint(0, 5)
            
            player_health = player_health - enemy_damage
            enemy_health = enemy_health - player_damage
            
            print(f"You defend, reducing damage to {enemy_damage}")
            print("The beast fails to damage you much.")
            
        elif action == "run":
            if random.random() < 0.5:
                print("You successfully escape!")
                return
            else:
                player_damage = 0
                enemy_damage = random.randint(10, 20)

                player_health = player_health - enemy_damage
                enemy_health = enemy_health - player_damage

                print(f"You fail to escape and the beast attacks for {player_damage} damage!")
        else:
            print("Invalid action. Try again.")
            continue
            
        if player_health <= 0:
            print("\nYou have been defeated!")
        elif enemy_health <= 0:
            print("\nYou have defeated the beast!")
            
    if player_health > 0 and enemy_health <= 0:
        print("Congratulations, you won the battle!")
    else:
        print("Better luck next time!")

def main():
    combat_scenario()

if __name__ == "__main__":
    main()
