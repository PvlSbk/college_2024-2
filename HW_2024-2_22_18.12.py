# Задание от 18.12.24
# 1. Создайте базовый класс Employee (сотрудник), который содержит:
# Приватные переменные:
# name (имя сотрудника).
# salary (зарплата сотрудника).
# Конструктор для инициализации name и salary.
# Функцию displayInfo(), которая выводит информацию о сотруднике.
# Затем создайте два производных класса:
# Manager (менеджер), который добавляет переменную bonus (бонус).
# Developer (разработчик), который добавляет переменную linesOfCode (количество строк кода).
# Переопределите функцию displayInfo() в каждом производном классе, чтобы она выводила дополнительную информацию.
# В функции main создайте объекты Manager и Developer, вызовите displayInfo() и проверьте результат.

class Employee:
    def __init__(self, name, salary):
        self.__name = name  # Приватная переменная для имени
        self.__salary = salary  # Приватная переменная для зарплаты

    def displayInfo(self):
        print(f"Имя: {self.__name}, Зарплата: {self.__salary}")


class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.__bonus = bonus
    def displayInfo(self):
        super().displayInfo()
        print(f"Бонус: {self.__bonus}")


class Developer(Employee):
    def __init__(self, name, salary, linesOfCode):
        super().__init__(name, salary)
        self.__linesOfCode = linesOfCode

    def displayInfo(self):
        super().displayInfo()
        print(f"Количество строк кода: {self.__linesOfCode}")


def main():
    manager = Manager("Иван Иванов", 100000, 15000)
    developer = Developer("Петр Петров", 80000, 20000)

    print("Информация о менеджере:")
    manager.displayInfo()

    print("\nИнформация о разработчике:")
    developer.displayInfo()


if __name__ == "__main__":
    main()

# 2. Создайте класс Student, который содержит:
# Приватные переменные:
# name (имя студента).
# age (возраст студента).
# Статическую переменную studentCount, которая будет считать количество созданных объектов класса Student.
# Конструктор, который принимает name и age, и увеличивает значение studentCount на 1.
# Деструктор, который уменьшает значение studentCount на 1.
# Статическую функцию getStudentCount(), которая возвращает текущее значение studentCount.
# В функции main создайте несколько объектов класса Student, выведите количество созданных объектов
# с помощью функции getStudentCount(), а затем удалите некоторые объекты и снова выведите количество объектов.

class Student:
    studentCount = 0

    def __init__(self, name, age):
        self.name = name
        self.__age = age
        Student.studentCount += 1

    def __del__(self):
        Student.studentCount -= 1

    @staticmethod
    def getStudentCount():
        return Student.studentCount

def main():
    student1 = Student("Алексей", 20)
    student2 = Student("Мария", 22)
    student3 = Student("Светлана", 21)

    print("Количество студентов:", Student.getStudentCount())

    del student2

    print("Количество студентов после удаления:", Student.getStudentCount())

if __name__ == "__main__":
    main()