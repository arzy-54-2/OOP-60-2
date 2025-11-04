# Наследование

# родительский\супер Класс
class Hero:
    def __init__(self, lvl, hp, name=None,):
        # Атрибуты класса
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        return self.name

class Skill:
    pass

# дочерний класс
class MageHero(Hero):

    def __init__(self, lvl, hp, mp):
        super().__init__(lvl, hp)
        self.mp = mp

    def action1(self):
        return f"Я потомок {self.name}"


class WarriorHero(MageHero):
    pass

obj_1 = Hero("Олег", 10, 100)
obj_2 = MageHero("Ardager", 10, 100, 50)
obj_3 = WarriorHero("Ardager", 10, 100, 50)

# print(obj_1.action())
# print(obj_2.action())



class A:
    def action(self):
        return "A"

class B(A):
    def action(self):
        return "B"

class C(A):
    def action(self):
        return "C"

class D(C, B):

    def action(self):
        return "test"

obj_4 = D()

print(D.__mro__)



class Animal:
    def action(self):
        return "Animal"

class Swim(Animal):
    def action(self):
        return "Swim"

class Fly(Animal):
    def action(self):
        return f"Fly"

class Duck(Fly,Swim):
    ...

duck = Duck()

print(duck.action())