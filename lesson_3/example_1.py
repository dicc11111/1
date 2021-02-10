arg1 = int (input ('Введите делимое: '))
arg2 = int (input ('Введите делитель: '))

"""Функция деления с предусматриванием деления на ноль"""


def my_fum(arg1, arg2):
    if arg2 != 0:
        return arg1 / arg2
    else:
        print ("Wrong number! Devider can't be null")


print (my_fum (arg1, arg2))
