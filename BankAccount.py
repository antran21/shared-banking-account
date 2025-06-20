class BankAccount:
    bankTitle = "UNC Charlotte Bank"

    def __init__(self, customer_name, current_balance, minimum_balance):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance

    def deposit(self, amount):
        self.current_balance = self.current_balance + amount
        print("You have deposited " + str(amount))
        print("Your new current balance is " + str(self.current_balance))

    def withdraw(self, withdraw_amount):
        if self.current_balance - withdraw_amount >= self.minimum_balance:
            self.current_balance = self.current_balance - withdraw_amount
            print("You have withdrawn:", str(withdraw_amount))
            print("Your new current balance is:", str(self.current_balance))
        else:
            print("Your withdraw amount will exceed your set minimum balance: ", str(self.current_balance))


    def print_customer_information(self):
        print("Bank Title: " + self.bankTitle)
        print("Customer Name:", self.customer_name)
        print("Current Balance:", str(self.current_balance))
        print("Minimum Balance:", str(self.minimum_balance))


test1 = BankAccount("John Doe", 1000, 200)
test1.deposit(100)
test1.withdraw(1100)
test1.withdraw(500)
test1.print_customer_information()

test2 = BankAccount("Jane Doe", 100, 200)
test2.withdraw(20)
test2.deposit(400)
test2.withdraw(300)
test2.print_customer_information()
