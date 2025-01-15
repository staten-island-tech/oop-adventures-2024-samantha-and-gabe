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

class Armor:
    def __init__(self, name, additional_hp, defense, strength, price):
        self.name = name
        self.additional_hp = additional_hp
        self.defense = defense
        self.strength = strength
        self.price = price


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
                Weapon("Reaper Scythe", 250, 100, 5, 50, 1800),
                Weapon("Spirit Bow", 200, 80, 10, 20, 1400),
                Weapon("JuJu Shortbow", 220, 90, 15, 30, 1500),
                Weapon("AotE", 120, 60, 5, 10, 800),
                Weapon("Valkyrie", 350, 200, 10, 50, 2000),
            ],
            'Armor': [
                Armor("Necron's Armor", 200 + dungeon_level * 5, 100 + dungeon_level, 50, 700),
                Armor("Shadow Assassin Armor", 150 + dungeon_level * 5, 75 + dungeon_level, 40, 600),
                Armor("Young Dragon Armor", 300, 200, 50, 1300),
                Armor("Old Dragon Armor", 500, 400, 25, 1500),
                Armor("Crystal Armor", 250, 150, 50, 1400),
                Armor("Goldor’s Armor", 400, 450, 50, 1800),
                Armor("Dragon Hunter Armor", 350, 300, 75, 1700),
            ],
            'Potions': [
                {"name": "Health Potion", "effect": "Restore 50 HP", "price": 50},
                {"name": "Damage Potion", "effect": "Increase damage by 10 for next dungeon", "price": 75},
                {"name": "Defense Potion", "effect": "Increase defense by 10 for next dungeon", "price": 75},
                {"name": "Strength Potion", "effect": "Increase strength by 30 for 1 dungeon", "price": 100},
                {"name": "Speed Potion", "effect": "Increases movement speed by 25% for 2 minutes", "price": 80},
                {"name": "Magic Resistance Potion", "effect": "Reduces magic damage by 20%", "price": 120},
                {"name": "Adrenaline Potion", "effect": "Increases attack speed by 20%", "price": 90},
                {"name": "Critical Potion", "effect": "Increases crit chance by 10%", "price": 120},
            ],
            'Utility': [
                {"name": "Overflux Orb", "effect": "Regenerates 100 health and 50 mana", "price": 1000},
                {"name": "Fishing Rod of Champions", "effect": "Grants bonus loot when fishing", "price": 900},
                {"name": "Builder's Wand", "effect": "Speeds up building", "price": 700},
                {"name": "Wand of Restoration", "effect": "Heals 200 HP instantly", "price": 400},
                {"name": "Power Orb", "effect": "Boosts all stats by 10%", "price": 1200},
            ]
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

            if choice == '1':
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
                    print("Invalid input. Returning to merchant.")
            elif choice == '2':
                print("Leaving the merchant and returning to options menu...")
                break
            else:
                print("Invalid choice. Please choose a valid option.")




