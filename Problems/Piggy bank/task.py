class PiggyBank:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents
        self.new_cents = None
        self.new_dollars = None

    def add_money(self, deposit_dollars, deposit_cents):
        self.dollars = self.dollars + deposit_dollars
        self.cents = self.cents + deposit_cents

        if self.cents >= 100:
            add_dollars = int(self.cents / 100)
            self.cents = self.cents % 100
            self.dollars += add_dollars
