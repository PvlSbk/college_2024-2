# Задание от 23.10.24
# 1. Создайте абстрактный класс Character с абстрактными методами attack и defend.
# Реализуйте два подкласса: Warrior и Mage, которые будут иметь свои уникальные реализации этих методов.
# Например, Warrior может иметь метод атаки с использованием оружия, а Mage может использовать заклинание для атаки.

from abc import ABC, abstractmethod


class Character(ABC):

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def defend(self):
        pass


class Warrior(Character):

    def attack(self):
        print("Воин атакует с использованием меча!")

    def defend(self):
        print("Воин защищается щитом!")


class Mage(Character):

    def attack(self):
        print("Маг атакует заклинанием огня!")

    def defend(self):
        print("Маг использует щит магии для защиты!")


# Тестирование классов
if __name__ == "__main__":
    warrior = Warrior()
    mage = Mage()

    print("Warrior:")
    warrior.attack()
    warrior.defend()

    print("\nMage:")
    mage.attack()
    mage.defend()

# 2. Определите абстрактный класс Book, который будет иметь атрибуты title и author,
# и абстрактный метод get_summary, который будет возвращать краткое описание книги.
# Реализуйте следующие подклассы:
# Fiction: должен переопределить метод get_summary, чтобы предоставлять описание художественной книги.
# NonFiction: должен переопределить метод get_summary, чтобы предоставлять описание нехудожественной книги.
# Poetry: в этом классе вы должны также переопределить метод get_summary, чтобы предоставлять описание книги стихов.
# Реализуйте возможность создать список книг разных типов и пройтись по этому списку,
# вызывая метод get_summary для каждой книги, чтобы выводить описание.

from abc import ABC, abstractmethod

class Book(ABC):

    def __init__(self, title, author):
        self.title = title
        self.author = author

    @abstractmethod
    def get_summary(self):
        pass


class Fiction(Book):

    def get_summary(self):
        return f"Художественная книга '{self.title}' написана {self.author}. Это произведение вымышленной литературы."


class NonFiction(Book):

    def get_summary(self):
        return f"Нехудожественная книга '{self.title}' написана {self.author}. Это произведение основано на реальных фактах."


class Poetry(Book):

    def get_summary(self):
        return f"Книга стихов '{self.title}' написана {self.author}. Это сборник поэзии, наполненный эмоциями и образами."


if __name__ == "__main__":
    books = [
        Fiction("1984", "Джордж Оруэлл"),
        NonFiction("Sapiens: A Brief History of Humankind", "Юваль Ной Харари"),
        Poetry("The Waste Land", "Т. С. Элиот")
    ]

    for book in books:
        print(book.get_summary())

