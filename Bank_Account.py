class Bank_account:
    def __init__(self, account_number: int, name: str, balance=0):
        """Constructor that initialize the attributes of the object"""
        self.account_number = account_number
        self.name = name
        self.balance = balance
        self.transactions = []

    def __str__(self):
        """This method will return a string with all the object details that we want to see while print it"""
        return f"account number:{self.account_number} name: {self.name} balance: {self.balance}"

    def bank_statement(self):
        print(f"account number:{self.account_number} name: {self.name} balance: {self.balance}")

    def deposit(self, amount: int):
        self.balance += amount

    def withdraw(self, amount: int):
        if self.balance >= amount:
            self.balance -= amount


# create an object my account of type(class) Bank_Account
# my_account = Bank_account()
# my_account.account_number = int(input("Enter account number: "))
# my_account.name = input("Enter account owner name: ")
# my_account.balance = 400

account_number = int(input("Enter account number: "))
name = input("Enter account owner name: ")
my_account = Bank_account(account_number, name)

my_account.bank_statement()

amount = int(input("Enter the amount to withdraw: "))
my_account.withdraw(amount)

my_account.bank_statement()

amount = int(input("Enter the amount to deposit: "))
my_account.deposit(amount)
my_account.withdraw(350)

my_account.bank_statement()

print(my_account)