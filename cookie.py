import time

class CookieClicker:
    def __init__(self):
        self.cookies = 0
        self.click_value = 1
        self.cookies_per_second = 0
        self.upgrades = {
            'Cursor': {'cost': 15, 'cps': 1},
            'Grandma': {'cost': 100, 'cps': 5},
            'Factory': {'cost': 500, 'cps': 20},
        }

    def click_cookie(self):
        """Simulate a cookie click, adding to the total cookies."""
        self.cookies += self.click_value
        print(f"Cookies: {self.cookies} (Clicked! +{self.click_value})")

    def buy_upgrade(self, upgrade_name):
        """Buy an upgrade to increase cookies per second."""
        if upgrade_name in self.upgrades:
            upgrade = self.upgrades[upgrade_name]
            if self.cookies >= upgrade['cost']:
                self.cookies -= upgrade['cost']
                self.cookies_per_second += upgrade['cps']
                print(f"Purchased {upgrade_name}! (+{upgrade['cps']} cookies/sec)")
            else:
                print(f"Not enough cookies to buy {upgrade_name}.")
        else:
            print(f"Upgrade {upgrade_name} doesn't exist.")

    def print_status(self):
        """Print the current game status."""
        print(f"\nCookies: {self.cookies}")
        print(f"Cookies per second: {self.cookies_per_second}")
        print("Upgrades available:")
        for name, upgrade in self.upgrades.items():
            print(f"- {name}: {upgrade['cost']} cookies")

    def auto_collect(self):
        """Automatically collect cookies every second."""
        while True:
            self.cookies += self.cookies_per_second
            print(f"\nCookies: {self.cookies} (+{self.cookies_per_second} cps)")
            time.sleep(1)

def game_loop():
    game = CookieClicker()
    print("Welcome to Cookie Clicker!")
    
    # Start a thread to simulate cookies per second (auto-collection)
    import threading
    threading.Thread(target=game.auto_collect, daemon=True).start()
    
    while True:
        game.print_status()
        print("\nOptions:")
        print("1. Click cookie (+1)")
        print("2. Buy Cursor (15 cookies, +1 cps)")
        print("3. Buy Grandma (100 cookies, +5 cps)")
        print("4. Buy Factory (500 cookies, +20 cps)")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            game.click_cookie()
        elif choice == "2":
            game.buy_upgrade('Cursor')
        elif choice == "3":
            game.buy_upgrade('Grandma')
        elif choice == "4":
            game.buy_upgrade('Factory')
        elif choice == "5":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    game_loop()