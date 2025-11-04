

# Класс
class Hero:
    # Конструктор класса
    def __init__(self, nick_name, lvl, hp):
        # Атрибуты класса
        self.nick_name = nick_name
        self.lvl = lvl
        self.hp = hp

    # Методы класса
    def action(self):
         return f"{self.nick_name} Hi this my base action!!"


# объект\экземпляр класса
kirito = Hero("Kirito", 100, 1000)
asuna = Hero("Asuna", 100, 1000)


simple_text = str("simple_text")
# simple_int = int(123)
# simple_float = float(123.12)
# class MageHero:

print(kirito.action())
print(asuna.action())
