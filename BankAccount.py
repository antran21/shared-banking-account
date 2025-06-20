class BankAccount:
    bank_name = "Angel's Bank"
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
        self.account_number = account_number
        self.routing_number = routing_number

    def deposit(self, amount):
        self.current_balance = self.current_balance + amount

    def withdraw(self, amount):
        if (self.current_balance - amount) < self.minimum_balance:
            print("Cannot Withdraw!")
        else:
            self.current_balance = self.current_balance - amount

    def __str__(self):
        return(f"Bank: {BankAccount.bank_name}\n"
            f"Customer Name: {self.customer_name}\n"
            f"Current Balance: ${self.current_balance}\n"
            f"Minimum Balance: ${self.minimum_balance}")