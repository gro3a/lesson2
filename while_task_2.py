### Перепишите предыдущий пример в виде функции find_person(name), которая ищет имя в списке.
from copy import copy
names=["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
name=input('Введите имя: ')
list_to_change=copy(names)

def find_person (name, list_to_change):
    result=''
    while list_to_change:
        if list_to_change.pop() == name:
            result = name +' нашелся: '+ str(len(list_to_change)+1)
            break
        else:
            result = ' Тут таких нет'
    return result
    
print(find_person(name,list_to_change))