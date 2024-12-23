# Задание от 07.10.24
# Напишите программу с классом Student, в котором есть три приватных атрибута: name, groupNumber и age.
# По умолчанию name = Ivan, age = 18, groupNumber = 10A.
# Также создать геттеры и сеттеры.
# В программе необходимо создать 3 экземпляра класса Student,
# установить им разные имена, возраст и номер группы, также проверить работу геттеров и сеттеров.

class Student:
    def __init__(self, name="Ivan", groupNumber="10A", age=18):
        self.__name = name
        self.__groupNumber = groupNumber
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_groupNumber(self):
        return self.__groupNumber

    def set_groupNumber(self, groupNumber):
        self.__groupNumber = groupNumber

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

student1 = Student()  # по умолчанию
student2 = Student("Anna", "11B", 20)  # с параметрами
student3 = Student("Mikhail", "9C", 22)  # с параметрами

student1.set_name("Ivanov")
student1.set_groupNumber("12A")
student1.set_age(19)

student2.set_name("Svetlana")
student2.set_groupNumber("10B")
student2.set_age(21)

student3.set_name("Alexei")
student3.set_groupNumber("8D")
student3.set_age(23)

# Проверка 
print(f"Student 1: {student1.get_name()}, Group: {student1.get_groupNumber()}, Age: {student1.get_age()}")
print(f"Student 2: {student2.get_name()}, Group: {student2.get_groupNumber()}, Age: {student2.get_age()}")
print(f"Student 3: {student3.get_name()}, Group: {student3.get_groupNumber()}, Age: {student3.get_age()}")