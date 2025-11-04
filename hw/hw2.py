class Animal:
    def __init__(self, name: str, age: int, health: int):
        self.name = name
        self.age = age
        self.health = health  # очки здоровья

    def info(self):
        return f"{self.name}, {self.age} лет, здоровье {self.health}"

    def use_ability(self):
        """Переопределяется в наследниках"""
        return f"{self.name} использует базовую способность."


# 1. Миксины
class Flyable:
    def use_ability(self):
        return super().use_ability() + " летит."


class Swimmable:
    def use_ability(self):
        return super().use_ability() + " плавает."


class Invisible:
    def use_ability(self):
        return super().use_ability() + " не видит."


# 2. Животные (пример Duck)
class Duck(Flyable, Swimmable, Animal):
    ...


# 3. Phoenix – свой метод reborn()
class Phoenix(Flyable, Invisible, Animal):

    def reborn(self) -> str:
        self.health += 100
        return f"{self.name} возрождается из пепла! Здоровье +100 (теперь {self.health})"


class Bat(Invisible, Swimmable, Animal):
    ...


class Frog(Swimmable, Flyable, Animal):
    ...


# 4. Zoo
class Zoo:

    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def show_all(self):
        for animal in self.animals:
            print(animal.info())

    def perform_show(self):
        for animal in self.animals:
            print(animal.use_ability())


if __name__ == "__main__":
    zoo = Zoo()

    duck = Duck("Дональд", 3, 80)
    bat = Bat("Бэтти", 5, 60)
    frog = Frog("Кермит", 2, 50)
    phoenix = Phoenix("Феникс", 100, 200)

    for animal in (duck, bat, frog, phoenix):
        zoo.add_animal(animal)

    print("=== Информация о животных ===")
    zoo.show_all()

    print("\n=== Шоу суперспособностей ===")
    zoo.perform_show()
    #
    print("\nMRO для Duck:", Duck.__mro__)
    print("MRO для Phoenix:", Phoenix.__mro__)

    # Доп. проверка
    print(phoenix.reborn())