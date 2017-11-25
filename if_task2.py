###Написать функцию, которая принимает на вход две строки.
###Если строки одинаковые, возвращает 1.
###Если строки разные и первая длиннее, возвращает 2.
###Если строки разные и вторая строка 'learn', возвращает 3.

def strings (str1, str2):
    if str1 == str2:
        print(1)
    elif len(str1) > len(str2):
        print(2)
    elif str2 == 'learn':
        print(3)

strings('sladjaslkfjals', 'dfd')