###Переписать функцию ask_user(), добавив обработку exception-ов
###Добавить перехват ctrl+C и прощание

answers = { 
'привет': "привет", 'как дела?':'Хорошо', 'пока':'пока'
}
def get_answer(qs,anwers):
    return answers.get(qs)

def ask_user(answers):
     while True:
        user=input('Скажи что-нибудь: ')
        answer = get_answer(user, answers)
        print(answer)

        if user == 'Пока':
            print('Пока!')
            break

def cut_error(ask_user):
    try:
        print(ask_user(answers))
    except KeyboardInterrupt:
        print ('Hasta la vista, baby!')

cut_error(ask_user)