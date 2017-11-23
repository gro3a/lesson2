###При помощи функции get_answer() отвечать на вопросы пользователя в ask_user(), пока он не скажет “Пока!”

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

ask_user(answers)