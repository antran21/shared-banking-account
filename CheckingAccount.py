from BankAccount import BankAccount

class CheckingAccount(BankAccount):
    __account_number = None
    __routing_number = None

    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number):
        self.__account_number = account_number
        self.__routing_number = routing_number
        super().__init__(customer_name, current_balance, minimum_balance)