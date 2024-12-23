# Задание от 13.11.24
# 1. Создайте программу, которая запрашивает у пользователя ввод числа от 1 до 100.
# Используйте вложенный оператор if, чтобы сначала проверить, находится ли число в указанном диапазоне.
# Если условие выполняется, определите, больше, меньше или равно введенное число 50,
# и выведите соответствующий результат на консоль.

class NumberChecker:
    def __init__(self, number):
        self.number = number

    def check_range(self):
        if 1 <= self.number <= 100:
            self.check_value()
        else:
            print("Число не входит в диапазон от 1 до 100.")

    def check_value(self):
        if self.number > 50:
            print("Число больше 50")
        elif self.number < 50:
            print("Число меньше 50")
        else:
            print("Число равно 50")

try:
    user_input = int(input("Введите число от 1 до 100: "))
    checker = NumberChecker(user_input)
    checker.check_range()
except ValueError:
    print("Ошибка: введено нечисловое значение.")

# 2. Создайте программу, в которой пользователь вводит два числа.
# Программа должна определить, больше ли первое число второго, меньше или равны они.
# Для выполнения этой проверки используйте тернарный оператор.

class NumberComparer:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def compare(self):
        result = "Первое число больше второго" if self.num1 > self.num2 else (
            "Первое число меньше второго" if self.num1 < self.num2 else "Числа равны")
        print(result)

try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    comparer = NumberComparer(num1, num2)
    comparer.compare()
except ValueError:
    print("Ошибка: пожалуйста, введите числа.")

# 3. Напишите программу, которая запрашивает у пользователя ввод возраста.
# Используйте условный оператор для определения,
# является ли пользователь совершеннолетним (18 лет и старше) или несовершеннолетним (младше 18 лет).
# Выведите соответствующее сообщение на консоль: "Вы совершеннолетний" или "Вы несовершеннолетний".

class AgeChecker:
    def __init__(self, age):
        self.age = age

    def check_age(self):
        if self.age >= 18:
            print("Вы совершеннолетний")
        else:
            print("Вы несовершеннолетний")

try:
    age = int(input("Введите ваш возраст: "))
    checker = AgeChecker(age)
    checker.check_age()

except ValueError:
    print("Ошибка: введено некорректное значение. Пожалуйста, введите числовое значение возраста.")