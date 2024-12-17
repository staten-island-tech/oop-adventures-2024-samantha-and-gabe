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


Date: 12/16/24 CREATE HP VARIABLE 
1. Asked chat gpt to create an HP variable for the user, input this code to define the variable "hp"
def take_damage(hp, enemy):
    hp -= enemy["damage"]
    hp = max(hp - damage, 0)
    print(f"Player takes {damage} damage. Remaining HP: {hp}")
    return hp


def choose_weapon():
    weapon_choice = input("Which weapon would you like to use?").strip()
    for i in inventory:
        if weapon_choice == i["name"]:
            if len(selected_weapon) > 0:

            else:
                selected_weapon.append(i)




def deal_damage(damage, enemy):
    enemy["hp"] -= damage
    print(enemy["hp"])
    return enemy["hp"]
2. Chat gpt returned 
def create_hp(base_hp=None, additional_hp=None, defense=None, additional_defense=None):
    return {
        "base_hp": base_hp,
        "additional_hp": additional_hp,
        "defense": defense,
        "additional_defense": additional_defense,
    }
3. which i then edited and added values to, to become this:
def create_hp(base_hp=None, additional_hp=None, defense=None, additional_defense=None):
    {
        "base_hp": 100,
        "additional_hp": 5,
        "damage": 10,
        "additional_damage": 5
    }
    create_hp(base_hp=None, additional_hp=None, defense=None, additional_defense=None)

hp = create_hp()  
custom_hp = create_hp(base_hp=200, additional_hp=50, defense=15, additional_defense=10) 
Overall i learned how to create an hp variable in which the user could create their own variable, 
or have the one specific to the game which is what the values represent  