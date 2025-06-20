from BankAccount import BankAccount

class SavingsAccount:
    #private members
    __account_number = None
    __routing_number = None

    def __init__(self, account_number, routing_number):
        self.__account_number = account_number
        self.__routing_number = routing_number