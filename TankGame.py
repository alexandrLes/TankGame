from random import randint
import time


class Position:
    def __init__(self, status: bool, turn: str):
        """
        Class constructor. Designed to save the current position and game status.
        :param status: Game Status
        :param turn: Current player
        """
        self.GameStatus = status
        self.NowTurn = turn

    def setStatus(self, newStatus: bool) -> None:
        """
        Set game status
        :param newStatus: New Game Status
        :return: None
        """
        self.GameStatus = newStatus

    def getStatus(self) -> bool:
        """
        Get game status
        :return: Game Status
        """
        return self.GameStatus

    def setTurn(self, newTurn: str) -> None:
        """
        Set Current player
        :param newTurn: New Current Player
        :return: None
        """
        self.NowTurn = newTurn

    def getTurn(self) -> str:
        """
        Get Current player
        :return: Current player
        """
        return self.NowTurn


class Tank:
    def __init__(self, model: str, armor: int, min_damage: int, max_damage: int, health: int) -> None:
        """
        Main Class Constructor
        :param model: Сrew Name
        :param armor: Tank armor
        :param min_damage: Tank damage (determined randomly in a given range, which passed to the class initialization method)
        :param max_damage: Tank damage (determined randomly in a given range, which passed to the class initialization method)
        :param health: Tank Health
        """
        self.model = model
        self.armor = armor
        self.damage = randint(min_damage, max_damage + 1)
        self.health = health

    def getModel(self):
        """
        Get Crew Name
        :return: Crew Name
        """
        return self.model

    def print_info(self):
        """
        Crew Information
        :return: None
        """
        print(
            f"{self.model} имеет лобовую броню {self.armor} мм. при {self.health} ед. здоровья и урон в {self.damage} единиц.")

    def health_down(self, enemy_damage: int) -> None:
        """
        A function that lowers the health of the tank
        :param enemy_damage: Tank Damage - Enemy
        :return: None
        """
        try:
            self.health -= round(enemy_damage / self.armor, 2)
            print(
                f"{self.model} : Командир, по экипажу {self.model} попали, у нас осталось {self.health} единиц здоровья")
        except ZeroDivisionError:
            self.armor = 0.000000001
            self.health -= round(enemy_damage / self.armor, 2)
            print(
                f"{self.model} : Командир, по экипажу {self.model} попали, у нас осталось {self.health} единиц здоровья")

    def shot(self, enemy, position) -> None:
        """
        The function of shooting at the enemy
        :param enemy: Enemy Instance
        :param position: Current game position
        :return: None
        """
        if enemy.health <= 0:
            print(f"Экипаж танка {enemy.model} уничтожен!")
            position.setStatus(False)
        else:
            position.setTurn(enemy.model)
            self.health_down(enemy.damage)
            print(f"{self.model} : точно в цель!\n\n"
                  f"У противника {enemy.model} осталось {round(enemy.health, 2)} единиц здоровья")


if __name__ == '__main__':
    print('Приступаем к построению 1го танка! Игрок 1, введите название экипажа!')
    model = input()
    print('Игрок 1, установите броню корабля!')
    armor = int(input())
    print('Игрок 1, установите границы урона вашего танка! Введите Начальную границу!')
    min_damage = int(input())
    print('Игрок 1, установите границы урона вашего танка! Введите Конечную границу!')
    max_damage = int(input())
    print('Игрок 1, установите значение здоровья вашего танка!')
    health = int(input())
    print('Танк Игрока 1 успешно построен!')
    tank_1 = Tank(model, armor, min_damage, max_damage, health)

    print('Приступаем к построению 2го танка! Игрок 2, введите название экипажа!')
    model2 = input()
    print('Игрок 2, установите броню корабля!')
    armor2 = int(input())
    print('Игрок 2, установите границы урона вашего танка! Введите Начальную границу!')
    min_damage2 = int(input())
    print('Игрок 2, установите границы урона вашего танка! Введите Конечную границу!')
    max_damage2 = int(input())
    print('Игрок 2, установите значение здоровья вашего танка!')
    health2 = int(input())
    print('Танк Игрока 2 успешно построен!')
    tank_2 = Tank(model2, armor2, min_damage2, max_damage2, health2)
    print('--- --- ---')
    tank_1.print_info()
    print('---')
    tank_2.print_info()
    print('---\n\n')
    position = Position(True, tank_1.getModel())
    time.sleep(3)
    count_of_iteration_1 = 0
    count_of_iteration_2 = 0
    while position.getStatus() is not False:
        if position.getTurn() == model:
            count_of_iteration_1 += 1
            print('Стреляет экипаж: ' + position.getTurn())
            time.sleep(2)
            tank_1.shot(tank_2, position)
            time.sleep(2)
        elif position.getTurn() == model2:
            count_of_iteration_2 += 1
            print('Стреляет экипаж: ' + position.getTurn())
            time.sleep(2)
            tank_2.shot(tank_1, position)
            time.sleep(2)

    print('\n\n--- --- ИГРА ОКОНЧЕНА --- ---')
    print(f'Количество итераций у экипажа {model}: {count_of_iteration_1}')
    print(f'Количество итераций у экипажа {model2}: {count_of_iteration_2}')
