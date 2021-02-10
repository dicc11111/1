def my_sum():
    sum_res = 0
    a = False
    while a == False:
        number = input ('Введите числа или * для завершения выполнения программы ').split ()

        res = 0
        for el in range (len (number)):
            if number[el] == '*':
                a = True
                break
            else:
                res = res + int (number[el])
        sum_res = sum_res + res
        print (f'Сумма чисел {sum_res}')
    print (f'Финальная сумма чисел {sum_res}')


my_sum ()
