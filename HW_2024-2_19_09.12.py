# Задание от 09.12.24
# 1. Напишите программу, которая запрашивает у пользователя размер массива
# и затем динамически выделяет память для массива целых чисел (int) указанного размера.
# Пользователь вводит значения элементов массива. Затем пользователь вводит значение, которое нужно найти в массиве.
# Программа должна найти и вывести на консоль индекс первого вхождения этого значения в массиве.
# Если значение не найдено, программа должна вывести соответствующее сообщение.

class ArraySearch:
    def __init__(self, size):
        self.size = size
        self.array = []

    def input_elements(self):
        print(f"Введите {self.size} целых чисел:")
        for i in range(self.size):
            while True:
                try:
                    element = int(input(f"Элемент {i + 1}: "))
                    self.array.append(element)
                    break
                except ValueError:
                    print("Пожалуйста, введите целое число.")

    def find_element(self, target):
        if target in self.array:
            return self.array.index(target)
        else:
            return -1


def main():
    while True:
        try:
            size = int(input("Введите размер массива: "))
            if size <= 0:
                print("Размер массива должен быть положительным числом. Попробуйте снова.")
            else:
                break
        except ValueError:
            print("Пожалуйста, введите положительное целое число для размера массива.")

    array_search = ArraySearch(size)

    array_search.input_elements()

    while True:
        try:
            target = int(input("Введите число для поиска: "))
            break
        except ValueError:
            print("Пожалуйста, введите целое число.")

    index = array_search.find_element(target)
    if index != -1:
        print(f"Число {target} найдено на индексе {index}.")
    else:
        print(f"Число {target} не найдено в массиве.")


if __name__ == "__main__":
    main()

# 2. Напишите программу, которая запрашивает у пользователя размер массива
# и затем динамически выделяет память для массива целых чисел (int) указанного размера.
# Пользователь вводит значения элементов массива. Затем пользователь вводит значение нового элемента и индекс,
# куда его нужно добавить. Программа должна добавить новый элемент в указанный индекс
# и вывести измененный массив на консоль.

class ArrayManipulation:
    def __init__(self, size):
        self.size = size
        self.array = []

    def input_elements(self):
        print(f"Введите {self.size} целых чисел:")
        for i in range(self.size):
            while True:
                try:
                    element = int(input(f"Элемент {i + 1}: "))
                    self.array.append(element)
                    break
                except ValueError:
                    print("Пожалуйста, введите целое число.")

    def add_element_at_index(self, element, index):
        if 0 <= index <= len(self.array):
            self.array.insert(index, element)
        else:
            print("Неверный индекс. Элемент не был добавлен.")

    def display_array(self):
        print("Изменённый массив:", self.array)


def main():
    while True:
        try:
            size = int(input("Введите размер массива: "))
            if size <= 0:
                print("Размер массива должен быть положительным числом. Попробуйте снова.")
            else:
                break
        except ValueError:
            print("Пожалуйста, введите положительное целое число для размера массива.")

    array_manipulation = ArrayManipulation(size)

    array_manipulation.input_elements()

    while True:
        try:
            new_element = int(input("Введите новый элемент для добавления: "))
            break
        except ValueError:
            print("Пожалуйста, введите целое число.")

    while True:
        try:
            index = int(input(f"Введите индекс (от 0 до {size}) для добавления элемента: "))
            if 0 <= index <= size:
                break
            else:
                print(f"Индекс должен быть от 0 до {size}. Попробуйте снова.")
        except ValueError:
            print("Пожалуйста, введите целое число для индекса.")

    array_manipulation.add_element_at_index(new_element, index)

    array_manipulation.display_array()


if __name__ == "__main__":
    main()

# 3. Напишите программу, которая запрашивает у пользователя размер массива
# и затем динамически выделяет память для массива целых чисел (int) указанного размера.
# Пользователь вводит значения элементов массива. Затем пользователь вводит индекс элемента, который нужно удалить.
# Программа должна удалить элемент с указанным индексом и вывести измененный массив на консоль.

class DynamicArray:
    def __init__(self, size):
        self.size = size
        self.array = [0] * size
    def input_elements(self):
        print("Введите элементы массива:")
        for i in range(self.size):
            self.array[i] = int(input(f"Элемент {i + 1}: "))

    def delete_element(self, index):
        if 0 <= index < self.size:
            del self.array[index]
            self.size -= 1
        else:
            print("Ошибка: индекс вне диапазона")

    def display(self):
        print("Массив после изменений:", self.array)


def main():
    size = int(input("Введите размер массива: "))
    array = DynamicArray(size)

    array.input_elements()

    index_to_delete = int(input(f"Введите индекс элемента для удаления (0-{size - 1}): "))
    array.delete_element(index_to_delete)

    array.display()


if __name__ == "__main__":
    main()