# Задание от 20.11.24
# 1. Напишите программу, которая запрашивает у пользователя размер массива и его элементы,
# а затем запрашивает число и проверяет, присутствует ли это число в массиве. Выведите соответствующее сообщение.

class ArrayChecker:
    def __init__(self, array):
        self.array = array

    def check_number(self, number):
        if number in self.array:
            print(f"Число {number} присутствует в массиве.")
        else:
            print(f"Число {number} не найдено в массиве.")

try:
    size = int(input("Введите размер массива: "))
    array = []
    print(f"Введите {size} элементов массива:")
    for i in range(size):
        element = int(input(f"Элемент {i + 1}: "))
        array.append(element)
    checker = ArrayChecker(array)
    number = int(input("Введите число для поиска в массиве: "))
    checker.check_number(number)

except ValueError:
    print("Ошибка: пожалуйста, введите корректные числовые значения.")

# 2. Напишите программу, которая запрашивает у пользователя размер массива и его элементы,
# а затем находит и выводит максимальный и минимальный элементы массива.

class ArrayProcessor:
    def __init__(self, array):
        self.array = array

    def find_max_min(self):
        max_value = max(self.array)
        min_value = min(self.array)
        print(f"Максимальный элемент массива: {max_value}")
        print(f"Минимальный элемент массива: {min_value}")

try:
    size = int(input("Введите размер массива: "))

    array = []
    print(f"Введите {size} элементов массива:")
    for i in range(size):
        element = int(input(f"Элемент {i + 1}: "))
        array.append(element)
    processor = ArrayProcessor(array)

    processor.find_max_min()

except ValueError:
    print("Ошибка: пожалуйста, введите корректные числовые значения.")

# 3. Напишите программу, которая запрашивает у пользователя размер массива, его элементы и значение элемента,
# который нужно удалить. Программа должна удалить все вхождения этого элемента и вывести новый массив.

class ArrayManipulator:
    def __init__(self, array):
        self.array = array

    def remove_element(self, element):
        self.array = [item for item in self.array if item != element]
        return self.array

try:
    size = int(input("Введите размер массива: "))
    array = []
    print(f"Введите {size} элементов массива:")
    for i in range(size):
        element = int(input(f"Элемент {i + 1}: "))
        array.append(element)

    manipulator = ArrayManipulator(array)

    element_to_remove = int(input("Введите элемент, который нужно удалить из массива: "))

    new_array = manipulator.remove_element(element_to_remove)

    print(f"Новый массив после удаления элемента {element_to_remove}: {new_array}")
except ValueError:
    print("Ошибка: пожалуйста, введите корректные числовые значения.")

# 4. Напишите программу, которая запрашивает у пользователя размеры двух массивов и их элементы,
# а затем создает новый массив, который содержит элементы обоих массивов, и выводит его.

class ArrayMerger:
    def __init__(self, array1, array2):
        self.array1 = array1
        self.array2 = array2

    def merge_arrays(self):
        return self.array1 + self.array2

try:
    size1 = int(input("Введите размер первого массива: "))
    array1 = []
    print(f"Введите {size1} элементов первого массива:")
    for i in range(size1):
        element = int(input(f"Элемент {i + 1}: "))
        array1.append(element)

    size2 = int(input("Введите размер второго массива: "))

    array2 = []
    print(f"Введите {size2} элементов второго массива:")
    for i in range(size2):
        element = int(input(f"Элемент {i + 1}: "))
        array2.append(element)

    merger = ArrayMerger(array1, array2)

    merged_array = merger.merge_arrays()

    print(f"Объединенный массив: {merged_array}")

except ValueError:
    print("Ошибка: пожалуйста, введите корректные числовые значения.")

# 5. Напишите программу, которая запрашивает у пользователя размер массива и его элементы,
# а затем сортирует массив по возрастанию (можно использовать сортировку пузырьком) и выводит отсортированный массив.

class ArraySorter:
    def __init__(self, array):
        self.array = array

    def bubble_sort(self):
        n = len(self.array)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
        return self.array

try:
    size = int(input("Введите размер массива: "))
    array = []
    print(f"Введите {size} элементов массива:")
    for i in range(size):
        element = int(input(f"Элемент {i + 1}: "))
        array.append(element)
    sorter = ArraySorter(array)
    sorted_array = sorter.bubble_sort()
    print(f"Отсортированный массив: {sorted_array}")

except ValueError:
    print("Ошибка: пожалуйста, введите корректные числовые значения.")