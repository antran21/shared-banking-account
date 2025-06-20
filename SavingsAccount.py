from BankAccount import BankAccount

class SavingsAccount:
    #private members
    __account_number = None
    __routing_number = None

    def __init__(self, account_number, routing_number):
        this.__account_number = account_number
        this.__routing_number = routing_number