class Dungeon:
    def __init__(self, name, dungeon_level):
        self.name = name
        self.dungeon_level = dungeon_level
        self.enemies = self.generate_enemies()

    def generate_enemies(self):
        dungeon_themes = {
            "Dark Forest": ["Shadow Fiend", "Vampire Bat", "Corrupted Tree"],
            "Fire Caverns": ["Fire Wraith", "Lava Beast", "Flame Serpent"],
            "Frozen Peaks": ["Ice Golem", "Frost Specter", "Yeti"],
            "Haunted Ruins": ["Ghost", "Skeleton Warrior", "Necromancer"],
            "Abyssal Depths": ["Sea Serpent", "Kraken Tentacle", "Abyssal Shadow"],
        }

        
        theme = random.choice(list(dungeon_themes.keys()))
        print(f"The theme of this dungeon is: {theme}")
        enemy_types = dungeon_themes[theme]

        
        enemies = []
        num_enemies = self.dungeon_level // 5 + 1
        for i in range(num_enemies):
            enemy_type = random.choice(enemy_types)
            if enemy_type == "Shadow Fiend":
                enemies.append(Enemy(f"Shadow Fiend {i + 1}",
                                      40 + self.dungeon_level * 4,
                                      15 + self.dungeon_level * 3,
                                      3 + self.dungeon_level,
                                      15 + self.dungeon_level * 4))
            elif enemy_type == "Vampire Bat":
                enemies.append(Enemy(f"Vampire Bat {i + 1}",
                                      30 + self.dungeon_level * 3,
                                      10 + self.dungeon_level * 2,
                                      5 + self.dungeon_level,
                                      10 + self.dungeon_level * 3))
            elif enemy_type == "Fire Wraith":
                enemies.append(Enemy(f"Fire Wraith {i + 1}",
                                      60 + self.dungeon_level * 2,
                                      20 + self.dungeon_level * 3,
                                      2 + self.dungeon_level,
                                      20 + self.dungeon_level * 5))
            elif enemy_type == "Lava Beast":
                enemies.append(Enemy(f"Lava Beast {i + 1}",
                                      80 + self.dungeon_level * 3,
                                      25 + self.dungeon_level * 4,
                                      8 + self.dungeon_level,
                                      25 + self.dungeon_level * 6))
            elif enemy_type == "Ice Golem":
                enemies.append(Enemy(f"Ice Golem {i + 1}",
                                      80 + self.dungeon_level * 5,
                                      5 + self.dungeon_level * 2,
                                      10 + self.dungeon_level * 4,
                                      30 + self.dungeon_level * 6))
            elif enemy_type == "Frost Specter":
                enemies.append(Enemy(f"Frost Specter {i + 1}",
                                      50 + self.dungeon_level * 3,
                                      15 + self.dungeon_level * 2,
                                      5 + self.dungeon_level * 2,
                                      15 + self.dungeon_level * 4))
            elif enemy_type == "Ghost":
                enemies.append(Enemy(f"Ghost {i + 1}",
                                      40 + self.dungeon_level * 3,
                                      10 + self.dungeon_level * 2,
                                      3 + self.dungeon_level,
                                      12 + self.dungeon_level * 3))
            elif enemy_type == "Skeleton Warrior":
                enemies.append(Enemy(f"Skeleton Warrior {i + 1}",
                                      50 + self.dungeon_level * 4,
                                      15 + self.dungeon_level * 3,
                                      5 + self.dungeon_level * 3,
                                      15 + self.dungeon_level * 4))
            elif enemy_type == "Necromancer":
                enemies.append(Enemy(f"Necromancer {i + 1}",
                                      70 + self.dungeon_level * 5,
                                      20 + self.dungeon_level * 4,
                                      8 + self.dungeon_level,
                                      20 + self.dungeon_level * 6))
            elif enemy_type == "Sea Serpent":
                enemies.append(Enemy(f"Sea Serpent {i + 1}",
                                      90 + self.dungeon_level * 6,
                                      25 + self.dungeon_level * 5,
                                      10 + self.dungeon_level * 4,
                                      30 + self.dungeon_level * 7))
            elif enemy_type == "Kraken Tentacle":
                enemies.append(Enemy(f"Kraken Tentacle {i + 1}",
                                      100 + self.dungeon_level * 7,
                                      30 + self.dungeon_level * 6,
                                      12 + self.dungeon_level * 5,
                                      35 + self.dungeon_level * 8))
            elif enemy_type == "Abyssal Shadow":
                enemies.append(Enemy(f"Abyssal Shadow {i + 1}",
                                      120 + self.dungeon_level * 8,
                                      35 + self.dungeon_level * 7,
                                      15 + self.dungeon_level * 6,
                                      40 + self.dungeon_level * 9))
        return enemies

    def start_dungeon(self, player):
        print(f"{player.name} enters the {self.name} dungeon!")
        while player.is_alive() and len(self.enemies) > 0:
            enemy = self.enemies[0]
            print(f"A wild {enemy.name} appears!")
            player.damage_enemy(enemy)
            if enemy.is_alive():
                enemy.damage_player(player)
            else:
                print(f"{enemy.name} has been defeated! It drops {enemy.gold} gold.")
                player.gold += enemy.gold
                print(f"{player.name} now has {player.gold} gold.")
                self.enemies.pop(0)

            if player.is_alive() and len(self.enemies) > 0:
                print("Next turn...\n")

        if player.is_alive():
            print(f"{player.name} has cleared the dungeon!")
        else:
            print(f"{player.name} has been defeated in the dungeon.")    


