hp = 100
damage = 1


class Enemy():
    def __init__(self, hp, defense, damage):
        self.hp = hp
        self.defense = defense
        self.damage = damage
        



selected_weapon = []

evil_spirit = Enemy(100, 0, 5).__dict__



inventory = []

sword = {
    "name": "Starter Sword",
    "damage": 10,
    "strength": 5,
    "ecc": 1, 
    "critdmg": 5
    }

bow = {
    "name": "Starter Sword",
    "damage": 10,
    "strength": 5,
    "ecc": 1, 
    "critdmg": 5
    }

def f(x):
    return x**2

def add_to_inventory(item):
    inventory.append(item)

add_to_inventory(sword)
add_to_inventory(bow)


# function should be reusable for any enemy

def take_damage(base_hp, enemy):
    hp -= enemy["damage"]
    hp = max(base_hp - damage, 0)
    print(f"Player takes {damage} damage. Remaining HP: {base_hp}")
    return hp


def choose_weapon():
    weapon_choice = input("Which weapon would you like to use?").strip()
    for i in inventory:
        if weapon_choice == i["name"]:
            if len(selected_weapon) > 0:

            else:
                selected_weapon.append(i)




def deal_damage(damage, enemy):
    enemy["base_hp"] -= damage
    print(enemy["base_hp"])
    return enemy["base_hp"]


    



