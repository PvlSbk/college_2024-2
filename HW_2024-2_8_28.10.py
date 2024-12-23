# Задание от 28.10.2024
# 1. Напишите функцию read_file(filename), которая принимает имя файла и возвращает его содержимое.
# Если файл не существует, функция должна возвращать строку "Ошибка: Файл не найден".

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "Ошибка: Файл не найден"

# Пример
filename = "example.txt"
file_content = read_file(filename)
print(file_content)

# 2. Напишите функцию process_data(data), которая принимает список чисел.
# Функция должна возвращать сумму всех чисел в списке.
# Если в списке есть элементы, которые не являются числами,
# функция должна игнорировать их и выводить сообщение "Ошибка: Неверный тип данных, пропущено [значение]".

def process_data(data):
    total_sum = 0
    for item in data:
        if isinstance(item, (int, float)):
            total_sum += item
        else:
            print(f"Ошибка: Неверный тип данных, пропущено {item}")
    return total_sum

# Пример
data_list = [1, 2, 'a', 3.5, None, 4]
result = process_data(data_list)
print("Сумма чисел:", result)