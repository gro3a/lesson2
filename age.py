###Попросить пользователя ввести возраст.
###По возрасту определить, чем он должен заниматься: учиться в детском саду, школе, ВУЗе или работать.
###Вывести занятие на экран.
age=int(input('Введите свой возраст:'))
if age <0:
    print('Столько не живут')
elif age <7:
    print('Воспитатель ждет тебя в дет.саду')
elif age <17:
    print('Дуй в школу. А то мамка заругает.')
elif age <=23:
    print('Учиться, учиться и еще раз учиться. Ленин. Не помню, кто сказал.')
else:
    print ('Работать, негры, солнце еще высоко.')