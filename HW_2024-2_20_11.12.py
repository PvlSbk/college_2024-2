# Задание от 11.12.24
# 1. Создайте класс `Car`, который содержит приватные переменные для марки автомобиля (`brand`),
# года выпуска (`year`) и скорости (`speed`). Реализуйте конструктор, который инициализирует эти переменные.
# Добавьте методы для увеличения и уменьшения скорости, а также метод для вывода информации об автомобиле.
# В функции `main` создайте объект класса `Car` и продемонстрируйте работу всех методов.

class Car:
    def __init__(self, brand, year, speed=0):
        self.__brand = brand
        self.__year = year
        self.__speed = speed

    def accelerate(self, increment):
        if increment > 0:
            self.__speed += increment
            print(f"Скорость увеличена на {increment} км/ч. Текущая скорость: {self.__speed} км/ч.")
        else:
            print("Увеличение скорости должно быть положительным числом.")

    def decelerate(self, decrement):
        if decrement > 0:
            if self.__speed - decrement >= 0:
                self.__speed -= decrement
                print(f"Скорость уменьшена на {decrement} км/ч. Текущая скорость: {self.__speed} км/ч.")
            else:
                print("Невозможно уменьшить скорость, так как она не может быть меньше 0.")
        else:
            print("Уменьшение скорости должно быть положительным числом.")

    def display_info(self):
        print(f"Марка автомобиля: {self.__brand}")
        print(f"Год выпуска: {self.__year}")
        print(f"Текущая скорость: {self.__speed} км/ч")

def main():
    car1 = Car("Toyota", 2020)
    car1.display_info()
    car1.accelerate(50)
    car1.decelerate(20)
    car1.decelerate(40)
    car1.display_info()

if __name__ == "__main__":
    main()

# 2. Создайте класс `Rectangle`, который содержит приватные переменные для длины (`length`) и ширины (`width`).
# Реализуйте конструктор, который принимает значения длины и ширины.
# Добавьте методы для вычисления площади и периметра прямоугольника.
# В функции `main` создайте объект класса `Rectangle` и выведите площадь и периметр.

class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return 2 * (self.__length + self.__width)

def main():
    length = float(input("Введите длину прямоугольника: "))
    width = float(input("Введите ширину прямоугольника: "))

    rectangle = Rectangle(length, width)

    print(f"Площадь прямоугольника: {rectangle.area()} единиц²")
    print(f"Периметр прямоугольника: {rectangle.perimeter()} единиц")


if __name__ == "__main__":
    main()

# 3. Создайте класс `Student`, который содержит приватные переменные для имени (`name`),
# возраста (`age`) и среднего балла (`averageGrade`). Реализуйте конструктор, который инициализирует эти переменные.
# Добавьте методы для установки и получения значений переменных, а также метод для вывода информации о студенте.
# В функции `main` создайте объект класса `Student` и продемонстрируйте работу всех методов.

class Student:
    def __init__(self, name, age, averageGrade):
        self.__name = name
        self.__age = age
        self.__averageGrade = averageGrade

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_averageGrade(self, averageGrade):
        self.__averageGrade = averageGrade

    def get_averageGrade(self):
        return self.__averageGrade

    def display_info(self):
        print(f"Имя студента: {self.__name}")
        print(f"Возраст студента: {self.__age}")
        print(f"Средний балл студента: {self.__averageGrade:.2f}")

def main():
    name = input("Введите имя студента: ")
    age = int(input("Введите возраст студента: "))
    averageGrade = float(input("Введите средний балл студента: "))

    student = Student(name, age, averageGrade)

    student.display_info()

    new_name = input("Введите новое имя студента: ")
    student.set_name(new_name)

    new_age = int(input("Введите новый возраст студента: "))
    student.set_age(new_age)

    new_averageGrade = float(input("Введите новый средний балл студента: "))
    student.set_averageGrade(new_averageGrade)

    student.display_info()


if __name__ == "__main__":
    main()

# 4. Создайте класс `BankAccount`, который содержит приватные переменные для номера счета (`accountNumber`)
# и баланса (`balance`). Реализуйте конструктор, который инициализирует эти переменные.
# Добавьте методы для пополнения и снятия денег со счета, а также метод для вывода текущего баланса.
# В функции `main` создайте объект класса `BankAccount` и продемонстрируйте работу всех методов.

class BankAccount:
    def __init__(self, accountNumber, initialBalance=0):
        self.__accountNumber = accountNumber
        self.__balance = initialBalance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Пополнено на {amount} единиц. Текущий баланс: {self.__balance} единиц.")
        else:
            print("Сумма пополнения должна быть положительной.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"Снято {amount} единиц. Текущий баланс: {self.__balance} единиц.")
            else:
                print("Недостаточно средств на счете.")
        else:
            print("Сумма снятия должна быть положительной.")

    def get_balance(self):
        return self.__balance

    def display_account_info(self):
        print(f"Номер счета: {self.__accountNumber}")
        print(f"Текущий баланс: {self.__balance} единиц.")


def main():
    accountNumber = input("Введите номер счета: ")
    initialBalance = float(input("Введите начальный баланс: "))

    account = BankAccount(accountNumber, initialBalance)

    account.display_account_info()

    depositAmount = float(input("Введите сумму для пополнения: "))
    account.deposit(depositAmount)

    withdrawAmount = float(input("Введите сумму для снятия: "))
    account.withdraw(withdrawAmount)

    print(f"Текущий баланс на счете: {account.get_balance()} единиц.")

if __name__ == "__main__":
    main()

# 5. Создайте класс `Circle`, который содержит приватную переменную для радиуса (`radius`).
# Реализуйте конструктор, который принимает значение радиуса. Добавьте методы для вычисления площади и длины окружности.
# В функции `main` создайте объект класса `Circle` и выведите площадь и длину окружности.

import math


class Circle:
    def __init__(self, radius):
        # Инициализация приватной переменной для радиуса
        self.__radius = radius

    # Метод для вычисления площади круга
    def area(self):
        return math.pi * (self.__radius ** 2)

    # Метод для вычисления длины окружности
    def circumference(self):
        return 2 * math.pi * self.__radius

    # Метод для вывода информации о круге
    def display_info(self):
        print(f"Радиус круга: {self.__radius}")
        print(f"Площадь круга: {self.area():.2f}")
        print(f"Длина окружности: {self.circumference():.2f}")


# Функция main для демонстрации работы класса
def main():
    # Ввод данных для радиуса
    radius = float(input("Введите радиус круга: "))

    # Создаем объект круга
    circle = Circle(radius)

    # Выводим информацию о круге
    circle.display_info()


# Запуск функции main
if __name__ == "__main__":
    main()