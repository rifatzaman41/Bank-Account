import random

class User:
    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.account_number = random.randint(10000, 99999)
        self.transaction_history = []
        self.loan_taken = 0
        self.max_loan_count = 2

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f'Deposit: {amount}')

    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal amount exceeded")
        else:
            self.balance -= amount
            self.transaction_history.append(f'Withdraw: {amount}')

    def check_balance(self):
        return self.balance

    def check_transaction_history(self):
        return self.transaction_history

    def take_loan(self, amount):
        if self.loan_taken < self.max_loan_count:
            self.balance += amount
            self.loan_taken += 1
            self.transaction_history.append(f'Loan Taken: {amount}')
        else:
            print("Maximum loan limit reached")

    def transfer(self, amount, recipient):
        if amount > self.balance:
            print("Insufficient funds for transfer")
        elif recipient is None:
            print("Recipient account does not exist")
        else:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append(f'Transfer to {recipient.name}: {amount}')

class Admin:
    def __init__(self):
        self.users = []

    def create_account(self, name, email, address, account_type):
        user = User(name, email, address, account_type)
        self.users.append(user)
        return user

    def delete_account(self, user):
        self.users.remove(user)

    def get_all_accounts(self):
        return self.users

    def total_balance(self):
        return sum(user.balance for user in self.users)

    def total_loan_amount(self):
        return sum(user.loan_taken for user in self.users)

    

admin = Admin()


user1 = admin.create_account("John Doe", "john@example.com", "123 Main St", "Savings")
user2 = admin.create_account("Jane Smith", "jane@example.com", "456 Elm St", "Current")


user1.deposit(1000)
user1.withdraw(500)


user2.deposit(500)
user1.transfer(300, user2)


print(user1.check_balance())
print(user1.check_transaction_history())


user1.take_loan(2000)

print(admin.total_balance())
print(admin.total_loan_amount())