def save_game(player):
    save_data = {
        "name": player.name,
        "health": player.health,
        "damage": player.damage,
        "defense": player.defense,
        "inventory": [{"name": item.name} for item in player.inventory],
        "equipped_weapon": player.equipped_weapon.name if player.equipped_weapon else None,
        "equipped_armor": player.equipped_armor.name if player.equipped_armor else None,
        "gold": player.gold,
    }

    if not os.path.exists('saves'):
        os.makedirs('saves')

    save_filename = f"saves/{player.name}_save.json"
    with open(save_filename, 'w') as save_file:
        json.dump(save_data, save_file)
    print(f"Game saved for {player.name}!")

def load_game():
    print("Load your saved game:")
    saved_files = [f for f in os.listdir('saves') if f.endswith('_save.json')]
    if not saved_files:
        print("No saved games found. Starting a new game...")
        return None

    while True:
        for idx, file in enumerate(saved_files):
            print(f"{idx + 1}. {file.replace('_save.json', '')}")

        try:
            choice = int(input("Choose a save to load: ")) - 1
            if choice < 0 or choice >= len(saved_files):
                print("Invalid input. Please choose a valid save number.")
                continue
            selected_file = saved_files[choice]
            break
        except ValueError:
            print("Invalid input. Please enter a number corresponding to a save file.")

    with open(f"saves/{selected_file}", 'r') as save_file:
        save_data = json.load(save_file)

    player = Warrior(save_data['name'])
    player.health = save_data['health']
    player.damage = save_data['damage']
    player.defense = save_data['defense']
    player.gold = save_data['gold']

    for item_data in save_data['inventory']:
        item_name = item_data['name']
        if item_name in ["Aspect of the Dragons", "Livid Dagger"]:
            player.inventory.append(Weapon(item_name, 10, 5, 1, 5, 500))
        elif item_name in ["Necron's Armor", "Shadow Assassin Armor"]:
            player.inventory.append(Armor(item_name, 20, 10, 5, 700))

    return player



def warrior1():
    print("Welcome to the Adventure Game!")
    print("Instructions: \n- Explore dungeons, fight enemies, and gain gold.")
    print("- Buy better items from merchants and equip them to get stronger.")
    print("- You can save and quit your progress at any time.")
    print("----Please do not break my game I already failed the final exam i spent a lot of time learning what this code after using Ai to make it so give me a 100:)")

    while True:
        choice = input("Do you want to (1) Start a new game or (2) Load a saved game? ")
        if choice == '1':
            player_name = input("Enter your character name: ")
            player = Warrior(player_name)
            break
        elif choice == '2':
            player = load_game()
            if not player:
                return
            break
        else:
            print("Invalid input. Please enter '1' to start a new game or '2' to load a saved game.")

    dungeon_level = 1
    while dungeon_level <= 1000:
        print(f"\n--- Dungeon {dungeon_level} ---")
        dungeon = Dungeon(f"Dungeon {dungeon_level}", dungeon_level)
        dungeon.start_dungeon(player)

        if not player.is_alive():
            print("Game Over! You have been defeated.")
            return  

        while True:
            print("\nOptions:")
            print("1. Save and quit")
            print("2. Continue to the merchant")
            print("3. Skip merchant and go to the next dungeon")
            print("4. View stats")
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
            else:
                print("Invalid input. Please choose a valid option.")

        dungeon_level += 1



if __name__ == "__main__":
    warrior1()
