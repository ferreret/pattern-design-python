from abc import ABC, abstractmethod
import random


class Enemy(ABC):
    @abstractmethod
    def attack(self):
        pass


class Boss(ABC):
    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def special_attack(self):
        pass


class DesertEnemy(Enemy):
    def attack(self):
        print("Ataca al enemigo con una lanza -5")


class WaterEnemy(Enemy):
    def attack(self):
        print("Ataca al enemigo con chorro de agua -5")


class DesertBoss(Boss):
    def attack(self):
        print("El jefe del desierto ataca con una rafaga de arena -10")

    def special_attack(self):
        print("El jefe del desierto lanza una tormenta de arena -20")


class WaterBoss(Boss):
    def attack(self):
        print("El jefe del agua ataca con un chorro de agua a presion -10")

    def special_attack(self):
        print("El jefe del agua lanza un sunami -20")


class EnemiesFactory(ABC):
    @abstractmethod
    def create_enemy(self) -> Enemy:
        pass

    @abstractmethod
    def create_boss(self) -> Boss:
        pass


class DesertEnemiesFactory(EnemiesFactory):
    def create_enemy(self) -> Enemy:
        return DesertEnemy()

    def create_boss(self) -> Boss:
        return DesertBoss()


class WaterEnemiesFactory(EnemiesFactory):
    def create_enemy(self) -> Enemy:
        return WaterEnemy()

    def create_boss(self) -> Boss:
        return WaterBoss()


class Game:
    def __init__(self, factory: EnemiesFactory):
        self.__factory = factory
        self.__enemy1 = self.__factory.create_enemy()
        self.__enemy2 = self.__factory.create_enemy()

    def enemy_attack(self):
        who_attacks = random.randint(1, 4)

        match who_attacks:
            case 1:
                self.__enemy1.attack()
            case 2:
                self.__enemy2.attack()
            case 3:
                self.__factory.create_boss().attack()
            case 4:
                self.__factory.create_boss().special_attack()


# Aplicación -------------------------------------------------------------------
game = Game(WaterEnemiesFactory())
game.enemy_attack()
game.enemy_attack()
game.enemy_attack()
game.enemy_attack()
game.enemy_attack()