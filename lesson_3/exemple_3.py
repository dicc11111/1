arg1 = int (input ('Введите первое значение'))
arg2 = int (input ('Введите второе значение'))
arg3 = int (input ('Введите третье значение'))


def my_func(arg1, arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 > arg2 and arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3


print (f'Результат - {my_func (arg1, arg2, arg3)}')
