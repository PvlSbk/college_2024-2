# Задание от 11.11.24
# 1. Напишите программу обмена валют: программа запрашивает текущий курс доллара, например, к рублю,
# и количество единиц (рублей) для конвертации и выводит на консоль сконвертированную сумму в долларах.

class CurrencyConverter:
    def __init__(self):
        self.exchange_rate = 0.0

    def set_exchange_rate(self):
        try:
            self.exchange_rate = float(input("Введите текущий курс доллара к рублю: "))
            if self.exchange_rate <= 0:
                print("Курс доллара должен быть положительным числом.")
                self.exchange_rate = 0.0  # сбросить курс
        except ValueError:
            print("Ошибка ввода. Введите корректное число для курса.")

    def convert_rubles_to_dollars(self, rubles):
        if self.exchange_rate == 0:
            print("Сначала необходимо установить курс доллара.")
            return None
        return rubles / self.exchange_rate

    def print_converted_amount(self, rubles):
        dollars = self.convert_rubles_to_dollars(rubles)
        if dollars is not None:
            print(f"{rubles} рублей = {dollars:.2f} долларов по курсу {self.exchange_rate:.2f} рублей за доллар.")

def main():
    converter = CurrencyConverter()

    converter.set_exchange_rate()

    try:
        rubles = float(input("Введите количество рублей для конвертации: "))
        if rubles <= 0:
            print("Количество рублей должно быть положительным числом.")
        else:
            converter.print_converted_amount(rubles)
    except ValueError:
        print("Ошибка ввода. Введите корректное число для суммы рублей.")


if __name__ == "__main__":
    main()

# 2. Разработайте программу, которая преобразует метры в километры и остаток метров. Программа должна:
#  - Запрашивать у пользователя количество метров.
#  - Вычислять, сколько это километров и сколько остается метров.
#  - Выводить результат в формате: "X километров и Y метров".

class MeterConverter:
    def __init__(self, meters):
        self.meters = meters
        self.kilometers = 0
        self.remaining_meters = 0

    def convert(self):
        """Преобразует метры в километры и остаточные метры."""
        self.kilometers = self.meters // 1000
        self.remaining_meters = self.meters % 1000

    def display_result(self):
        """Выводит результат преобразования."""
        print(f"{self.kilometers} километров и {self.remaining_meters} метров")


def main():
    try:
        meters = int(input("Введите количество метров: "))

        if meters < 0:
            print("Количество метров не может быть отрицательным.")
            return

        converter = MeterConverter(meters)
        converter.convert()
        converter.display_result()

    except ValueError:
        print("Ошибка ввода. Введите корректное количество метров.")


if __name__ == "__main__":
    main()

# 3. Разработайте программу, которая выполняет следующие действия:
# Запрашивает у пользователя радиус круга.
# Используя формулу площади круга S=π×r^2
# Выводит результат на экран в формате: "Площадь круга с радиусом R составляет S".

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

    def display_area(self):
        area = self.calculate_area()
        print(f"Площадь круга с радиусом {self.radius} составляет {area:.2f}")


def main():
    try:
        radius = float(input("Введите радиус круга: "))

        if radius <= 0:
            print("Радиус должен быть положительным числом.")
            return

        circle = Circle(radius)
        circle.display_area()

    except ValueError:
        print("Ошибка ввода. Введите корректное число для радиуса.")


# Запуск программы
if __name__ == "__main__":
    main()