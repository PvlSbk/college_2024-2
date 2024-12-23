# Задание от 25.11.24
# 1. Напишите программу, которая проверяет, является ли двумерный массив симметричным относительно главной диагонали

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0]) if matrix else 0

    def is_symmetric(self):
        if self.rows != self.cols:
            return False

        for i in range(self.rows):
            for j in range(i + 1, self.cols):
                if self.matrix[i][j] != self.matrix[j][i]:
                    return False

        return True


matrix_input = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]

matrix = Matrix(matrix_input)

if matrix.is_symmetric():
    print("Да.")
else:
    print("Нет.")

# 2. Напишите программу, которая ищет заданный элемент в двумерном массиве и возвращает его позицию (строка и столбец).
# Если элемент не найден, программа должна вывести соответствующее сообщение.

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def find_element(self, target):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == target:
                    return i, j
        return None

matrix_input = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

target = int(input("Введите элемент для поиска: "))

matrix = Matrix(matrix_input)

position = matrix.find_element(target)

if position:
    print(f"Элемент {target} найден на позиции: строка {position[0] + 1}, столбец {position[1] + 1}.")
else:
    print(f"Элемент {target} не найден в матрице.")

# 3. Напишите программу, которая транспонирует двумерный массив (меняет строки на столбцы).

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def transpose(self):
        return [[self.matrix[j][i] for j in range(len(self.matrix))] for i in range(len(self.matrix[0]))]

matrix_data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix = Matrix(matrix_data)

transposed_matrix = matrix.transpose()

print("Оригинальная матрица:")
for row in matrix_data:
    print(row)

print("\nТранспонированная матрица:")
for row in transposed_matrix:
    print(row)