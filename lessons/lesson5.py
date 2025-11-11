# 1. Что такое декоратор?
# Декоратор — это функция, которая принимает другую функцию как аргумент и
# возвращает новую функцию, обычно обернутую в дополнительную функциональность.

# class Person:
#
#     def simple_method(self):
#         pass
#
#     @staticmethod
#     def static_method(self):
#         pass
#
#     @classmethod
#     def class_method(cls):
#         pass

def simple_decorator(func):
    def wrapper():
        print('До выполнения!!')
        func()
        print('После выполнения!!!')
    return wrapper

@simple_decorator
def test():
    return print('Test')

# test()



def greeting_decorator(func):
    def wrapper(name, age, hobby):
        print(f"{func.__name__}")
        print(f"Привет {name}")
        func(name)
    return wrapper

@greeting_decorator
def greeting(name, age=None, hobby=None):
    return print(f"Как дела {name}?")


@greeting_decorator
def greeting2(name, age=None, hobby=None):
    return print(f"Как дела {name}?")

# greeting('Ardager', age=20, hobby='Python')



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
            return print('я новый метод')
    return NewClass

@class_decorator
class OldClass:
    def old_method(self):
        return print('Я старый метод')

obj_1 = OldClass()

# print(type(obj_1))

# obj_1.new_method()
# obj_1.old_method()




msg = "aradger" + "Привет!"


# msg.name
# msg.id
# msg.is_admin
black_list = ["ляя", "лол"]


def admin_decorator(func):
    def wrapper(msg):
        if msg.value in black_list:
            print('Бан!!')
        else:
            func()
    return wrapper

@admin_decorator
def send_msg(msg):
    print(msg)


def ban(command, user_id):
    print('Вы за банены')

send_msg()