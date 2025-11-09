# # class Test:
# #
# #     # double underline
# #     def __init__(self, name):
# #         self.name = name
# #
# #     def __str__(self):
# #         return self.name
# #
# #
# # # int_test = 123
# # # int_test2 = 1233
# # #
# # # print(int_test > int_test2)
# #
# # # test_obj = Test("test")
# # #
# # # test_tsr = "123"
# # #
# # # print(test_obj)
# #
# #
# # class Post:
# #     def __init__(self, x, y, array):
# #         self.x = x
# #         self.y = y
# #         self.array = array
# #
# #
# #     def __lt__(self, other):
# #         return self.x < other.x
# #
# #     def __gt__(self, other):
# #         return self.y > other.x
# #
# #     def __getitem__(self, item):
# #         return self.array[item]
# #
# # class MyList(list):
# #     pass
# # #
# # # my_list = MyList([1, 2, 3])
# # # # print(my_list[2])
# # #
# # # origin_list = [1, 2, 3]
# # # print(origin_list[1, 2, 3])
# #
# #
# #
# #
# #
# #
# # class Money:
# #
# #     def __init__(self, sum, currency):
# #         self.sum = sum
# #         self.currency = currency
# #
# #     def __eq__(self, other):
# #         if self.currency == other.currency:
# #             return True
# #         else:
# #             return False
# #
# #     def __add__(self, other):
# #         if self.currency == other.currency:
# #             return self.sum + other.sum
# #         else:
# #             return f"Валиты не равны {self.currency} {other.currency}"
# #
# #     def __call__(self, *args, **kwargs):
# #         pass
# #
# #     def __new__(cls, *args, **kwargs):
# #         pass
# #
# #
# #
# # SOM = Money(100, "SOM")
# # SOM2 = Money(100, "SOM")
# # USD = Money(100, "USD")
# #
# # print(SOM + USD)
# # print(SOM + SOM2)
# #
# #
# #
# #
# #
# #
# # # obj_1 = Vector(1, 2, [1, 2, 3])
# # # # obj_2 = Vector(3, 4)
# # # # obj_3 = Vector(3, 4)
# # # print(obj_1[2])
#
#
#
# class BankAccount:
#     # Атрибута класса
#     bank_name = "Simba"
#
#     def __init__(self, first_name, last_name, balance):
#         # Атрибута экземпляра класса
#         self.first_name = first_name
#         self.last_name = last_name
#         self.balance = balance
#
#
#     def get_name(self):
#         return self.first_name
#
#     @property
#     def full_name(self):
#         return f"{self.first_name} {self.last_name}"
#
#     @classmethod
#     def get_bank_name(cls):
#         return cls.bank_name
#
#     @staticmethod
#     def calculate_deposit():
#         return 123
#
#
# ardager = BankAccount("Ardager", "Kartanbekov", 10000)
# john = BankAccount("John", "Doe", 999)
#
# # print(ardager.first_name)
# # print(john.get_name())
# print(john.full_name)
#
