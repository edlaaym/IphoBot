import telebot
from telebot import types

TOKEN = '7457498085:AAHds8W0MAHaoYl1hk248QstLs4AtLA58yQ'

bot = telebot.TeleBot(TOKEN)

ADMIN_USERNAME = 'edlaaym'
user_data = {}
admin_chat_id = None

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    btn1 = types.KeyboardButton('О боте')
    btn2 = types.KeyboardButton('Выбрать устройство')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, 'Выберите действие:', reply_markup=markup)

@bot.message_handler(commands=['setadmin'])
def set_admin(message):
    global admin_chat_id
    if message.from_user.username == ADMIN_USERNAME:
        admin_chat_id = message.chat.id
        bot.send_message(admin_chat_id, f'Теперь вы зарегистрированы как администратор бота. Вставьте в коде admin_chat_id = {979662097} и перезапустите бота')
    else:
        bot.send_message(message.chat.id, 'У вас нет прав на выполнение этой команды.')

@bot.message_handler(func=lambda message: message.text.lower() == 'о боте')
def about_bot(message):
    bot.send_message(message.chat.id, '<Бот создан для облегчения в создании объявлений. На данный момент бот создан в качестве дипломного проекта. По всем вопросам к @edlaaym>')

@bot.message_handler(func=lambda message: message.text.lower() == 'выбрать устройство')
def choose_device(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    btn1 = types.KeyboardButton('iPhone')
    btn2 = types.KeyboardButton('iPad')
    btn3 = types.KeyboardButton('AirPods')
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, 'Выберите тип устройства:', reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'iPhone')
def iphone(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    btn1 = types.KeyboardButton('iPhone 6')
    btn2 = types.KeyboardButton('iPhone 6 Plus')
    btn3 = types.KeyboardButton('iPhone 6s')
    btn4 = types.KeyboardButton('iPhone 6s Plus')
    btn5 = types.KeyboardButton('iPhone 7')
    btn6 = types.KeyboardButton('iPhone 7 Plus')
    btn7 = types.KeyboardButton('iPhone 8')
    btn8 = types.KeyboardButton('iPhone 8 Plus')
    btn9 = types.KeyboardButton('iPhone X')
    btn10 = types.KeyboardButton('iPhone Xs')й/ф
    btn11 = types.KeyboardButton('iPhone Xs Max')
    btn12 = types.KeyboardButton('iPhone XR')
    btn13 = types.KeyboardButton('iPhone 11')
    btn14 = types.KeyboardButton('iPhone 11 Pro')
    btn15 = types.KeyboardButton('iPhone 11 Pro Max')
    btn16 = types.KeyboardButton('iPhone 12')
    btn17 = types.KeyboardButton('iPhone 12 mini')
    btn18 = types.KeyboardButton('iPhone 12 Pro')
    btn19 = types.KeyboardButton('iPhone 12 Pro Max')
    btn20 = types.KeyboardButton('iPhone 13')
    btn21 = types.KeyboardButton('iPhone 13 mini')
    btn22 = types.KeyboardButton('iPhone 13 Pro')
    btn23 = types.KeyboardButton('iPhone 13 ProMax')
    btn24 = types.KeyboardButton('iPhone 14')
    btn25 = types.KeyboardButton('iPhone 14 Plus')
    btn26 = types.KeyboardButton('iPhone 14 Pro')
    btn27 = types.KeyboardButton('iPhone 14 Pro Max')
    btn28 = types.KeyboardButton('iPhone 15')
    btn29 = types.KeyboardButton('iPhone 15 Plus')
    btn30 = types.KeyboardButton('iPhone 15 Pro')
    btn31 = types.KeyboardButton('iPhone 15 Pro Max')
    btn32 = types.KeyboardButton('iPhone SE 2020')
    btn33 = types.KeyboardButton('iPhone SE 2022')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14, btn15, btn16, btn17, btn18, btn19, btn20, btn21, btn22, btn23, btn24, btn25, btn26, btn27, btn28, btn29, btn30, btn31, btn32, btn33)
    bot.send_message(message.chat.id, 'Выберите конкретную модель:', reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'iPhone 6')
