# Задание от 04.12.24
# 1. Напишите функцию gcd(), которая принимает два целых числа a и b и возвращает их наибольший общий делитель.
# 2. Напишите функцию sumArray(), которая принимает массив целых чисел и его размер,
# и возвращает сумму всех элементов массива.
# 3. Напишите функцию findMax(), которая принимает массив целых чисел и его размер,
# и возвращает максимальный элемент в массиве.
# 4. Напишите функцию sortArray(), которая принимает массив целых чисел и его размер,
# и сортирует массив по возрастанию. Функция не должна возвращать значение, а должна изменять переданный массив.

class ArrayOperations:

    @staticmethod
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    @staticmethod
    def sumArray(arr):
        return sum(arr)

    @staticmethod
    def findMax(arr):
        if len(arr) == 0:
            return None  # Если массив пустой, возвращаем None
        return max(arr)

    @staticmethod
    def sortArray(arr):
        arr.sort()  # Сортируем массив по возрастанию


# Пример использования функций

# Ввод данных
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

# Находим НОД
gcd_result = ArrayOperations.gcd(a, b)
print(f"Наибольший общий делитель чисел {a} и {b}: {gcd_result}")

# Массив для других операций
arr = list(map(int, input("Введите числа массива через пробел: ").split()))

# Сумма элементов массива
sum_result = ArrayOperations.sumArray(arr)
print(f"Сумма элементов массива: {sum_result}")

# Максимальный элемент в массиве
max_result = ArrayOperations.findMax(arr)
print(f"Максимальный элемент в массиве: {max_result}")

# Сортировка массива
ArrayOperations.sortArray(arr)
print(f"Отсортированный массив: {arr}")