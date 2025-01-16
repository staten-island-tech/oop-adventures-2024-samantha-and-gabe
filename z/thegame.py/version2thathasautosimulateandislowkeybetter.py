import random
import json
import os


class Enemy:
    def __init__(self, name, health, damage, defense, gold):
        self.name = name
        self.health = health
        self.damage = damage
        self.defense = defense
        self.gold = gold

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name} takes {damage} damage! Health: {self.health}")

    def is_alive(self):
        return self.health > 0

    def damage_player(self, player):
        damage = max(0, self.damage - player.defense)
        print(f"{self.name} damages {player.name} for {damage} damage.")
        player.take_damage(damage)


class Weapon:
    def __init__(self, name, damage, strength, ecc, critdmg, price):
        self.name = name
        self.damage = damage
        self.strength = strength
        self.ecc = ecc
        self.critdmg = critdmg
        self.price = price

    def to_dict(self):
        return {
            'name': self.name,
            'damage': self.damage,
            'strength': self.strength,
            'ecc': self.ecc,
            'critdmg': self.critdmg,
            'price': self.price
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['name'], data['damage'], data['strength'], data['ecc'], data['critdmg'], data['price'])


class Armor:
    def __init__(self, name, additional_hp, defense, strength, price):
        self.name = name
        self.additional_hp = additional_hp
        self.defense = defense
        self.strength = strength
        self.price = price

    def to_dict(self):
        return {
            'name': self.name,
            'additional_hp': self.additional_hp,
            'defense': self.defense,
            'strength': self.strength,
            'price': self.price
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['name'], data['additional_hp'], data['defense'], data['strength'], data['price'])


class Character:
    def __init__(self, name, health, damage, defense):
        self.name = name
        self.health = health
        self.damage = damage
        self.defense = defense
        self.abilities = []
        self.inventory = [] 
        self.equipped_weapon = None  
        self.equipped_armor = None  
        self.gold = 0 

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name} takes {damage} damage! Health: {self.health}")

    def is_alive(self):
        return self.health > 0

    def damage_enemy(self, enemy):
        damage = self.damage
        if self.equipped_weapon:
            damage += self.equipped_weapon.damage
        damage = max(0, damage - enemy.defense)
        print(f"{self.name} damages {enemy.name} for {damage} damage.")
        enemy.take_damage(damage)

    def equip_weapon(self, weapon):
        self.equipped_weapon = weapon
        self.damage += weapon.damage
        print(f"{self.name} equipped {weapon.name}. New damage: {self.damage}")

    def equip_armor(self, armor):
        self.equipped_armor = armor
        self.health += armor.additional_hp
        self.defense += armor.defense
        print(f"{self.name} equipped {armor.name}. New health: {self.health}, New defense: {self.defense}")

    def view_stats(self):
        print(f"\n--- {self.name}'s Stats ---")
        print(f"Health: {self.health}")
        print(f"Damage: {self.damage}")
        print(f"Defense: {self.defense}")
        print(f"Gold: {self.gold}")
        if self.equipped_weapon:
            print(f"Equipped Weapon: {self.equipped_weapon.name}")
        if self.equipped_armor:
            print(f"Equipped Armor: {self.equipped_armor.name}")
        
    def open_inventory(self):
        print("\n--- Inventory ---")
        if not self.inventory:
            print("Your inventory is empty.")
            return
        
        print("1. View Potions")
        print("2. View Weapons")
        print("3. View Armor")
        print("4. Close inventory")
        
        option = input("Choose an option: ")
        
        try:
            option = int(option)
            if option == 1:
                self.view_potions()
            elif option == 2:
                self.view_weapons()
            elif option == 3:
                self.view_armor()
            elif option == 4:
                print("Closing inventory.")
            else:
                print("Invalid input. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        
    def view_potions(self):
        print("\n--- Potions ---")
        potions = [item for item in self.inventory if isinstance(item, dict)]
        if not potions:
            print("No potions in inventory.")
            return
        for idx, potion in enumerate(potions, start=1):
            print(f"{idx}. {potion['name']}: {potion['effect']}")
        try:
            choice = int(input("Choose a potion to use: ")) - 1
            if 0 <= choice < len(potions):
                self.use_potion(potions[choice])
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        
    def use_potion(self, potion):
        print(f"You used {potion['name']}!")
        self.inventory.remove(potion)
        if potion['name'] == "Health Potion":
            self.health += 50
            print(f"Health increased by 50. Current health: {self.health}")
        elif potion['name'] == "Damage Potion":
            self.damage += 10
            print(f"Damage increased by 10. Current damage: {self.damage}")
        elif potion['name'] == "Defense Potion":
            self.defense += 10
            print(f"Defense increased by 10. Current defense: {self.defense}")
        # Add more potions effects as needed.

    def view_weapons(self):
        print("\n--- Weapons ---")
        weapons = [item for item in self.inventory if isinstance(item, Weapon)]
        if not weapons:
            print("No weapons in inventory.")
            return
        for idx, weapon in enumerate(weapons, start=1):
            print(f"{idx}. {weapon.name}: {weapon.damage} damage, {weapon.price} gold")
        try:
            choice = int(input("Choose a weapon to equip: ")) - 1
            if 0 <= choice < len(weapons):
                self.equip_weapon(weapons[choice])
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def view_armor(self):
        print("\n--- Armor ---")
        armors = [item for item in self.inventory if isinstance(item, Armor)]
        if not armors:
            print("No armor in inventory.")
            return
        for idx, armor in enumerate(armors, start=1):
            print(f"{idx}. {armor.name}: {armor.additional_hp} HP, {armor.defense} defense, {armor.price} gold")
        try:
            choice = int(input("Choose armor to equip: ")) - 1
            if 0 <= choice < len(armors):
                self.equip_armor(armors[choice])
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, 200, 40, 20)
        self.abilities = ["Slash", "Shield Block"]

    def use_ability(self, enemy):
        print(f"{self.name} uses Slash!")
        damage = random.randint(30, 50)
        print(f"{self.name} deals {damage} damage with Slash.")
        enemy.take_damage(damage)


