string = input ("Введите строку из слов, состоящих из латинских прописных букв " "в нижнем регистре: ")


def int_func(A):
    result = ""
    for a in A:
        a = a[0].upper () + a[1:]
        result += a + " "
    return result


print (int_func (string.split ()))
