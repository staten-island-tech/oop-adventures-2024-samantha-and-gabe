Date: 12/11/24 CODING ENEMY DAMAGE 
1. Asked chat gpt to edit this function so a enemy can do damage, my initial function was:  
    def take_damage(hp, enemy):
        hp -= enemy["damage"]
        print(hp)
        return hp
2. Chatgpt had returned
def take_damage(hp, enemy):
    """
    Reduces the player's health points (hp) based on the damage inflicted by an enemy.

    Args:
        hp (int): The current health points of the player.
        enemy (dict): A dictionary containing enemy attributes, including "damage".

    Returns:
        int: The updated health points after taking damage.
    """
    if not isinstance(enemy, dict) or "damage" not in enemy:
        raise ValueError("Enemy must be a dictionary containing a 'damage' key.")

    damage = enemy["damage"]

    if not isinstance(damage, (int, float)) or damage < 0:
        raise ValueError("Damage must be a non-negative number.")

    hp = max(hp - damage, 0)  # Ensure HP doesn't drop below 0
    print(f"Player takes {damage} damage. Remaining HP: {hp}")
    return hp
3. My function has already had the proper components other than health dropping below zero so i incorporated
     hp = max(hp - damage, 0)  # Ensure HP doesn't drop below 0
    print(f"Player takes {damage} damage. Remaining HP: {hp}")
    return hp
and created a final function of 
def take_damage(hp, enemy):
    hp -= enemy["damage"]
    hp = max(hp - damage, 0)
    print(f"Player takes {damage} damage. Remaining HP: {hp}")
    return hp
We learned how to reduce hp to a certain point, however, not reach below zero 

Date: 1/12/25 CODING MERCHANT FILE 
1. I pasted items from the items json to create a merchant class and asked chat gpt how to make it better and more efficient 
[
    {
        "name": "Starter Sword",
        "damage": 10,
        "strength": 5,
        "ecc": 1,
        "critdmg": 5,
        "type": "weapon"
    },
    {
        "name": "Metal Sword",
        "damage": 15,
        "strength": 10,
        "ecc": 5,
        "critdmg": 5,
        "type": "weapon"
    },
    {
        "name": "Aspect of the Jerry",
        "damage": 1,
        "strength": 0,
        "ecc": 0,
        "critdmg": 0,
        "type": "weapon"
    },
    {
        "name": "Fancy Sword",
        "damage": 20,
        "strength": 0,
        "ecc": 0,
        "critdmg": 0,
        "type": "weapon"
    },
    {
        "name": "Rogue Sword",
        "damage": 20,
        "strength": 0,
        "ecc": 0,
        "critdmg": 0,
        "type": "weapon"
    },

2. chat gpt returned this 
class Merchant:
    def __init__(self):
        self.items_for_sale = {
            'Starter Sword': 10,  # Set price for a weapon
            'Metal Sword': 50,   # Set price for a potion
            'Fancy Sword': 150,
            'Rogue Sword': 50,   # Set price for a potion
            'Spider Sword': 150,   #
            'Undead Sword': 100,  # type: ignore
            'End Sword': 50,   # Set price for a potion
            'Flaming Sword': 200, 
            'Hunter Knife':  100,   # Set price for a potion
            'Prismarine Blade': 150, 
            'Voildwalker Katana ': 230,   # Set price for a potion
            'Silver fang': 150, 
            'Sword of Bad Health': 200,   # Set price for a potion
            'Tribal Spear': 150, 
            'Mercanary axe': 150 }
        self.coke_price = 50  # Price of chips
        self.coke_probability = 0.05  # 5% chance to sell chips

    def sanitize_input(self, user_input):
        return user_input.strip().title()

3. I then changed the values and input new items. I learned how to take a user input and use it despite no capitalization
this was done throught the strip().title()

i then input it into the main file as different dictionaries 

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
