import random

## practice -- archer class 
class Character:
    def __init__(self, name, health, attack, defense, class_type):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.class_type = class_type
        self.abilities = []

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name} takes {damage} damage! Health: {self.health}")

    def is_alive(self):
        return self.health > 0

    def attack_enemy(self, enemy):
        damage = max(0, self.attack - enemy.defense)
        print(f"{self.name} attacks {enemy.name} for {damage} damage.")
        enemy.take_damage(damage)


class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, 200, 40, 20, "Warrior")
        self.abilities = ["Slash", "Shield Block"]

    def use_ability(self, enemy):
        print(f"{self.name} uses Slash!")
        damage = random.randint(30, 50)
        print(f"{self.name} deals {damage} damage with Slash.")
        enemy.take_damage(damage)



class Archer(Character):
    def __init__(self, name):
        super().__init__(name, 120, 35, 15, "Archer")
        self.abilities = ["Arrow Shot", "Explosive Arrow"]

    def use_ability(self, enemy):
        print(f"{self.name} uses Explosive Arrow!")
        damage = random.randint(25, 45)
        print(f"{self.name} deals {damage} damage with Explosive Arrow.")
        enemy.take_damage(damage)


class Healer(Character):
    def __init__(self, name):
        super().__init__(name, 100, 15, 10, "Healer")
        self.abilities = ["Heal", "Divine Shield"]

    def use_ability(self, ally):
        print(f"{self.name} uses Heal!")
        heal_amount = random.randint(30, 50)
        print(f"{self.name} heals {ally.name} for {heal_amount} health.")
        ally.health += heal_amount

## enemy for dungeon 
class Enemy:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name} takes {damage} damage! Health: {self.health}")

    def is_alive(self):
        return self.health > 0

    def attack_player(self, player):
        damage = max(0, self.attack - player.defense)
        print(f"{self.name} attacks {player.name} for {damage} damage.")
        player.take_damage(damage)


class Dungeon:
    def __init__(self, name, enemies):
        self.name = name
        self.enemies = enemies

    def start_dungeon(self, player):
        print(f"{player.name} enters the {self.name} dungeon!")
        while player.is_alive() and len(self.enemies) > 0:
            enemy = self.enemies[0]
            print(f"A wild {enemy.name} appears!")
            player.attack_enemy(enemy)
            if enemy.is_alive():
                enemy.attack_player(player)
            else:
                print(f"{enemy.name} has been defeated!")
                self.enemies.pop(0)  # Remove defeated enemy

            if random.random() < 0.2:  # Random chance to use ability
                player.use_ability(enemy)

            if player.is_alive() and len(self.enemies) > 0:
                print("Next turn...\n")

        if player.is_alive():
            print(f"{player.name} has cleared the dungeon!")
        else:
            print(f"{player.name} has been defeated in the dungeon.")

