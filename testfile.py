class Enemy:
    def __init__(self, hp, defense, damage):
        self.hp = hp
        self.defense = defense
        self.damage = damage

# Define an enemy
evil_spirit = Enemy(100, 0, 5)

# Using __dict__ directly
print(evil_spirit.__dict__)  # Output: {'hp': 100, 'defense': 0, 'damage': 5}

