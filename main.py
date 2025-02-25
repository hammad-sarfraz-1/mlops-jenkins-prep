class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited {amount}. New balance: {self.balance}"
        return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew {amount}. New balance: {self.balance}"
        return "Invalid withdrawal amount or insufficient funds."

    def get_balance(self):
        return f"Current balance: {self.balance}"

if __name__ == "__main__":
    account = BankAccount("John Doe", 1000)
    print(account.deposit(500))
    print(account.withdraw(300))
    print(account.get_balance())
