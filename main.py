from SavingsAccount import SavingsAccount
from CheckingAccount import CheckingAccount

Savings1 = SavingsAccount("Angel", 100, 20, "1234", "019474")
print(Savings1)
Savings1.withdraw(50)
print(Savings1)
Savings2 = SavingsAccount("Markiplier", 120, 10, "4321", "10842")
print(Savings2)
Savings2.deposit(100)
print(Savings2)

Checking1 = CheckingAccount("Angel", 200, 40, "5678", "91836")
print(Checking1)
Checking1.withdraw(150)
print(Checking1)
Checking2 = CheckingAccount("Markiplier", 300, 20, "0987", "014877")
print(Checking2)
Checking2.deposit(500)
print(Checking2)