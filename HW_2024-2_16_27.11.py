# Задание от 27.11.24
# 1. Напишите программу, которая запрашивает у пользователя ввод строки и удаляет все пробелы из неё.
# Выведите результат на экран.

class StringProcessor:
    def __init__(self, input_string):
        self.input_string = input_string

    def remove_spaces(self):
        return self.input_string.replace(" ", "")

user_input = input("Введите строку: ")

processor = StringProcessor(user_input)
result = processor.remove_spaces()

# Выводим результат
print("Строка без пробелов:", result)

# 2. Напишите программу, которая запрашивает у пользователя строку и подсчитывает количество определенных букв в ней.
# Выведите результаты на экран.

class StringAnalyzer:
    def __init__(self, input_string):
        self.input_string = input_string

    def count_letter(self, letter):
        return self.input_string.count(letter)

user_input = input("Введите строку: ")

letter_to_count = input("Введите букву для подсчета: ")

analyzer = StringAnalyzer(user_input)
count = analyzer.count_letter(letter_to_count)

print(f"Буква '{letter_to_count}' встречается {count} раз(а) в строке.")

# 3. Создайте программу, которая запрашивает у пользователя ввод двух строк и объединяет их в одну,
# вставляя между ними пробел. Выведите полученную строку.

class StringMerger:
    def __init__(self, string1, string2):
        self.string1 = string1
        self.string2 = string2

    def merge_strings(self):
        return self.string1 + " " + self.string2

first_string = input("Введите первую строку: ")
second_string = input("Введите вторую строку: ")

merger = StringMerger(first_string, second_string)
result = merger.merge_strings()

print("Объединенная строка:", result)