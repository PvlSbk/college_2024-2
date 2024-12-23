# Задание от 09.10.2024
# 1. Создайте класс Mammal с методом give_birth, который выводит "Я даю жизнь".
# Создайте класс Flying с методом fly, который выводит "Я летаю".
# Создайте класс Bat, который наследует от обоих классов (Mammal и Flying). Определите метод give_birth_bat, чтобы он возвращал "Я летучая мышь, я даю жизнь".
# Протестируйте максимально все классы

class Mammal:
    def give_birth(self):
        print("Я даю жизнь")

class Flying:
    def fly(self):
        print("Я летаю")
class Bat(Mammal, Flying):
    def give_birth_bat(self):
        return "Я летучая мышь, я даю жизнь"

def main():
    bat = Bat()
    print(bat.give_birth_bat())
    bat.give_birth()
    bat.fly()

if __name__ == "__main__":
    main()

# 2. Создайте класс Robot с методом power_on, который выводит "Робот включен".
# Создайте класс Soldier с методом fight, который выводит "Солдат сражается".
# Создайте класс BattleRobot, который наследует оба класса.
# Определите метод power_on_br, чтобы он выводил "Боевая машина включена".
# Протестируйте максимально все классы

class Robot:
    def power_on(self):
        print("Робот включен")

class Soldier:
    def fight(self):
        print("Солдат сражается")

class BattleRobot(Robot, Soldier):
    def power_on_br(self):
        print("Боевая машина включена")

if __name__ == "__main__":
    robot = Robot()
    robot.power_on()

    soldier = Soldier()
    soldier.fight()

    battle_robot = BattleRobot()
    battle_robot.power_on()
    battle_robot.fight()
    battle_robot.power_on_br()