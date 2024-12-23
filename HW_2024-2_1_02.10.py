# Задание от 02.10.24
# Создайте класс Car, который представляет автомобиль. Определите в этом классе атрибуты make и model,
# которые представляют марку и модель автомобиля.
# Через параметры конструктора передайте этим атрибутам начальные значения.
# Также в классе определите метод start, который выводит сообщение о том, что автомобиль заведен,
# и метод stop, который выводит сообщение о том, что автомобиль остановлен.
# При этом добавьте метод info, который выводит информацию о марке и модели автомобиля.
# добавьте атрибут status, который хранит текущее состояние машины (Заведен или остановлен)

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.status = "Остановлен"

    def start(self):
        self.status = "Заведен"
        print(f"Автомобиль {self.make} {self.model} заведен.")

    def stop(self):
        self.status = "Остановлен"
        print(f"Автомобиль {self.make} {self.model} остановлен.")

    def info(self):
        print(f"Марка: {self.make}, Модель: {self.model}, Состояние: {self.status}")

def main():
    car = Car("Toyota", "Camry")
    car.info()
    car.start()
    car.info()
    car.stop()
    car.info()

if __name__ == "__main__":
    main()