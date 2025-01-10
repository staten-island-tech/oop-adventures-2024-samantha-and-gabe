import random


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
        """Sanitize and format user input to match item keys."""
        return user_input.strip().title()

    def display_items(self):
        """Display the list of items the merchant sells."""
        print("Items for sale:")
        for item, price in self.items_for_sale.items():
            print(f"- {item}: {price} coins")
        print(f"Pure Columbian Cocaine: {self.coke_price} coins (with a 5% chance)")


    def attempt_to_sell_coke(self):
        """Check if the merchant is selling chips with a 5% chance."""
        return random.random() < self.coke_probability


    def sell_item(self, player_coins):
        """Simulate the process of buying an item from the merchant."""
        print("\nChoose an item to buy:")
        self.display_items()


        # Ask the player to choose an item
        item_choice = input("Enter the item you want to buy (Weapon, Potion, Armor): ").capitalize()
       
        if item_choice in self.items_for_sale:
            item_price = self.items_for_sale[item_choice]
            if player_coins >= item_price:
                player_coins -= item_price
                print(f"You have successfully bought a {item_choice} for {item_price} coins.")
            else:
                print("You don't have enough coins to buy that item.")
        else:
            print("Invalid choice. Please choose a valid item.")


        if self.attempt_to_sell_coke():
            if player_coins >= self.coke_price:
                player_coins -= self.coke_price
                print("The merchant offers you a Bag of Chips for 50 coins. You bought it!")
            else:
                print("You don't have enough coins to buy the Bag of Chips.")


        return player_coins




# Example usage
player_coins = 200  # Starting amount of coins


merchant = Merchant()
player_coins = merchant.sell_item(player_coins)
print(f"Remaining coins: {player_coins}")

class Merchant_1:
    def __init__(self):
        self.items_for_sale = {
            'Frozen Scythe': 100,  # Set price for a weapon
            'Golem Sword': 50,   # Set price for a potion
            'Raider Axe': 75,
            'Firedust Dagger': 100,   # Set price for a potion
            'Twilight dagger': 115,   #
            'Revenant Fachion': 150,  # type: ignore
            'Aspect of the End': 100,   # Set price for a potion
            'Recluse Fang': 200, 
            'Voidedge Katana':  150,   # Set price for a potion
            'Tacticians Sword': 200, 
            'Blade of the Volcano': 230,   # Set price for a potion
            'Ragnarock axe': 150,
            'Arack': 100,   # Set price for a potion
            'Scorpion foil': 150, 
            'Flower of truth': 200    # Set price for armor
        }
        self.coke_price = 50  # Price of chips
        self.coke_probability = 0.05  # 5% chance to sell chips

    def sanitize_input(self, user_input):
        """Sanitize and format user input to match item keys."""
        return user_input.strip().title()

    def display_items(self):
        """Display the list of items the merchant sells."""
        print("Items for sale:")
        for item, price in self.items_for_sale.items():
            print(f"- {item}: {price} coins")
        print(f"Pure Columbian Cocaine: {self.coke_price} coins (with a 5% chance)")


    def attempt_to_sell_coke(self):
        """Check if the merchant is selling chips with a 5% chance."""
        return random.random() < self.coke_probability


    def sell_item(self, player_coins):
        """Simulate the process of buying an item from the merchant."""
        print("\nChoose an item to buy:")
        self.display_items()


        # Ask the player to choose an item
        item_choice = input("Enter the item you want to buy (Weapon, Potion, Armor): ").capitalize()
       
        if item_choice in self.items_for_sale:
            item_price = self.items_for_sale[item_choice]
            if player_coins >= item_price:
                player_coins -= item_price
                print(f"You have successfully bought a {item_choice} for {item_price} coins.")
            else:
                print("You don't have enough coins to buy that item.")
        else:
            print("Invalid choice. Please choose a valid item.")


        if self.attempt_to_sell_coke():
            if player_coins >= self.coke_price:
                player_coins -= self.coke_price
                print("The merchant offers you a Bag of Chips for 50 coins. You bought it!")
            else:
                print("You don't have enough coins to buy the Bag of Chips.")


        return player_coins

Merchant1 = Merchant_1()
player_coins = Merchant1.sell_item(player_coins)
print(f"Remaining coins: {player_coins}")

class Merchant_2:
    def __init__(self):
        self.items_for_sale = {
            'Withercloak Sword': 100,  # Set price for a weapon
            'Dark Claymore': 150,   # Set price for a potion
            'Rosettas Armor': 75,
            'Biohazard Armor': 100,   # Set price for a potion
            'Miner Armor': 115,   #
            'Fairy Armor': 50,  # type: ignore
            'Armor of Growth': 100,   # Set price for a potion
            'Perfect Armor': 250, 
            'Shimmering Light Armor':  150,   # Set price for a potion
            'Blaze Armor': 150, 
            'Monster Hunter Armor': 230,   # Set price for a potion
            'Monster Raider Armor': 150 
        }
        self.coke_price = 50  # Price of chips
        self.coke_probability = 0.05  # 5% chance to sell chips

    def sanitize_input(self, user_input):
        """Sanitize and format user input to match item keys."""
        return user_input.strip().title()

    def display_items(self):
        """Display the list of items the merchant sells."""
        print("Items for sale:")
        for item, price in self.items_for_sale.items():
            print(f"- {item}: {price} coins")
        print(f"Pure Columbian Cocaine: {self.coke_price} coins (with a 5% chance)")


    def attempt_to_sell_coke(self):
        """Check if the merchant is selling chips with a 5% chance."""
        return random.random() < self.coke_probability


    def sell_item(self, player_coins):
        """Simulate the process of buying an item from the merchant."""
        print("\nChoose an item to buy:")
        self.display_items()


        # Ask the player to choose an item
        item_choice = input("Enter the item you want to buy (Weapon, Potion, Armor): ").capitalize()
       
        if item_choice in self.items_for_sale:
            item_price = self.items_for_sale[item_choice]
            if player_coins >= item_price:
                player_coins -= item_price
                print(f"You have successfully bought a {item_choice} for {item_price} coins.")
            else:
                print("You don't have enough coins to buy that item.")
        else:
            print("Invalid choice. Please choose a valid item.")


        if self.attempt_to_sell_coke():
            if player_coins >= self.coke_price:
                player_coins -= self.coke_price
                print("The merchant offers you a Bag of Chips for 50 coins. You bought it!")
            else:
                print("You don't have enough coins to buy the Bag of Chips.")


        return player_coins

Merchant2 = Merchant_2()
player_coins = Merchant2.sell_item(player_coins)
print(f"Remaining coins: {player_coins}")

def sanitize_input(self, user_input):
    """Sanitize and format user input to match item keys."""
    return user_input.strip().title()

