# Задание от 14.10.2024
# 1.Создайте класс Kvadr_urav, у которого есть 3 атрибута a, b и c (параметры квадратного уравнения).
# И метод solve, который решает данное уравнение с учетом того,
# что у уравнения может быть 1 действительный корень,  2 действительных корня или нет действительных корней.

import math

class Kvadr_urav:
    def init(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def solve(self):
        D = self.b ** 2 - 4 * self.a * self.c
        if D > 0:
            x1 = (-self.b + math.sqrt(D)) / (2 * self.a)
            x2 = (-self.b - math.sqrt(D)) / (2 * self.a)
            return f"Два корня: x1 = {x1}, x2 = {x2}"
        elif D == 0:
            x = -self.b / (2 * self.a)
            return f"Один корень: x = {x}"
        else:
            return "Нет действительных корней"

# Пример:
eq1 = Kvadr_urav(1, -3, 2)
print(eq1.solve())
eq2 = Kvadr_urav(1, -2, 1)
print(eq2.solve())
eq3 = Kvadr_urav(1, 1, 1)
print(eq3.solve())

# 2. Создайте базовый класс Shape, который содержит атрибуты color (цвет) и border_thickness (толщина границы).
# Переопределите эти атрибуты в подклассах Circle и Rectangle,
# добавив собственные атрибуты,
# такие как radius (радиус) для круга и width (ширина) и height (высота) для прямоугольника.
# Также переопределите метод area() для вычисления площади.

import math

class Shape:
    def init(self, color, border_thickness):
        self.color = color
        self.border_thickness = border_thickness

    def area(self):
        raise NotImplementedError("Метод 'area' должен быть переопределен в подклассе")

class Circle(Shape):
    def init(self, color, border_thickness, radius):
        super().init(color, border_thickness)
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def init(self, color, border_thickness, width, height):
        super().init(color, border_thickness)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Пример:
circle = Circle(color="red", border_thickness=2, radius=5)
rectangle = Rectangle(color="blue", border_thickness=3, width=10, height=7)
print(f"Площадь круга: {circle.area()}")
print(f"Площадь прямоугольника: {rectangle.area()}")
print(f"Цвет круга: {circle.color}, Толщина границы круга: {circle.border_thickness}")
print(f"Цвет прямоугольника: {rectangle.color}, Толщина границы прямоугольника: {rectangle.border_thickness}")
