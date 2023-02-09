import telebot
from telebot import types

bot_token = '5998323861:AAHKezlx0R-1pcbjLEpd8zze84gytHy3yR8'
FILE_DIRECTORY = '/home/irina/PycharmProjects/autonivki'

bot = telebot.TeleBot(bot_token)


@bot.message_handler(commands=['easteregg'])
def start(message):

    # if message.text == 'Слава Україні':
    bot.send_message(message.from_user.id, text='slava', parse_mode='html')

