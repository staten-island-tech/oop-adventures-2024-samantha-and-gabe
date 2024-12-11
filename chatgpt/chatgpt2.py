import random

class Character:
    def __init__(self, name, health, attack_power, defense):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.defense = defense

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0  # Health should never go below 0
        print(f"{self.name} takes {damage} damage! Health is now {self.health}")

    def is_alive(self):
        return self.health > 0

def calculate_damage(attacker, defender):
    # Random factor to make attacks a little less predictable
    damage_variance = random.uniform(0.8, 1.2)
    base_damage = attacker.attack_power * damage_variance

    # Calculate the effective damage by considering the defender's defense
    effective_damage = max(0, base_damage - defender.defense)

    return effective_damage

def attack(attacker, defender):
    print(f"{attacker.name} attacks {defender.name}!")
    damage = calculate_damage(attacker, defender)
    defender.take_damage(damage)

# Example of two characters: an attacker and a defender
player = Character(name="Player", health=100, attack_power=25, defense=5)
enemy = Character(name="Enemy", health=80, attack_power=20, defense=3)

# Simulate a battle round where the player attacks the enemy
attack(player, enemy)

# Check if the enemy is still alive
if not enemy.is_alive():
    print(f"{enemy.name} has been defeated!")
else:
    print(f"{enemy.name} is still standing with {enemy.health} health.")