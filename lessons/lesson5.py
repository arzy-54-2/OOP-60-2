# # class Swimm:
# #     def move(self):
# #         return f"Плавает"
# #     pass
# # class Flyable:
# #     def move(self):
# #         return f"Летает"
# #     pass
# # class Animal:
# #     def move(self):
# #         return f"Двигается"
# #     pass
# #
# # class Duck(Animal, Swimm, Flyable):
# #     # def move(self):
# #     #     return "Может плавать летать и ходить"
# #     pass
# #
# # donald_duck = Duck()
# # # print(donald_duck.move())
# # print(Duck.__mro__)
#
#
# class A:
#     def action(self):
#         return print("A")
#
# class B(A):
#     def action(self):
#         super().action()
#         return print("B")
#
# class C(A):
#     def action(self):
#         # super().action()
#         return print("C")
#
# class D(B, C):
#     # def action(self):
#     #     return "D"
#     pass
#
# obj_d = D()
# obj_d.action()
# print(D.__mro__)



# @abstractmethod
# @staticmethod
# @classmethod
# @property

# Декоратор
# def simple_decorator(func):
#     def wrapper():
#         print('До выполнения!!!')
#         func()
#         print('после выполнения!!')
#     return wrapper
#
#
# @simple_decorator
# def say_hello():
#     return print("hello!!")
#
# @simple_decorator
# def test():
#     return print("test")
# # say_hello()
# # test()
#
#
# def greeting_decorator(func):
#     def wrapper(name):
#         print(f'Hello !!')
#         func(name)
#     return wrapper
#
# @greeting_decorator
# def greet(name):
#     return print(f"Как дела {name}?")
#
#
# greet("Ardager")

def repeat_decorator(n):
    def decorator(func):
        def wrapper():
            for i in range(n):
                func()
        return wrapper
    return decorator


@repeat_decorator(5)
def hello_world():
    return print("Hello World")

# hello_world()


def class_decorator(cls):
    class NewClass(cls):
        def new_method(self):
            return print("I am a new method!!")
    return NewClass

@class_decorator
class OldClass:
    def old_method(self):
        return print("I am old method!!")

obj_1 = OldClass()

print(type(obj_1))

class I:
    def t(self):
        pass

class J(I):
    def t2(self):