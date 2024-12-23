# Задание от 16.10.2024
# 1. Создайте класс Class, который имеет атрибут класса total_students, отслеживающий общее количество студентов,
# и метод add_student, который увеличивает значение total_students на 1.
# Добавьте статический метод get_total_students, который возвращает текущее значение total_students.

class Class:
    total_students = 0
    def add_student(self):
        # Увеличиваем количество студентов на 1
        Class.total_students += 1
    @staticmethod
    def get_total_students():
        return Class.total_students
# Пример
student1 = Class()
student2 = Class()
student3 = Class()
student1.add_student()
student2.add_student()
student3.add_student()
print("Total students:", Class.get_total_students())
student4 = Class()
student4.add_student()
print("Total students:", Class.get_total_students())

# 2. Создайте класс Bank, который имеет атрибут класса total_balance, представляющий общий баланс банка.
# Реализуйте метод deposit, который увеличивает total_balance на заданную сумму,
# и статический метод get_total_balance, возвращающий текущий баланс.
# Пример использования: сначала выполните несколько депозитов, а затем получите общий баланс.

class Bank:
    total_balance = 0
    def deposit(self, amount):
        if amount > 0:
            Bank.total_balance += amount
        else:
            print("Сумма депозита должна быть положительной!")
    @staticmethod
    def get_total_balance():
        return Bank.total_balance
# Пример
bank1 = Bank()
bank2 = Bank()
bank1.deposit(1000)
bank2.deposit(500)
print("Общий баланс банка:", Bank.get_total_balance())
bank1.deposit(200)
print("Общий баланс банка:", Bank.get_total_balance())

# 3. Создайте базовый класс Vehicle с методом describe(), который выводит "Это транспортное средство".
# Затем создайте дочерние классы Car и Bike, которые переопределяют метод describe(),
# чтобы выводить специфическую информацию о каждом виде транспорта:
# "Это машина" и "Это велосипед" соответственно. Проверьте вывод для объектов обоих классов.

class Vehicle:
    def describe(self):
        print("Это транспортное средство")
class Car(Vehicle):
    def describe(self):
        print("Это машина")
class Bike(Vehicle):
    def describe(self):
        print("Это велосипед")
# Пример
vehicle = Vehicle()
car = Car()
bike = Bike()
vehicle.describe()
car.describe()
bike.describe()