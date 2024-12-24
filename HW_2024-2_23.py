# Задание от 23.12.24
# 1. Создайте базовые классы Vehicle (транспортное средство) и Engine (двигатель).
# Класс Vehicle содержит информацию о максимальной скорости, а класс Engine — о мощности двигателя.
# Создайте класс Car, который наследуется от обоих классов. Реализуйте метод,
# который выводит информацию о максимальной скорости и мощности двигателя.

class Vehicle:
    def __init__(self, max_speed):
        self.max_speed = max_speed

    def get_max_speed(self):
        return self.max_speed


class Engine:
    def __init__(self, power):
        self.power = power

    def get_power(self):
        return self.power

class Car(Vehicle, Engine):
    def __init__(self, max_speed, power):
        Vehicle.__init__(self, max_speed)
        Engine.__init__(self, power)

    def display_info(self):
        print(f"Максимальная скорость автомобиля: {self.get_max_speed()} км/ч")
        print(f"Мощность двигателя: {self.get_power()} л.с.")

car = Car(max_speed=250, power=150)
car.display_info()

# 2. Создайте базовые классы BankAccount (банковский счёт) и InvestmentAccount (инвестиционный счёт).
# Класс BankAccount содержит информацию о балансе, а класс InvestmentAccount — о доходности.
# Создайте класс CombinedAccount, который наследуется от обоих классов. Реализуйте метод,
# который выводит информацию о балансе и доходности.


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def get_balance(self):
        return self.balance


class InvestmentAccount:
    def __init__(self, return_rate):
        self.return_rate = return_rate

    def get_return_rate(self):
        return self.return_rate


class CombinedAccount(BankAccount, InvestmentAccount):
    def __init__(self, balance, return_rate):
        BankAccount.__init__(self, balance)
        InvestmentAccount.__init__(self, return_rate)

    def display_info(self):
        print(f"Баланс на счёте: {self.get_balance()} руб.")
        print(f"Доходность инвестиционного счёта: {self.get_return_rate()}%")

account = CombinedAccount(balance=50000, return_rate=7)
account.display_info()

