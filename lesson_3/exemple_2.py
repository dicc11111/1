name = input ("Введите имя: ")
surname = input ('Введите фамилию: ')
year: int = int (input ('Введите год: '))
city = input ('Введите город: ')
email = input ('Введите email: ')
telephone = int (input ('Телефон: '))

"""Реализовать вывод функции в одну строку"""


def my_func(name, surname, year, city, email, telephone):
    return list ([name, surname, year, city, email, telephone])


print (*my_func (name, surname, year, city, email, telephone))
