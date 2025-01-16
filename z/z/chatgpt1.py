import random

class Character:
    def __init__(self, name, health, attack, defense, level):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.level = level

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        return self.health > 0
    


class Ability:
    def __init__(self, name, power, ability_type, critical_chance=0.1, elemental_bonus=1):
        self.name = name
        self.power = power
        self.ability_type = ability_type  # 'physical' or 'magical'
        self.critical_chance = critical_chance  # Chance of dealing critical damage
        self.elemental_bonus = elemental_bonus  # Elemental modifier (e.g., fire, water)

    def calculate_damage(self, attacker, target):
        # Base damage formula (simplified for this example)
        if self.ability_type == 'physical':
            # Physical damage calculation
            damage = (attacker.attack - target.defense) + self.power
        elif self.ability_type == 'magical':
            # Magical damage calculation
            damage = attacker.attack + self.power
        else:
            raise ValueError("Unknown ability type!")

        # Apply elemental bonus
        damage *= self.elemental_bonus

        # Check for critical hit
        if random.random() < self.critical_chance:
            print(f"{attacker.name}'s {self.name} landed a critical hit!")
            damage *= 2  # Critical hit doubles the damage

        # Ensure that damage cannot be negative
        damage = max(damage, 0)
        
        return damage
attacker = Character(name="Hero", health=100, attack=50, defense=20, level=10)
target = Character(name="Monster", health=100, attack=30, defense=10, level=8)

# Create abilities
fireball = Ability(name="Fireball", power=30, ability_type="magical", critical_chance=0.2, elemental_bonus=1.5)
slash = Ability(name="Slash", power=20, ability_type="physical", critical_chance=0.1, elemental_bonus=1)

# Calculate damage
print("Attacker Health:", attacker.health)
print("Target Health:", target.health)

# Attacker uses Fireball ability
damage = fireball.calculate_damage(attacker, target)
print(f"{attacker.name} used {fireball.name} on {target.name} and dealt {damage} damage!")
target.take_damage(damage)

print("Target's remaining health:", target.health)

# Attacker uses Slash ability
damage = slash.calculate_damage(attacker, target)
print(f"{attacker.name} used {slash.name} on {target.name} and dealt {damage} damage!")
target.take_damage(damage)

print("Target's remaining health:", target.health)