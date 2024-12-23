# Задание от 21.10.24
# 1. Создать класс "Матрица", который будет иметь магический метод mul, реализующий умножение матрицы на число.

class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return "\n".join(["\t".join(map(str, row)) for row in self.data])

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            result = [[element * other for element in row] for row in self.data]
            return Matrix(result)
        else:
            raise ValueError("Можно умножать только на число (скаляр).")

# Пример:
matrix = Matrix([[1, 2], [3, 4]])
result_matrix = matrix * 3
print("Исходная матрица:")
print(matrix)
print("\nРезультат умножения на 3:")
print(result_matrix)

# 2. Создать класс "Фильм", который будет иметь магический метод len, возвращающий длительность фильма в минутах.

class Movie:
    def __init__(self, title, duration_minutes):
        self.title = title
        self.duration_minutes = duration_minutes

    def __str__(self):
        return f"Фильм: {self.title}, Длительность: {self.duration_minutes} минут"

    def __len__(self):
        return self.duration_minutes

# Пример
movie = Movie("Интерстеллар", 169)
print(movie)
print(f"Длительность фильма: {len(movie)} минут")