class Merchant:
    def __init__(self, dungeon_level):
        self.dungeon_level = dungeon_level
        self.items = {
            'Weapon': [
                Weapon("Aspect of the Dragons", 100 + dungeon_level * 2, 50 + dungeon_level, 10, 25, 500),
                Weapon("Livid Dagger", 75 + dungeon_level * 2, 40 + dungeon_level, 15, 50, 400),
                Weapon("Hyperion", 300, 150, 10, 200, 1500),
            ],
            'Armor': [
                Armor("Necron's Armor", 200 + dungeon_level * 5, 100 + dungeon_level, 50, 700),
                Armor("Shadow Assassin Armor", 150 + dungeon_level * 5, 75 + dungeon_level, 40, 600),
            ],
            'Potions': [
                {"name": "Health Potion", "effect": "Restore 50 HP", "price": 50},
                {"name": "Damage Potion", "effect": "Increase damage by 10 for next dungeon", "price": 75},
            ],
        }

    def display_items(self):
        print("\nItems for sale:")
        item_id = 1
        for category, items in self.items.items():
            print(f"{category}:")
            for item in items:
                if isinstance(item, Weapon) or isinstance(item, Armor):
                    print(f"{item_id}. {item.name}: {item.damage if isinstance(item, Weapon) else item.additional_hp} {('damage' if isinstance(item, Weapon) else 'HP')}, {item.price} gold")
                elif isinstance(item, dict):  
                    print(f"{item_id}. {item['name']}: {item['effect']}, {item['price']} gold")
                item_id += 1

    def sell_item(self, player):
        while True:
            print("\nOptions:")
            print("1. Buy items")
            print("2. Leave merchant")
            choice = input("Choose an option: ")

            try:
                choice = int(choice)
                if choice == 1:
                    print("\nChoose an item to buy:")
                    self.display_items()

                    try:
                        choice = int(input("Enter the number of the item you want to buy: ")) - 1
                        all_items = sum(self.items.values(), [])
                        if choice < 0 or choice >= len(all_items):
                            print("Invalid choice. Returning to merchant.")
                            continue

                        item = all_items[choice]
                        price = item.price if isinstance(item, (Weapon, Armor)) else item['price']

                        if player.gold >= price:
                            confirm = input(f"This will cost {price} gold. Confirm purchase? (yes/no): ").lower()
                            if confirm == 'yes':
                                player.gold -= price
                                if isinstance(item, dict):  # Potions
                                    print(f"You bought a {item['name']}. Effect: {item['effect']}")
                                    player.inventory.append(item)
                                else:
                                    player.inventory.append(item)
                                    print(f"You have bought {item.name}.")
                                    equip = input(f"Do you want to equip {item.name}? (yes/no): ").lower()
                                    if equip == 'yes':
                                        if isinstance(item, Weapon):
                                            player.equip_weapon(item)
                                        elif isinstance(item, Armor):
                                            player.equip_armor(item)
                            else:
                                print("Purchase canceled.")
                        else:
                            print("Not enough gold!")
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")
                elif choice == 2:
                    print("Leaving the merchant.")
                    break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")


