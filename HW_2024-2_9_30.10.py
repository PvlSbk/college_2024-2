# Задание от 30.10.24
# Задача 1.
# Разработать класс для представления дробей и выполнения операций над ними. Класс должен обеспечивать создание дробей,
# их упрощение, а также поддержку умножения и деления как с другими дробями, так и с целыми числами.
# Требования к классу MyFraction:
# Инициализация:
# Конструктор класса должен принимать числитель (num) и знаменатель (den).
# Дробь должна быть упрощена при создании, используя наибольший общий делитель (НОД).
# Если числитель или знаменатель равен нулю, необходимо выбрасывать исключение ValueError с сообщением
# "Числитель и знаменатель не могут быть равны нулю".
# Генерация дробей:
# Реализовать статический метод generate(num_min, num_max, den_min, den_max),
# который будет случайным образом генерировать дробь с заданными диапазонами для числителя и знаменателя.
# Строковое представление:
# Реализовать метод __str__(), который возвращает строковое представление дроби в формате "числитель/знаменатель".
# Операции:
# Реализовать метод __mul__(self, other), который позволяет умножать дробь на другую дробь или целое число.
# Реализовать метод __truediv__(self, other), который позволяет делить дробь на другую дробь или целое число.
# Обрабатывать ошибки, выбрасывая исключение TypeError с сообщением
# "Можно умножать/делить только на дробь или целое число", если операция выполняется с неподходящим типом.
# Тестирование:
# Создать несколько дробей с использованием метода generate
# и продемонстрировать операции умножения и деления как с дробями, так и с целыми числами, выводя результаты на экран.

import random
import math


class MyFraction:
    def __init__(self, num, den):
        if num == 0 and den == 0:
            raise ValueError("Числитель и знаменатель не могут быть равны нулю")
        if den == 0:
            raise ValueError("Знаменатель не может быть равен нулю")

        gcd = math.gcd(num, den)
        self.num = num // gcd
        self.den = den // gcd

        if self.den < 0:
            self.num = -self.num
            self.den = -self.den

    @staticmethod
    def generate(num_min, num_max, den_min, den_max):
        num = random.randint(num_min, num_max)
        den = random.randint(den_min, den_max)
        return MyFraction(num, den)

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __mul__(self, other):
        if isinstance(other, MyFraction):
            # Умножение дробей: (a/b) * (c/d) = (a*c) / (b*d)
            num = self.num * other.num
            den = self.den * other.den
            return MyFraction(num, den)
        elif isinstance(other, int):
            # Умножение дроби на целое число: (a/b) * c = (a*c) / b
            num = self.num * other
            return MyFraction(num, self.den)
        else:
            raise TypeError("Можно умножать только на дробь или целое число")

    def __truediv__(self, other):
        if isinstance(other, MyFraction):
            # Деление дробей: (a/b) / (c/d) = (a/d) / (b/c)
            num = self.num * other.den
            den = self.den * other.num
            return MyFraction(num, den)
        elif isinstance(other, int):
            # Деление дроби на целое число: (a/b) / c = a / (b*c)
            den = self.den * other
            return MyFraction(self.num, den)
        else:
            raise TypeError("Можно делить только на дробь или целое число")

    def __eq__(self, other):
        if isinstance(other, MyFraction):
            return self.num == other.num and self.den == other.den
        return False


fraction1 = MyFraction.generate(1, 10, 1, 10)
fraction2 = MyFraction.generate(1, 10, 1, 10)
fraction3 = MyFraction.generate(1, 10, 1, 10)

print("Дробь 1:", fraction1)
print("Дробь 2:", fraction2)
print("Дробь 3:", fraction3)

# Умножение дробей
result_multiply = fraction1 * fraction2
print("Результат умножения дробей:", result_multiply)

# Деление дробей
result_divide = fraction1 / fraction2
print("Результат деления дробей:", result_divide)

# Умножение дроби на целое число
integer = 3
result_multiply_int = fraction1 * integer
print(f"Результат умножения дроби на {integer}:", result_multiply_int)

# Деление дроби на целое число
result_divide_int = fraction1 / integer
print(f"Результат деления дроби на {integer}:", result_divide_int)

