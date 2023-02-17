import telebot
from telebot import types
from os import path
import config

FILE_DIRECTORY = path.dirname(path.abspath('autonivki'))

bot = telebot.TeleBot(config.bot_token)


def main_menu():
    customer_markup = types.ReplyKeyboardMarkup(True)
    customer_markup.row('Світло є чи нема? bot')
    customer_markup.row('Комерція в ЖК', 'Чати ЖК')
    customer_markup.row('Пошта, поштомати', 'Контакти ЖЕК')
    return customer_markup


def commerce():
    customer_markup = types.ReplyKeyboardMarkup(True)
    customer_markup.row('Їжа та кава')
    customer_markup.row("Краса та здоров'я")
    customer_markup.row('Все інше (категорію придумайте самі)')
    return customer_markup


def chats_menu():
    customer_markup = types.ReplyKeyboardMarkup(True)
    customer_markup.row('Дошки оголошень', 'Помийка офіційна', 'Затишний підвал')
    customer_markup.row('Нявки і гавки Парк', 'Веселий парк', 'Адміни будинків')
    customer_markup.row('Головне меню')
    return customer_markup


def easter(message):
    if message.text.lower() == 'слава україні':
        bot.send_message(message.from_user.id, text='Героям слава! 🇺🇦', parse_mode='html')
    elif message.text.lower() == 'слава нації':
        bot.send_message(message.from_user.id, text='Смерть ворогам!', parse_mode='html')
    elif message.text.lower() == 'україна':
        bot.send_message(message.from_user.id, text='Понад усе!', parse_mode='html')
    elif message.text.lower() == 'путін':
        bot.send_message(message.from_user.id, text='Хуйло!', parse_mode='html')
    elif message.text.lower() == 'ой у лузі червона калина':
        bot.send_message(message.from_user.id, text='пооооохилиласяяяяя....', parse_mode='html')
    elif message.text.lower() == 'русня':
        bot.send_message(message.from_user.id, text='п*дараси 😡', parse_mode='html')
    elif message.text.lower() == 'русні':
        bot.send_message(message.from_user.id, text='п*зда 😁', parse_mode='html')


def send_message(chat_id, message):
    bot.send_message(chat_id, text=message)


@bot.message_handler(commands=['send'])
def send_message(message):
    bot.send_message(381547535, text='test')


@bot.message_handler(commands=['mainmenu'])
def mainmenu_button(message):
    main_menu()
    bot.send_message(message.chat.id, text='Повернення до головного меню', reply_markup=main_menu())


@bot.message_handler(commands=['start'])
def start(message):
    main_menu()
    bot.send_message(message.chat.id, 'Вітаю, {0.first_name}'.format(message.from_user), reply_markup=main_menu())


