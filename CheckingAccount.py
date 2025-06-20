import BankingAccount

class CheckingAccount(BankingAccount):

    _accountNumber = None
    __routingNumber = None

    def __init__(self, customer_name, current_balance, minimum_balance, transfer_limit):
        super().__init__(customer_name, current_balance, minimum_balance)
        self.transfer = transfer_limit