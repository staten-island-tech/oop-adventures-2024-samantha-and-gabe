Date: 12/11/24 CODING ENEMY DAMAGE 
1. Asked chat gpt to editthis function so a enemy can do damage, my initial function was:  
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


Date: 12/11/24 CREATE HP VARIABLE 
1. 