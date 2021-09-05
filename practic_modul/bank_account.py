# Voronov Andrei
# Создайте класс BankAccount, который представляет банковский счет, c атрибутами экземпляра: 
# accountNumber (числовой тип), name (имя владельца счета строкового типа), balance.
class BankAccount:
    account_number = int
    name = str
    balance = float
# Создайте конструктор с параметрами: accountNumber, name, balance.
    def __init__(self, account_number, name, balance) -> None:
        self.account_number = account_number
        self.name = name
        self.balance = balance
# Создайте метод Deposit(), который управляет действиями по пополнению счета.
    def deposit(self, add_money):
        self.balance += add_money
# Создайте метод Withdrawal(), который управляет действиями по снятию средств.
    def withdrawal(self, take_money):
        self.balance -= take_money
# Создайте метод bankFees() для применения банковской комиссии в размере 5% от баланса счета.
    def bank_fees(self):
        self.balance -= (self.balance * 0.05)
# Создайте метод display() для отображения деталей счета.
    def display(self):
        print(f'''Намер счета: {self.account_number}
Имя владельца счета: {self.name}
Баланс: {self.balance} ''')
# Приведите примеры использования.
client_1 = BankAccount(130899301, 'Andrei', 15439.4)
client_2 = BankAccount(120899302, 'Anton', 20000)
client_1.deposit(50000)
client_1.display()
client_1.withdrawal(10000)
client_1.display()
client_1.bank_fees()
client_1.display()
client_2.deposit(150000)
client_2.display()
client_2.withdrawal(31000)
client_2.display()
client_2.bank_fees()
client_2.display()