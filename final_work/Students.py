class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

    def to_file_string(self):
        """Returns a string that can be saved in a file."""
        return f"{self.student_id},{self.name},{self.age},{self.grade}"

class StudentManagementSystem:
    def __init__(self, filename="students_data.txt"):
        self.filename = filename
        self.students = []
        self.load_from_file()

    def add_student(self):
        student_id = input("Введите ID студента: ")
        name = input("Введите имя студента: ")
        age = input("Введите возраст студента: ")
        grade = input("Введите оценку студента: ")
        new_student = Student(student_id, name, age, grade)
        self.students.append(new_student)
        print("Студент успешно добавлен.")

    def remove_student(self):
        student_id = input("Введите ID студента для удаления: ")
        student_to_remove = None
        for student in self.students:
            if student.student_id == student_id:
                student_to_remove = student
                break
        if student_to_remove:
            self.students.remove(student_to_remove)
            print("Студент успешно удалён.")
        else:
            print("Студент не найден.")

    def display_all_students(self):
        if not self.students:
            print("Нет студентов для отображения.")
            return
        for student in self.students:
            print(student)

    def search_student(self):
        student_id = input("Введите ID студента для поиска: ")
        found = False
        for student in self.students:
            if student.student_id == student_id:
                print(student)
                found = True
                break
        if not found:
            print("Студент не найден.")

    def update_student(self):
        student_id = input("Введите ID студента для обновления: ")
        student_to_update = None
        for student in self.students:
            if student.student_id == student_id:
                student_to_update = student
                break
        if student_to_update:
            student_to_update.name = input(f"Введите новое имя (текущее: {student_to_update.name}): ")
            student_to_update.age = input(f"Введите новый возраст (текущий: {student_to_update.age}): ")
            student_to_update.grade = input(f"Введите новую оценку (текущая: {student_to_update.grade}): ")
            print("Данные студента обновлены.")
        else:
            print("Студент не найден.")

    def save_to_file(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            for student in self.students:
                file.write(student.to_file_string() + "\n")
        print("Данные успешно сохранены в файл.")

    def load_from_file(self):
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    student_data = line.strip().split(",")
                    if len(student_data) == 4:
                        student = Student(student_data[0], student_data[1], student_data[2], student_data[3])
                        self.students.append(student)
            print("Данные успешно загружены из файла.")
        except FileNotFoundError:
            print("Файл с данными не найден. Начинаем с пустой базы данных.")

    def export_to_text_file(self):
        export_filename = input("Введите имя файла для экспорта данных (например, 'export.txt'): ")
        with open(export_filename, "w") as file:
            for student in self.students:
                file.write(student.to_file_string() + "\n")
        print(f"Данные успешно экспортированы в файл {export_filename}.")

def main():
    system = StudentManagementSystem()

    while True:
        print("\nСистема управления студентами")
        print("1. Добавить студента")
        print("2. Удалить студента")
        print("3. Показать всех студентов")
        print("4. Найти студента")
        print("5. Обновить данные студента")
        print("6. Сохранить в файл")
        print("7. Экспортировать в текстовый файл")
        print("8. Выйти")

        choice = input("Введите ваш выбор (1-8): ")

        if choice == '1':
            system.add_student()
        elif choice == '2':
            system.remove_student()
        elif choice == '3':
            system.display_all_students()
        elif choice == '4':
            system.search_student()
        elif choice == '5':
            system.update_student()
        elif choice == '6':
            system.save_to_file()
        elif choice == '7':
            system.export_to_text_file()
        elif choice == '8':
            system.save_to_file()
            print("Выход из программы...")
            break
        else:
            print("Неверный выбор. Пожалуйста, введите число от 1 до 8.")

if __name__ == "__main__":
    main()
