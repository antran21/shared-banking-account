from BankAccount import BankAccount

class SavingsAccount(BankAccount):

    _accountNumber = None
    __routingNumber = None

    def __init__(self, customer_name, current_balance, minimum_balance, interest_num):
        super().__init__(customer_name, current_balance, minimum_balance)
        self.interest = interest_num