class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, 200, 40, 20, "Warrior")
        self.abilities = ["Slash", "Shield Block"]

    def use_ability(self, enemy):
        print(f"{self.name} uses Slash!")
        damage = random.randint(30, 50)
        print(f"{self.name} deals {damage} damage with Slash.")
        enemy.take_damage(damage)


# Example Usage
def warrior1():
    # Create a player (Warrior)
    player = Warrior("Hero")

    # Create enemies for the dungeon
    enemies = [
        Enemy("Goblin", 50, 10, 5),
        Enemy("Skeleton", 60, 15, 8),
        Enemy("Troll", 100, 20, 10)
    ]

    # Create a dungeon
    dungeon = Dungeon("The Dark Cavern", enemies)

    # Start the dungeon
    dungeon.start_dungeon(player)

    if __name__ == "__main__":
        main()

if not enemy.is_alive():
    print(f"{enemy.name} has been defeated!")
else:
    print(f"{enemy.name} is still standing with {enemy.health} health.")

player = None

def classchoose():
    sigma = input("What dungeon class do you want to be?").strip()
    if sigma == "archer":
        player = Archer()
        print("You have chosen the Archer class")
    if sigma == "warrior":
        player = Warrior()
        print("You have chosen the Warrior class")
    if sigma == "mage":
        player = Mage()
        print("You have chosen the Mage class")
    if sigma == "healer":
        player = Healer()
        print("You have chosen the Healer class")