def save_game(player):
    game_data = {
        'name': player.name,
        'health': player.health,
        'damage': player.damage,
        'defense': player.defense,
        'gold': player.gold,
        'inventory': player.inventory,
        'equipped_weapon': player.equipped_weapon,
        'equipped_armor': player.equipped_armor,
    }
    with open(f"{player.name}_game_save.json", 'w') as file:
        json.dump(game_data, file)


def load_game():
    if not os.path.exists("game_save.json"):
        print("No save file found!")
        return None

    with open("game_save.json", 'r') as file:
        game_data = json.load(file)
        player = Warrior(game_data['name'])
        player.health = game_data['health']
        player.damage = game_data['damage']
        player.defense = game_data['defense']
        player.gold = game_data['gold']
        player.inventory = game_data['inventory']
        return player


def warrior1():
    # Creating the player object and starting the game
    player = Warrior("Warrior1")
    player.inventory = [
        Weapon("Basic Sword", 20, 5, 0, 0, 100),
        Armor("Basic Armor", 50, 10, 0, 50),
        {"name": "Health Potion", "effect": "Restores 50 HP", "price": 50}
    ]
    player.gold = 300

    dungeon_level = 1

    while dungeon_level <= 1000:
        print(f"\n--- Dungeon {dungeon_level} ---")
        print(f"{player.name} is battling enemies.")
        
        # Simulating an enemy encounter (simplified)
        enemy = Enemy("Goblin", 100, 20, 5, 50)
        while enemy.is_alive() and player.is_alive():
            print(f"\n{player.name}'s Turn:")
            player.damage_enemy(enemy)
            if enemy.is_alive():
                enemy.damage_player(player)

        if not player.is_alive():
            print("Game Over! You have been defeated.")
            return

        while True:
            print("\nOptions:")
            print("1. Save and quit")
            print("2. Continue to the merchant")
            print("3. Skip merchant and go to the next dungeon")
            print("4. View stats")
            print("5. View inventory")
            option = input("Choose an option: ")

            if option == '1':
                save_game(player)
                print("Thanks for playing!")
                return
            elif option == '2':
                merchant = Merchant(dungeon_level)
                merchant.sell_item(player)
                break
            elif option == '3':
                print("Skipping merchant and moving to the next dungeon...")
                break
            elif option == '4':
                player.view_stats()
            elif option == '5':
                player.open_inventory()
            else:
                print("Invalid input. Please choose a valid option.")

        dungeon_level += 1

warrior1()