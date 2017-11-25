###Установите модуль ephem
###Добавьте в бота команду /planet, которая будет принимать на вход название планеты на английском.
###При помощи условного оператора if и ephem.constellation научите бота отвечать, в каком созвездии сегодня находится планета.

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import ephem
import datetime
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

    
def name_planet(bot,update):
    text_from_user = update.message.text
    logging.info(text_from_user)
    planet = str(text_from_user)
    result=''
    date=datetime.datetime.now()
    if planet == '/planet Earth':
        result = 'Я не знаю, загугли'
    elif planet == '/planet Mercury':
        result = ephem.constellation(ephem.Mercury(date))
    elif planet == '/planet Venus':
        result = ephem.constellation(ephem.Venus(date))
    elif planet == '/planet Mars':
        result = ephem.constellation(ephem.Mars(date))
    elif planet == '/planet Jupiter':
        result = ephem.constellation(ephem.Jupiter(date))
    elif planet == '/planet Saturn':
        result = ephem.constellation(ephem.Saturn(date))
    elif planet == '/planet Uranus':
        result = ephem.constellation(ephem.Uranus(date))
    elif planet == '/planet Neptune':
        result = ephem.constellation(ephem.Neptune(date))пше
    update.message.reply_text(result)

def greet_user(bot, update):
    text='Hi Dear'
    logging.info(text)
    update.message.reply_text(text)
def talk_to_me(bot, update):
    user_text = update.message.text 
    logging.info(user_text)
    update.message.reply_text(user_text)
def main():
    updater=Updater('436117084:AAEfswoQNjFX6ntmhEOXhKfdPJDcWCbSd-U')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet",name_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    updater.start_polling()
    updater.idle()
main()