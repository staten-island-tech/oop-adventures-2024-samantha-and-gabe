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
