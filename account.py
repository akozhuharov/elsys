import random
import string


class Account:
    def __init__(self, name, balance):
        characters = string.ascii_letters + string.digits
        print(characters)
        self.name = name
        self.account_id = ""
        for i in range(10):
            self.account_id += str(random.choice(characters))
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount

    def print_all(self):
        # 1 Nachin 
        print("Name: {}, Account: {}, Balance: {}".format(self.name, self.account_id, self.balance))
        # 2 nachin
        print(f"Name: {self.name}, Account: {self.account_id}, Balance: {self.balance}")

acc = Account("Nasko", 150)
print(acc.balance)
acc.deposit(200)
acc.print_all()