@bot.message_handler(content_types=['text'])
def handle_text(message):
    easter(message)
    if message.text == 'Світло є чи нема? bot':
        light_bot = 'Бот світла нашого ЖК \n' \
                    'https://t.me/nivki_park_e_svitlo'
        image_light = open(FILE_DIRECTORY + '/photo/dtek.jpg', 'rb')
        bot.send_photo(message.from_user.id, image_light)
        bot.send_message(message.from_user.id,  text=light_bot, parse_mode='html')
    elif message.text == 'Чати ЖК':
        chats_menu()
        bot.send_message(message.chat.id, text='Чати ЖК', reply_markup=chats_menu())
    elif message.text == 'Помийка офіційна':
        text = 'Заходь, якщо сміливий, але потім не плач\n' \
               'https://t.me/nivkipark'
        bot.send_message(message.from_user.id, text=text, parse_mode='html')
    elif message.text == 'Веселий парк':
        text = 'Чат для івентів, ярмарок та будь-якої активності\n' \
               'https://t.me/+fUwKp1_4XuhiMzI6'
        bot.send_message(message.from_user.id, text=text, parse_mode='html')
    elif message.text == 'Адміни будинків':
        text = 'Щоб долучитися до чатів власників квартир Вашого будинку та будинків всього ЖК, ' \
            'звертайтеся до адмінів чатів у телеграмі :\n' \
            '1 буд: @Yev7777 \n2 буд: @Olena_Maistrenko \n3 буд: @RNatalii \n4 буд: @AnnaZaya45\n'\
            '5 буд: @BuldozeR_23 \n6 буд: @alison2009 \n7 буд: @sergeym0307 \n8 буд: @am1335\n'\
            "9 буд: @Catterrin \n10 буд: @luzaner \n11 буд: @Tetiana_Kurylenko \n12 буд : @passst'et"\
            'Для приєднання до чату необхідно надіслати адміну чату в особисті повідомлення фото першої сторінки ' \
            'договору з ІГБ або зустрітися особисто, щоб надати документ-підтвердження права власності. ' \
            'Вдячні за співпрацю.'
        bot.send_message(message.from_user.id, text=text, parse_mode='html')
    elif message.text == 'Нявки і гавки Парк':
        bot.send_message(message.from_user.id, text='https://t.me/+WKxiW13PG3D-UzHp', parse_mode='html')
    elif message.text == 'Затишний підвал':
        text = 'Чат для тих, хто лишився в ЖК під час війни. Власники та орендарі\n' \
               'https://t.me/c/1251627268/3807'
        bot.send_message(message.from_user.id, text=text, parse_mode='html')
    elif message.text == 'Дошки оголошень':
        text1 = 'Дошка оголошень ЖК. Віддам/продам за ціною нижче ринкової \n' \
                'https://t.me/+vo-W_N_TzX1iYmYy \n\n' \
                'Комерція, яка знаходиться в ЖК та поряд \n' \
                'https://t.me/+f_-wG5NaAUE0NDAy \n\n'
        bot.send_message(message.from_user.id,  text=text1, parse_mode='html')

    elif message.text == 'Контакти ЖЕК':
        telephones = '<b>Список працівників ЖК "Нивки Парк"</b> \n' \
                'Ігор Іванович (головний інженер) +380632699518 \n' \
                'Погребняк Інна Володимірівна (майстер) +380932973064 \n' \
                'Начальник охорони +380632485290 \n\n' \
                'Сантехнік Олександр +380682030921 \n' \
                'Сантехнік Вячеслав +380973993157 \n' \
                'Сантехнік Роман +380672923020 \n' \
                'Сантехнік Олег +380507333067 \n'\
                'Сантехнік Юрій +380968132186 \n' \
                'Бухгалтерія (вайбер) +380630315573 \n\n' \
                'Ключниця Олена +380674672523 \n' \
                'Ключниця Валя +380973925566 \n' \
                'Відділ продажу +380671134169 \n' \
                'Рекламація Руслан +380932255635 \n' \
                'Секретар ІнвестБудГаличина +380630315232 \n' \

        bot.send_message(message.from_user.id, text=telephones, parse_mode='html')

    elif message.text == 'Авто заявки (тестування)':
        auto_markup = types.ReplyKeyboardMarkup(True)
        auto_markup.row('Додати своє авто', 'Підписатись на авто')
        auto_markup.row('Написати власнику', 'Почетний ЛОСЬ')
        auto_markup.row('Головне меню')

        auto_start_text = 'В цьому розділі можна повідомити власника авто про різні ситуації. Наприклад: \n' \
                          '👉коли авто заважає проїзду або неправильно припарковане \n' \
                          '👉коли авто має відчинене вікно або ввімкнені фари \n' \
                          '👉стали свідком ДТП чи іншої ситуації \n\n' \
                          'Зробимо спілкування з водіями-сусідами легшим!'

        bot.send_message(message.chat.id, text=auto_start_text, reply_markup=auto_markup)

    elif message.text == 'Комерція в ЖК':
        commerce()
        bot.send_message(message.chat.id, text='Комерція на території ЖК', reply_markup=commerce())

    elif message.text == 'Їжа та кава':
        text = 'Йде збір інформації. Для додавання своєї комерції - пишіть адміну бота'
        bot.send_message(message.from_user.id, text=text, parse_mode='html')
    elif message.text == "Краса та здоров'я":
        text = 'Йде збір інформації. Для додавання своєї комерції - пишіть адміну бота'
        bot.send_message(message.from_user.id, text=text, parse_mode='html')
    elif message.text == 'Все інше (категорію придумайте самі)':
        text = 'Йде збір інформації. Для додавання своєї комерції - пишіть адміну бота'
        bot.send_message(message.from_user.id, text=text, parse_mode='html')

    elif message.text == 'Головне меню':
        main_menu()

        bot.send_message(message.chat.id, text='Головне меню', reply_markup=main_menu())

    elif message.text == 'Пошта, поштомати':
        post_text = 'Відділення Укрпошти <b>03117</b> \n' \
                    'Проспект Перемоги 67Г (3й будинок)\n' \
                    'Графік роботи: \n' \
                    'Вт-Пт: 09:00-18:00 \n' \
                    'Сб: 10:00-17:00 \n' \
                    'Нд, Пн - вихідний \n\n' \
                    'Поштомати Нової Пошти <b>21963, 31890</b>\n' \
                    'Шоурум "Здорова вода"\n' \
                    'Проспект Перемоги 67В (4 будинок)\n\n' \
                    '<b>Meest</b> \n' \
                    'Проспект Перемоги 65б (6й будинок)\n' \
                    'Забирати у відділенні Розетки \n'

        bot.send_message(message.chat.id, text=post_text, parse_mode='html')

    elif message.text == 'Почетний ЛОСЬ':
        post_text = 'Сьогодні всі пиріжечки правильно запарковані.'
        # image_light = open(FILE_DIRECTORY + '/photo/los1.jpg', 'rb')
        # bot.send_photo(message.from_user.id, image_light)
        bot.send_message(message.chat.id, text=post_text, parse_mode='html')
        print(message.chat.id)


@bot.message_handler(content_types=['text'])
def handle_auto(message):
    if message.text == 'Почетний ЛОСЬ':
        post_text = 'Сьогодні Почетний ЛОСЬ: АК 3453 КВ Toyota (чорний колір)'
        bot.send_message(message.chat.id, text=post_text, parse_mode='html')
    elif message.text == '1':
        bot.send_message(message.chat.id, text='1', parse_mode='html')
#     if message.text == 'Додати своє авто1':
#         text_first = 'Введіть номерний знак авто формату АА0000АК'
#         bot.send_message(message.chat.id, text=text_first, parse_mode='html')
#         pass
#
#
# @bot.callback_query_handler(func=lambda call:True)
# def answer(call):
#     if call.data == 'y':
#         pass


bot.polling(none_stop=True)
