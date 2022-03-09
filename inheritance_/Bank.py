
class Bank:
    cash = 10000

    def __init__(self, name, branch):
        self.name = name
        self.branch = branch

    @classmethod
    def borrow(cls, bank):
        amount = int(input("Enter amount : "))
        bank.add_cash(amount)
        cls.cash -= amount


class Kbz(Bank):
    def __init__(self, name, branch):
        super().__init__(name, branch)
        self.cash = 0

    def set_cash(self, cash):
        self.cash += cash

    def add_cash(self, cash):
        self.cash += cash

    def __str__(self):
        return f"Available cash : {self.cash}"


kbz = Kbz("KBZ", 34)
kbz.set_cash(6000)
Bank.borrow(kbz)
print(kbz)
print(Bank.cash)