def color_6(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    btn1 = types.KeyboardButton('Розовое золото')
    btn2 = types.KeyboardButton('Золотой')
    btn3 = types.KeyboardButton('Серебристый')
    btn4 = types.KeyboardButton('Серый космос')
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, 'Выберите цвет:', reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Розовое золото')
def memory_6(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    btn1 = types.KeyboardButton('16гб')
    btn2 = types.KeyboardButton('32гб')
    btn3 = types.KeyboardButton('64гб')
    btn4 = types.KeyboardButton('128гб')
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, 'Укажите объем памяти:', reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Золотой')
def memory_6_2(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    btn1 = types.KeyboardButton('16гб')
    btn2 = types.KeyboardButton('32гб')
    btn3 = types.KeyboardButton('64гб')
    btn4 = types.KeyboardButton('128гб')
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, 'Укажите объем памяти:', reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Серебристый')
def memory_6_3(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    btn1 = types.KeyboardButton('16гб')
    btn2 = types.KeyboardButton('32гб')
    btn3 = types.KeyboardButton('64гб')
    btn4 = types.KeyboardButton('128гб')
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, 'Укажите объем памяти:', reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Серый космос')
def memory_6_4(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    btn1 = types.KeyboardButton('16гб')
    btn2 = types.KeyboardButton('32гб')
    btn3 = types.KeyboardButton('64гб')
    btn4 = types.KeyboardButton('128гб')
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, 'Укажите объем памяти:', reply_markup=markup)


@bot.message_handler(func=lambda message: message.text in ['16гб', '32гб', '64гб', '128гб'])
def akb_condition(message):
    chat_id = message.chat.id
    user_data[chat_id]['akb'] = message.text
    bot.send_message(chat_id, 'Укажите состояние аккумулятора (пример: 87:')


@bot.message_handler(func=lambda message: message.chat.id in user_data and 'sim' not in user_data[message.chat.id])
def sim(message):
    chat_id = message.chat.id
    user_data[chat_id]['sim'] = message.text
    bot.send_message(chat_id, 'Укажите количество SIM (Пример: SIM + eSIM):')


@bot.message_handler(func=lambda message: message.chat.id in user_data and 'ac' not in user_data[message.chat.id])
def ac(message):
    chat_id = message.chat.id
    user_data[chat_id]['acondition'] = message.text
    bot.send_message(chat_id, 'Опишите внешнее состояние устройства:')


@bot.message_handler(func=lambda message: message.chat.id in user_data and 'wc' not in user_data[message.chat.id])
def wc(message):
    chat_id = message.chat.id
    user_data[chat_id]['wcondition'] = message.text
    bot.send_message(chat_id, 'Опишите рабочее состояние устройства:')


@bot.message_handler(func=lambda message: message.chat.id in user_data and 'name' not in user_data[message.chat.id])
def user_name(message):
    chat_id = message.chat.id
    user_data[chat_id]['name'] = message.text
    bot.send_message(chat_id, 'Укажите ваш "user name" (Пример: @example):')


    post = (f"Объявление:\n"
             f"Устройство: {user_data[chat_id]['iphone']}\n"
            f"Цвет: {user_data[chat_id]['color_6']}\n"
            f"Объем памяти: {user_data[chat_id]['memory_6']}\n"
            f"Объем памяти: {user_data[chat_id]['memory_6_2']}\n"
            f"Объем памяти: {user_data[chat_id]['memory_6_3']}\n"
            f"Объем памяти: {user_data[chat_id]['memory_6_4']}\n"
            f"Состояние аккумулятора: {user_data[chat_id]['akb']}\n"
            f"Количество SIM: {user_data[chat_id]['sim']}\n"
            f"Внешнее остояние: {user_data[chat_id]['acondition']}\n"
            f"Рабочее остояние: {user_data[chat_id]['wcondition']}\n"
            f"Продает: {user_data[chat_id]['name']}\n")

    bot.send_message(chat_id, post)

if admin_chat_id:
        bot.send_message(admin_chat_id,
                         f"Новое объявление от {message.from_user.username}:\n\n{post}")

bot.polling(none_stop=True)