# 2. Разработать консольное приложение для управления товарным ассортиментом и формирования чеков.
# Приложение должно предоставлять пользователю возможность взаимодействовать с прайс-листом товаров,
# выбирать товары для покупки и генерировать итоговый чек.
# Требования к приложению
# Классы и наследование:
# Создать абстрактный класс AbstractTovar с абстрактным методом print_menu().
# Реализовать класс Tovar, который наследует от AbstractTovar и реализует метод print_menu().
# Товарный ассортимент:
# Определить список товаров и соответствующих цен.
# Создать экземпляры класса Tovar для каждого товара и сохранить их в списке.
# Интерфейс пользователя:
# При запуске приложения отображать меню с доступными действиями:
# Показать прайс-лист товаров.
# Выбрать товар для покупки.
# Напечатать чек с выбранными товарами и их ценами.
# Выйти из приложения.
# Функциональность:
# При выборе опции "Показать прайс-лист" выводить список товаров с их ценами,
# разбивая их на страницы по 5 товаров на страницу.
# При выборе опции "Выбрать товар" позволить пользователю ввести название товара для его выбора.
# Если товар найден, он должен быть помечен как выбранный.
# При выборе опции "Напечатать чек" выводить список выбранных товаров и их цены, а также общую сумму покупки.
# Обработка ошибок:
# Обеспечить обработку ошибок ввода, чтобы пользователи могли корректно взаимодействовать с приложением,
# даже если они введут неверные данные.

from abc import ABC, abstractmethod


# Абстрактный класс для товара
class AbstractTovar(ABC):

    @abstractmethod
    def print_menu(self):
        pass


# Класс Tovar, реализующий AbstractTovar
class Tovar(AbstractTovar):
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.selected = False  # Флаг, чтобы отслеживать, выбран ли товар

    def print_menu(self):
        return f"{self.name} - {self.price} руб."

    def select(self):
        self.selected = True

    def deselect(self):
        self.selected = False


# Класс для работы с товарным ассортиментом
class TovarShop:
    def __init__(self):
        # Инициализация списка товаров
        self.tovars = [
            Tovar("Хлеб", 30),
            Tovar("Молоко", 50),
            Tovar("Яйца (10 шт.)", 75),
            Tovar("Сыр", 150),
            Tovar("Масло", 120),
            Tovar("Колбаса", 200),
            Tovar("Картофель", 60),
            Tovar("Помидоры", 80),
            Tovar("Огурцы", 70),
            Tovar("Яблоки", 90),
            Tovar("Апельсины", 120),
            Tovar("Кофе", 350)
        ]
        self.selected_tovars = []  # Список выбранных товаров

    def show_price_list(self, page=1, items_per_page=5):
        """Показывает прайс-лист с разбиением на страницы"""
        start = (page - 1) * items_per_page
        end = start + items_per_page
        paginated_tovars = self.tovars[start:end]

        if not paginated_tovars:
            print("Нет товаров для отображения.")
            return

        print(f"Страница {page}:")
        for tovar in paginated_tovars:
            print(f"- {tovar.print_menu()}")

        print(f"\nСтраница {page} завершена.")

    def select_tovar(self, name):
        """Выбирает товар по названию"""
        for tovar in self.tovars:
            if tovar.name.lower() == name.lower():
                tovar.select()
                self.selected_tovars.append(tovar)
                print(f"Товар '{name}' добавлен в корзину.")
                return
        print("Товар не найден.")

    def deselect_tovar(self, name):
        """Снимает выбор с товара"""
        for tovar in self.selected_tovars:
            if tovar.name.lower() == name.lower():
                tovar.deselect()
                self.selected_tovars.remove(tovar)
                print(f"Товар '{name}' удален из корзины.")
                return
        print("Товар не найден в корзине.")

    def print_receipt(self):
        """Печатает чек с выбранными товарами"""
        if not self.selected_tovars:
            print("Корзина пуста. Выберите товары для покупки.")
            return

        total = 0
        print("\nЧек:")
        for tovar in self.selected_tovars:
            print(f"{tovar.name} - {tovar.price} руб.")
            total += tovar.price
        print(f"\nИтого: {total} руб.")

    def clear_cart(self):
        """Очищает корзину"""
        for tovar in self.selected_tovars:
            tovar.deselect()
        self.selected_tovars.clear()
        print("Корзина очищена.")


def main():
    shop = TovarShop()
    current_page = 1

    while True:
        print("\nГлавное меню:")
        print("1. Показать прайс-лист товаров")
        print("2. Выбрать товар")
        print("3. Напечатать чек")
        print("4. Очистить корзину")
        print("5. Выйти")

    choice = input("Выберите действие (1-5): ")

    if choice == '1':
        shop.show_price_list(current_page)
        while True:
            action = input("Перейти на следующую страницу? (y/n): ").strip().lower()
            if action == 'y':
                current_page += 1
                shop.show_price_list(current_page)
            elif action == 'n':
                break
            else:
                print("Неверный ввод. Введите 'y' для следующей страницы или 'n' для выхода.")

    elif choice == '2':
        tovar_name = input("Введите название товара для выбора: ").strip()
        shop.select_tovar(tovar_name)

    elif choice == '3':
        shop.print_receipt()

    elif choice == '4':
        shop.clear_cart()

    elif choice == '5':
        print("Спасибо за использование приложения!")

    else:
        print("Неверный выбор. Пожалуйста, выберите номер из предложенных вариантов.")


# Запуск приложения
if __name__ == "__main__":
    main()
