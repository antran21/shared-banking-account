from CheckingAccount import CheckingAccount
from SavingsAccount import SavingsAccount

p1 = CheckingAccount("John Doe", 1000, 200, 0.5)
p1.deposit(100)
p1.withdraw(500)
p1.withdraw(1000)

p2 = CheckingAccount("Jane Doe", 9999, 100, 0.5)
p2.print_customer_information()

t1 = SavingsAccount("Bob Doe", 400, 300, 0.7)
t1.withdraw(200)
t1.deposit(500)
t1.withdraw(550)

t2 = SavingsAccount("Joe Doe", 1200, 200, 0.12)
t2.print_customer_information()