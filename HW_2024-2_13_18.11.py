# Задание от 18.11.24
# 1. Создайте программу, которая использует цикл для суммирования всех четных чисел в диапазоне
# от 1 до заданного пользователем числа. Программа должна выводить сумму четных чисел,
# а также количество четных чисел, которые были добавлены.

class EvenNumberSummation:
    def __init__(self, limit):
        self.limit = limit
        self.sum = 0
        self.count = 0

    def calculate_even_sum(self):
        for num in range(1, self.limit + 1):
            if num % 2 == 0:
                self.sum += num
                self.count += 1

    def display_results(self):
        print(f"Сумма четных чисел: {self.sum}")
        print(f"Количество четных чисел: {self.count}")


limit = int(input("Введите число: "))

even_sum = EvenNumberSummation(limit)
even_sum.calculate_even_sum()
even_sum.display_results()

# 2. Напишите программу, которая запрашивает у пользователя целое положительное число
# и выводит обратный счет от этого числа до 1.
# Программа должна использовать цикл и выводить каждое число на новой строке.

class Countdown:
    def __init__(self, number):
        self.number = number

    def start(self):
        if self.number > 0:
            for i in range(self.number, 0, -1):
                print(i)
        else:
            print("Пожалуйста, введите положительное число.")

user_input = int(input("Введите целое положительное число: "))

countdown = Countdown(user_input)
countdown.start()

# 3. Напишите программу, которая запрашивает у пользователя целое неотрицательное число
# и вычисляет его факториал с помощью цикла. Программа должна выводить результат, а также количество итераций,
# выполненных в цикле.

class FactorialCalculator:
    def __init__(self, number):
        self.number = number

    def calculate_factorial(self):
        if self.number < 0:
            print("Факториал можно вычислить только для неотрицательных чисел.")
            return

        factorial = 1
        iterations = 0

        for i in range(1, self.number + 1):
            factorial *= i
            iterations += 1

        print(f"Факториал числа {self.number} равен {factorial}.")
        print(f"Количество итераций: {iterations}")


user_input = int(input("Введите целое неотрицательное число: "))

calculator = FactorialCalculator(user_input)
calculator.calculate_factorial()