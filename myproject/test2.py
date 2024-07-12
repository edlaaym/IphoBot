import telebot
from telebot import types

API_TOKEN = '7457498085:AAHds8W0MAHaoYl1hk248QstLs4AtLA58yQ'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton(text="О боте")
    button2 = types.KeyboardButton(text="Выбрать устройство")
    keyboard.add(button1, button2)
    bot.send_message(message.chat.id, "Выберите действие:", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == "О боте")
def about_bot(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton(text="Х")
    button2 = types.KeyboardButton(text="Х2")
    keyboard.add(button1, button2)
    bot.send_message(message.chat.id, "Выберите действие:", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == "Выбрать устройство")
def choose_device(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton(text="1")
    button2 = types.KeyboardButton(text="2")
    keyboard.add(button1, button2)
    bot.send_message(message.chat.id, "Выберите устройство:", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text in ["1", "2"])
def device_action(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button3 = types.KeyboardButton(text="3")
    button4 = types.KeyboardButton(text="4")
    keyboard.add(button3, button4)
    bot.send_message(message.chat.id, "Дополнительные действия:", reply_markup=keyboard)

bot.polling()