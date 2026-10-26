class Counter:
    def __init__(self, start=0):
        self.value = start

    def increment(self, step=1):
        self.value += step


a = Counter()
b = Counter(10)
a.increment()
a.increment(5)
b.increment()
print(a.value, b.value)

class BankAccount:
    def __init__(self, owner, balance=0):

        self.owner = owner
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance-=amount
        else:
            print("Nedostatek penez")
    def describe(self):
        print (f"{self.owner}: {self.balance} korun ceskych")
acc = BankAccount("Jana")
acc.deposit(1000)
acc.withdraw(300)
acc.withdraw(5000)       # Nedostatek prostředků
print(acc.describe())    # Jana: 700.00 Kč