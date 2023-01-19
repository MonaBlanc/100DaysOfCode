#money_machine class
class MoneyMachine:

    CURRENCY = "€"

    COIN_VALUES = {
        "fifties": 0.5,
        "twenties": 0.2,
        "tens": 0.1,
    }

    def __init__(self):
        self.money_received = 0
        self.profit = 0

    def report(self):
        print(f"Money: {self.profit}{self.CURRENCY}")

    def process_coins(self):
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"how many {coin} pieces?: ")) * self.COIN_VALUES[coin]
        return self.money_received

        
    def make_payment(self, cost):
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {change}{self.CURRENCY} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False

