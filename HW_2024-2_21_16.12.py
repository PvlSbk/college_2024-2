# Задание от 16.12.24
# 1. Дан класс Integer, который представляет число:
#
# cpp
# Copy
# #include <iostream>
#
# class Integer
# {
# public:
#     Integer(int number)
#     {
#         value = number;
#     }
#     void print() const
#     {
#         std::cout << "Value: " << value << std::endl;
#     }
# private:
#     int value;
# };
# Добавьте в класс функцию, которая сравнивает текущий объект с другим объектом Integer,
# переданным в качестве аргумента. Функция должна возвращать:
#
# - положительное число, если текущий объект больше переданного,
#
# - отрицательное число, если текущий объект меньше переданного,
#
# - 0, если объекты равны.
#
# В функции main создайте несколько объектов класса Integer и проверьте их сравнение.

class Integer:
    def __init__(self, number):
        self.value = number

    def print(self):
        print(f"Value: {self.value}")

    def compare(self, other):
        if self.value > other.value:
            return 1
        elif self.value < other.value:
            return -1
        else:
            return 0

def main():
    num1 = Integer(10)
    num2 = Integer(20)
    num3 = Integer(10)

    result1 = num1.compare(num2)
    result2 = num1.compare(num3)

    if result1 > 0:
        print("num1 больше num2")
    elif result1 < 0:
        print("num1 меньше num2")
    else:
        print("num1 равно num2")

    if result2 > 0:
        print("num1 больше num3")
    elif result2 < 0:
        print("num1 меньше num3")
    else:
        print("num1 равно num3")

if __name__ == "__main__":
    main()

# 2. Создайте два класса: Rectangle и Circle. Реализуйте дружественную функцию, которая принимает объекты обоих классов и возвращает true, если площадь прямоугольника больше площади круга, и false в противном случае.
# Требования:
# Класс Rectangle должен иметь поля width и height.
# Класс Circle должен иметь поле radius.
# Реализуйте методы для вычисления площади для каждого класса.
# Используйте дружественную функцию для сравнения площадей.

import math


class Rectangle:
    def init(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle:
    def init(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


def compare_area(rectangle, circle):
    return rectangle.area() > circle.area()


def main():
    rectangle = Rectangle(10, 5)
    circle = Circle(3)

    if compare_area(rectangle, circle):
        print("Площадь прямоугольника больше площади круга.")
    else:
        print("Площадь круга больше или равна площади прямоугольника.")


if __name__ == "__main__":
    main()

# 3. Создайте класс Person, который содержит поля name и age.
# Реализуйте метод compareAge, который принимает другой объект Person и возвращает true,
# если возраст текущего объекта больше, чем возраст переданного объекта, и false в противном случае.
# Используйте ключевое слово this для обращения к текущему объекту.
# Требования:
# Метод compareAge должен использовать ключевое слово this.
# В функции main создайте два объекта класса Person и сравните их возраст.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def compareAge(self, other):
        if self.age > other.age:
            return True
        else:
            return False

def main():
    person1 = Person("Alice", 30)
    person2 = Person("Bob", 25)

    if person1.compareAge(person2):
        print(f"{person1.name} старше {person2.name}.")
    else:
        print(f"{person1.name} не старше {person2.name}.")

if __name__ == "__main__":
    main()