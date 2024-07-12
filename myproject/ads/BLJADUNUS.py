from pyexpat import model

import telebot
from telebot import types
from enum import Enum
from .models import Ad

TOKEN = '7457498085:AAHds8W0MAHaoYl1hk248QstLs4AtLA58yQ'

ADMIN_USERNAME = 'edlaaym'
user_data = {}
user_states = {}

bot = telebot.TeleBot(TOKEN)
admin_chat_id = None


# Итак, здесь первое основное отличие от вашего исходного кода
# Мне кажется, нужно не внутри функций прописывать названия айфонов, цветов и прочего,
# а заранее можно сделать класс, который хранит в себе все возможные варианты
# Тогда, если захотите например новый цвет добавить, то ну нужно будет по всему коду искать где и как он юзается
# нужно будет только в классе переменную с нужным значением задать

class UserState(Enum):
    # конкретно этот класс я решила добавить по следующим причинам:
    # У вас в коде были вот такие штуки:
    # @bot.message_handler(func=lambda message: message.chat.id in user_data and 'acondition' not in user_data[message.chat.id])
    # def ac(message):
    # ...
    # Это, наверное, рабочий вариант, но он сложный для понимания и если что-то сломается (или нужно будет добавить),
    # то разбираться с таким кодом будет проблематично. Поэтому я вынесла просто все возможные состояния юзера
    # в этот класс, каждому состоянию соответствует свой номер, так что этим пользоваться проще и понятнее

    CHOOSE_DEVICE = 1
    CHOOSE_MODEL = 2
    CHOOSE_COLOR = 3
    CHOOSE_MEMORY = 4
    INPUT_AKB = 5
    INPUT_SIM = 6
    INPUT_ACONDITION = 7
    INPUT_WCONDITION = 8

class DeviceType(Enum):
    IPHONE = 'iPhone'
    IPAD = 'iPad'
    AIRPODS = 'AirPods'

class IPhoneModel(Enum):
    IPHONE_6 = 'iPhone 6'
    IPHONE_6_PLUS = 'iPhone 6 Plus'
    IPHONE_6S = 'iPhone 6s'
    IPHONE_6S_PLUS = 'iPhone 6s Plus'
    PHONE_7 = 'iPhone 7'
    IPHONE_7_PLUS = 'iPhone 7 Plus'
    IPHONE_8 = 'iPhone 8'
    IPHONE_8_PLUS = 'iPhone 8 Plus'
    IPHONE_X = 'iPhone X'
    IPHONE_XS = 'iPhone Xs'
    IPHONE_XS_MAX = 'iPhone Xs Max'
    IPHONE_XR = 'iPhone XR'
    IPHONE_11 = 'iPhone 11'
    IPHONE_11_PRO = 'iPhone 11 Pro'
    IPHONE_11_PRO_MAX = 'iPhone 11 Pro Max'
    IPHONE_12 = 'iPhone 12'
    IPHONE_12_PRO = 'iPhone 12 Pro'
    IPHONE_12_PRO_MAX = 'iPhone 12 Pro Max'
    IPHONE_12_MINI = 'iPhone 12 mini'
    IPHONE_13 = 'iPhone 13'
    IPHONE_13_PRO = 'iPhone 13 Pro'
    IPHONE_13_PRO_MAX = 'iPhone 13 Pro Max'
    IPHONE_13_MINI = 'iPhone 13 mini'
    IPHONE_14 = 'iPhone 14'
    IPHONE_14_PRO = 'iPhone 14 Pro'
    IPHONE_14_PRO_MAX = 'iPhone 14 Pro Max'
    IPHONE_14_PLUS = 'iPhone 14 PLUS'
    IPHONE_15 = 'iPhone 15'
    IPHONE_15_PRO = 'iPhone 15'
    IPHONE_15_PRO_MAX = 'iPhone 15'
    IPHONE_15_PLUS = 'iPhone 15'
    IPHONE_SE_2 = 'iPhone SE (2-го поколения)'
    IPHONE_SE_3 = 'iPhone SE (3-го поколения)'
    # Добавьте остальные модели

class IPhoneColor6(Enum):
    GOLD = 'Золотой'
    SILVER = 'Серебристый'
    SPACE_GRAY = 'Серый космос'

class IPhoneColor6plus(Enum):
    GOLD = 'Золотой'
    SILVER = 'Серебристый'
    SPACE_GRAY = '"Серый космос"'

class IPhoneColor6s(Enum):
    ROSE_GOLD = 'Розовое золото'
    GOLD = 'Золотой'
    SILVER = 'Серебристый'
    SPACE_GRAY = 'Серый космос'

class IPhoneColor6splus(Enum):
    ROSE_GOLD = 'Розовое золото'
    GOLD = 'Золотой'
    SILVER = 'Серебристый'
    SPACE_GRAY = 'Серый космос'

class IPhoneColor7(Enum):
    GOLD = 'Золотой'
    SILVER = 'Серебристый'
    SPACE_GRAY = 'Серый космос'
    ROSE_GOLD = 'Розовое золото'
    BLACK = 'Черный'
    BLACK_ONIX = 'Черный оникс'
    RED = '(PRODUCT)RED'

class IPhoneColor7plus(Enum):
    GOLD = 'Золотой'
    SILVER = 'Серебристый'
    SPACE_GRAY = 'Серый космос'
    ROSE_GOLD = 'Розовое золото'
    BLACK = 'Черный'
    BLACK_ONIX = 'Черный оникс'
    RED = '(PRODUCT)RED'

class IPhoneColor8(Enum):
    GOLD = 'Золотой'
    SILVER = 'Серебристый'
    SPACE_GRAY = 'Серый космос'
    RED = '(PRODUCT)RED'

class IPhoneColor8plus(Enum):
    GOLD = 'Золотой'
    SILVER = 'Серебристый'
    SPACE_GRAY = 'Серый космос'
    RED = '(PRODUCT)RED'

class IPhoneColorX(Enum):
    SILVER = 'Серебристый'
    SPACE_GRAY = 'Серый космос'


class IPhoneColorXs(Enum):
    GOLD = 'Золотой'
    SILVER = 'Серебристый'
    SPACE_GRAY = 'Серый космос'

class IPhoneColorXsMax(Enum):
    GOLD = 'Золотой'
    SILVER = 'Серебристый'
    SPACE_GRAY = 'Серый космос'

class IPhoneColorXR(Enum):
    RED = '(PRODUCT)RED'
    BLACK = 'Черный'
    WHITE = 'Белый'
    KORALL = 'Коралловый'
    YELLOW = 'Желтый'
    BLUE = 'Синий'

class IPhoneColor11(Enum):
    RED = '(PRODUCT)RED'
    BLACK = 'Черный'
    WHITE = 'Белый'
    YELLOW = 'Желтый'
    PURPLE = 'Фиолетовый'
    GREEN = 'Зелёный'

class IPhoneColor11Pro(Enum):
    GOLD = 'Золотой'
    SILVER = 'Серебристый'
    SPACE_GRAY = 'Серый космос'
    DARK_GREEN = 'Тёмно-Зелёный'

class IPhoneColor11ProMax(Enum):
    GOLD = 'Золотой'
    SILVER = 'Серебристый'
    SPACE_GRAY = 'Серый космос'
    DARK_GREEN = 'Тёмно-Зелёный'

class IPhoneColor12(Enum):
    RED = '(PRODUCT)RED'
    BLACK = 'Черный'
    WHITE = 'Белый'
    BLUE = 'Синий'
    PURPLE = 'Фиолетовый'
    GREEN = 'Зелёный'

class IPhoneColor12mini(Enum):
    RED = '(PRODUCT)RED'
    BLACK = 'Черный'
    WHITE = 'Белый'
    BLUE = 'Синий'
    PURPLE = 'Фиолетовый'
    GREEN = 'Зелёный'

class IPhoneColor12Pro(Enum):
    GOLD = 'Золотой'
    SILVER = 'Серебристый'
    GRAPHIT = 'Графитовый'
    OCEAN_BLUE = 'Тихоокеанский синий'

class IPhoneColor12ProMax(Enum):
    GOLD = 'Золотой'
    SILVER = 'Серебристый'
    GRAPHIT = 'Графитовый'
    OCEAN_BLUE = 'Тихоокеанский синий'

class IPhoneColor13(Enum):
    RED = '(PRODUCT)RED'
    DARK_NIGHT = 'Тёмная ночь'
    STAR = 'Сияющая звезда'
    BLUE = 'Синий'
    PINK = 'Розовый'

class IPhoneColor13Pro(Enum):
    GOLD = 'Золотой'
    SILVER = 'Серебристый'
    GRAPHIT = 'Графитовый'
    SKY_BLUE = 'Небесно-голубой'

class IPhoneColor13ProMax(Enum):
    GOLD = 'Золотой'
    SILVER = 'Серебристый'
    GRAPHIT = 'Графитовый'
    SKY_BLUE = 'Небесно-голубой'

class IPhoneColor13mini(Enum):
    RED = '(PRODUCT)RED'
    DARK_NIGHT = 'Тёмная ночь'
    STAR = 'Сияющая звезда'
    BLUE = 'Синий'
    PINK = 'Розовый'
    GREEN = 'Зелёный'

class IPhoneColor14(Enum):
    RED = '(PRODUCT)RED'
    DARK_NIGHT = 'Тёмная ночь'
    STAR = 'Сияющая звезда'
    BLUE = 'Синий'
    YELLOW = 'Желтый'
    PURPLE = 'Фиолетовый'

class IPhoneColor14PLUS(Enum):
    RED = '(PRODUCT)RED'
    DARK_NIGHT = 'Тёмная ночь'
    STAR = 'Сияющая звезда'
    BLUE = 'Синий'
    YELLOW = 'Желтый'
    PURPLE = 'Фиолетовый'

class IPhoneColor14Pro(Enum):
    GOLD = 'Золотой'
    SILVER = 'Серебристый'
    BLACK = 'Чёрный'
    PURPLE = 'Фиолетовый'

class IPhoneColor14ProMax(Enum):
    GOLD = 'Золотой'
    SILVER = 'Серебристый'
    BLACK = 'Чёрный'
    PURPLE = 'Фиолетовый'

class IPhoneColor15(Enum):
    BLACK = 'Чёрный'
    BLUE = 'Голубой'
    GREEN = 'Зелёный'
    YELLOW = 'Желтый'
    PINK = 'Розовый'

class IPhoneColor15PLUS(Enum):
    BLACK = 'Чёрный'
    BLUE = 'Голубой'
    GREEN = 'Зелёный'
    YELLOW = 'Желтый'
    PINK = 'Розовый'

class IPhoneColor15Pro(Enum):
    BLACK = 'Чёрный'
    WHITE = 'Белый'
    BLUE = 'Синий'
    NATURAL_TITANIUM = 'Натуральный титан'

class IPhoneColor15ProMax(Enum):
    BLACK = 'Чёрный'
    WHITE = 'Белый'
    BLUE = 'Синий'
    NATURAL_TITANIUM = 'Натуральный титан'

class IPhoneColorSE2(Enum):
    BLACK = 'Черный'
    WHITE = 'Белый'

class IPhoneColorSE3(Enum):
    BLACK = 'Черный'
    WHITE = 'Белый'
    RED = '(PRODUCT)RED'

class MemoryOption6(Enum):
    GB_16 = '16гб'
    GB_32 = '32гб'
    GB_64 = '64гб'
    GB_128 = '128гб'

#КЛАССЫ С ПАМАТЬЮ КАЖДОЙ МОДЕЛИ

class MemoryOption6Plus(Enum):
    GB_16 = '16гб'
    GB_64 = '64гб'
    GB_128 = '128гб'

class MemoryOption6s(Enum):
    GB_16 = '16гб'
    GB_32 = '32гб'
    GB_64 = '64гб'
    GB_128 = '128гб'

class MemoryOption6sPlus(Enum):
    GB_16 = '16гб'
    GB_32 = '32гб'
    GB_64 = '64гб'
    GB_128 = '128гб'

class MemoryOption7(Enum):
    GB_32 = '32гб'
    GB_128 = '128гб'
    GB_256 = '256гб'

class MemoryOption7Plus(Enum):
    GB_32 = '32гб'
    GB_128 = '128гб'
    GB_256 = '256гб'

class MemoryOption8(Enum):
    GB_64 = '64гб'
    GB_128 = '128гб'
    GB_256 = '256гб'

class MemoryOption8Plus(Enum):
    GB_64 = '64гб'
    GB_128 = '128гб'
    GB_256 = '256гб'

class MemoryOptionX(Enum):
    GB_64 = '64гб'
    GB_256 = '256гб'

class MemoryOptionXS(Enum):
    GB_64 = '64гб'
    GB_256 = '256гб'
    GB_512 = '512гб'

class MemoryOptionXSMax(Enum):
    GB_64 = '64гб'
    GB_256 = '256гб'
    GB_512 = '512гб'

class MemoryOptionXR(Enum):
    GB_64 = '64гб'
    GB_256 = '256гб'
    GB_512 = '512гб'

class MemoryOption11(Enum):
    GB_64 = '64гб'
    GB_128 = '128гб'
    GB_256 = '256гб'

class MemoryOption11Pro(Enum):
    GB_64 = '64гб'
    GB_256 = '256гб'
    GB_512 = '512гб'

class MemoryOption11ProMax(Enum):
    GB_64 = '64гб'
    GB_256 = '256гб'
    GB_512 = '512гб'

class MemoryOption12(Enum):
    GB_64 = '64гб'
    GB_128 = '128гб'
    GB_256 = '256гб'

class MemoryOption12mini(Enum):
    GB_64 = '64гб'
    GB_128 = '128гб'
    GB_256 = '256гб'

class MemoryOption12Pro(Enum):
    GB_128 = '128гб'
    GB_256 = '256гб'
    GB_512 = '512гб'

class MemoryOption12ProMax(Enum):
    GB_128 = '128гб'
    GB_256 = '256гб'
    GB_512 = '512гб'

class MemoryOption13(Enum):
    GB_128 = '128гб'
    GB_256 = '256гб'
    GB_512 = '512гб'

class MemoryOption13mini(Enum):
    GB_128 = '128гб'
    GB_256 = '256гб'
    GB_512 = '512гб'

class MemoryOption13Pro(Enum):
    GB_128 = '128гб'
    GB_256 = '256гб'
    GB_512 = '512гб'
    TB_1 = '1тб'

class MemoryOption13ProMax(Enum):
    GB_128 = '128гб'
    GB_256 = '256гб'
    GB_512 = '512гб'
    TB_1 = '1тб'

class MemoryOption14(Enum):
    GB_128 = '128гб'
    GB_256 = '256гб'
    GB_512 = '512гб'

class MemoryOption14Plus(Enum):
    GB_128 = '128гб'
    GB_256 = '256гб'
    GB_512 = '512гб'

class MemoryOption14Pro(Enum):
    GB_128 = '128гб'
    GB_256 = '256гб'
    GB_512 = '512гб'
    TB_1 = '1тб'

class MemoryOption14ProMax(Enum):
    GB_128 = '128гб'
    GB_256 = '256гб'
    GB_512 = '512гб'
    TB_1 = '1тб'

class MemoryOption15(Enum):
    GB_128 = '128гб'
    GB_256 = '256гб'
    GB_512 = '512гб'

class MemoryOption15Plus(Enum):
    GB_128 = '128гб'
    GB_256 = '256гб'
    GB_512 = '512гб'

class MemoryOption15Pro(Enum):
    GB_128 = '128гб'
    GB_256 = '256гб'
    GB_512 = '512гб'
    TB_1 = '1тб'

class MemoryOption15ProMax(Enum):
    GB_128 = '128гб'
    GB_256 = '256гб'
    GB_512 = '512гб'
    TB_1 = '1тб'

class MemoryOptionSE2(Enum):
    GB_64 = '64'
    GB_128 = '128'
    GB_256 = '256гб'

class MemoryOptionSE3(Enum):
    GB_64 = '64'
    GB_128 = '128'
    GB_256 = '256гб'

def show_main_menu(chat_id):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    btn1 = types.KeyboardButton('О боте')
    btn2 = types.KeyboardButton('Выбрать устройство')
    markup.add(btn1, btn2)
    bot.send_message(chat_id, 'Выберите действие:', reply_markup=markup)

def set_user_state(chat_id, state):
    # здесь нужен иф, потому что ван нужна такая структура данных:
    # user_data = {
    #   'UserChatId_1': {
    #       'device': 'iPhone 6',
    #       'color': 'Gray',
    #       ...
    #   }
    # }
    # Но сразу словарь в словаре сделать нельзя. Надо проверить: если еще нет словаря по нашему юзеру, то мы его сделаем
    # и добавляем туда state как метку того состояния, в котором юзер находится сейчас

    if chat_id not in user_data:
        user_data[chat_id] = {}
    user_data[chat_id]['state'] = state

def get_user_state(chat_id):
    return user_data.get(chat_id, {}).get('state')

def create_keyboard(options):
    # эта функция нужна, чтобы передать в нее все возможные варианты кнопок, а она сделает клавиатуру с такими кнопками
    # это удобнее, чем каждый раз городить кучу кода для каждой новой клавиатуры с кнопками
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    for option in options:
        markup.add(types.KeyboardButton(option.value))
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    show_main_menu(message.chat.id)

@bot.message_handler(commands=['setadmin'])
def set_admin(message):
    global admin_chat_id
    if message.from_user.username == ADMIN_USERNAME:
        admin_chat_id = message.chat.id
        bot.send_message(admin_chat_id, 'Теперь вы зарегистрированы как администратор бота.')
    else:
        bot.send_message(message.chat.id, 'У вас нет прав на выполнение этой команды.')

@bot.message_handler(func=lambda message: message.text.lower() == 'о боте')
def about_bot(message):
    bot.send_message(message.chat.id, 'Бот создан для облегчения создания объявлений. На данный момент бот создан в качестве дипломного проекта. По всем вопросам к @edlaaym.')

@bot.message_handler(func=lambda message: message.text.lower() == 'выбрать устройство')
def choose_device(message):
    options = [DeviceType.IPHONE]
    # ну вот как раз - мы сделали список со всеми возможными вариантами кнопок и вызвали функцию для создания такой клавы
    bot.send_message(message.chat.id, 'Выберите тип устройства:', reply_markup=create_keyboard(options))
    set_user_state(message.chat.id, UserState.CHOOSE_DEVICE)


# теперь условия срабатывания функций выглядят проще: если юзер находится в состоянии выбора девайса -
# мы обрабатываем выбор девайса и переходим в состояние выбора модели.
# Название самой функции соответствует тому состоянию, В КОТОРОЕ мы переходим
@bot.message_handler(func=lambda message: get_user_state(message.chat.id) == UserState.CHOOSE_DEVICE)
def choose_model(message):
    try:
        device = DeviceType(message.text)
        user_data[message.chat.id]['device'] = device
        set_user_state(message.chat.id, UserState.CHOOSE_MODEL)
        models = {
            DeviceType.IPHONE: list(IPhoneModel),
            DeviceType.IPAD: [],  # Добавьте модели iPad
            DeviceType.AIRPODS: []  # Добавьте модели AirPods
        }
        bot.send_message(message.chat.id, 'Выберите модель:', reply_markup=create_keyboard(models[device]))
    except ValueError:
        bot.send_message(message.chat.id, 'Пожалуйста, выберите устройство из предложенного списка.')

@bot.message_handler(func=lambda message: get_user_state(message.chat.id) == UserState.CHOOSE_MODEL)
def choose_color(message):
    try:
        model = IPhoneModel(message.text)
        user_data[message.chat.id]['model'] = model
        set_user_state(message.chat.id, UserState.CHOOSE_COLOR)
        if user_data[message.chat.id]['model'] == IPhoneModel.IPHONE_6:
            colors = list(IPhoneColor6)
        elif user_data[message.chat.id]['model'] == IPhoneModel.IPHONE_6_PLUS:
            colors = list(IPhoneColor6plus)
        elif user_data[message.chat.id]['model'] == IPhoneModel.IPHONE_6S:
            colors = list(IPhoneColor6s)
        elif user_data[message.chat.id]['model'] == IPhoneModel.IPHONE_6S_PLUS:
            colors = list(IPhoneColor6splus)
        elif user_data[message.chat.id]['model'] == IPhoneModel.PHONE_7:
            colors = list(IPhoneColor7)
        elif user_data[message.chat.id]['model'] == IPhoneModel.IPHONE_7_PLUS:
            colors = list(IPhoneColor7plus)
        elif user_data[message.chat.id]['model'] == IPhoneModel.IPHONE_8:
            colors = list(IPhoneColor8)
        elif user_data[message.chat.id]['model'] == IPhoneModel.IPHONE_8_PLUS:
            colors = list(IPhoneColor8plus)
        elif user_data[message.chat.id]['model'] == IPhoneModel.IPHONE_X:
            colors = list(IPhoneColorX)
        elif user_data[message.chat.id]['model'] == IPhoneModel.IPHONE_XS:
            colors = list(IPhoneColorXs)
        elif user_data[message.chat.id]['model'] == IPhoneModel.IPHONE_XS_MAX:
            colors = list(IPhoneColorXsMax)
        elif user_data[message.chat.id]['model'] == IPhoneModel.IPHONE_XR:
            colors = list(IPhoneColorXR)
        elif user_data[message.chat.id]['model'] == IPhoneModel.IPHONE_11:
            colors = list(IPhoneColor11)
        elif user_data[message.chat.id]['model'] == IPhoneModel.IPHONE_11_PRO:
            colors = list(IPhoneColor11Pro)
        elif user_data[message.chat.id]['model'] == IPhoneModel.IPHONE_11_PRO_MAX:
            colors = list(IPhoneColor11ProMax)
        elif user_data[message.chat.id]['model'] == IPhoneModel.IPHONE_12:
            colors = list(IPhoneColor12)
        elif user_data[message.chat.id]['model'] == IPhoneModel.IPHONE_12_PRO:
            colors = list(IPhoneColor12Pro)
        elif user_data[message.chat.id]['model'] == IPhoneModel.IPHONE_12_PRO_MAX:
            colors = list(IPhoneColor12ProMax)
        elif user_data[message.chat.id]['model'] == IPhoneModel.IPHONE_12_MINI:
            colors = list(IPhoneColor12mini)
        elif user_data[message.chat.id]['model'] == IPhoneModel.IPHONE_13:
            colors = list(IPhoneColor13)
        elif user_data[message.chat.id]['model'] == IPhoneModel.IPHONE_13_PRO:
            colors = list(IPhoneColor13Pro)
        elif user_data[message.chat.id]['model'] == IPhoneModel.IPHONE_13_PRO_MAX:
            colors = list(IPhoneColor13ProMax)
        elif user_data[message.chat.id]['model'] == IPhoneModel.IPHONE_13_MINI:
            colors = list(IPhoneColor13mini)
        elif user_data[message.chat.id]['model'] == IPhoneModel.IPHONE_14:
            colors = list(IPhoneColor14)
        elif user_data[message.chat.id]['model'] == IPhoneModel.IPHONE_14_PRO:
            colors = list(IPhoneColor14Pro)
        elif user_data[message.chat.id]['model'] == IPhoneModel.IPHONE_14_PRO_MAX:
            colors = list(IPhoneColor14ProMax)
        elif user_data[message.chat.id]['model'] == IPhoneModel.IPHONE_14_PLUS:
            colors = list(IPhoneColor14PLUS)
        elif user_data[message.chat.id]['model'] == IPhoneModel.IPHONE_15:
            colors = list(IPhoneColor15)
        elif user_data[message.chat.id]['model'] == IPhoneModel.IPHONE_15_PRO:
            colors = list(IPhoneColor15Pro)
        elif user_data[message.chat.id]['model'] == IPhoneModel.IPHONE_15_PRO_MAX:
            colors = list(IPhoneColor15ProMax)
        elif user_data[message.chat.id]['model'] == IPhoneModel.IPHONE_15_PLUS:
            colors = list(IPhoneColor15PLUS)
        elif user_data[message.chat.id]['model'] == IPhoneModel.IPHONE_SE_2:
            colors = list(IPhoneColorSE2)
        elif user_data[message.chat.id]['model'] == IPhoneModel.IPHONE_SE_3:
            colors = list(IPhoneColorSE3)
        print(colors)
        user_data[message.chat.id]['color'] = colors
        bot.send_message(message.chat.id, 'Выберите цвет:', reply_markup=create_keyboard(colors))
    except ValueError:
        bot.send_message(message.chat.id, 'Пожалуйста, выберите модель из предложенного списка.')
        print(user_data[message.chat.id]['model'])

@bot.message_handler(func=lambda message: get_user_state(message.chat.id) == UserState.CHOOSE_COLOR)
def choose_memory(message):
    try:
        color = user_data[message.chat.id]['color'][user_data[message.chat.id]['state'].value]
        user_data[message.chat.id]['color'] = color
        set_user_state(message.chat.id, UserState.CHOOSE_MEMORY)
        if user_data[message.chat.id]['color'] == IPhoneColor6.GOLD:
            memory_options = list(MemoryOption6)
        elif user_data[message.chat.id]['color'] == IPhoneColor6.SILVER:
            memory_options = list(MemoryOption6)
        elif user_data[message.chat.id]['color'] == IPhoneColor6.SPACE_GRAY:
            memory_options = list(MemoryOption6)
        elif user_data[message.chat.id]['color'] == IPhoneColor6plus.GOLD:
            memory_options = list(MemoryOption6Plus)
        elif user_data[message.chat.id]['color'] == IPhoneColor6plus.SILVER:
            memory_options = list(MemoryOption6Plus)
        elif user_data[message.chat.id]['color'] == IPhoneColor6plus.SPACE_GRAY:
            memory_options = list(MemoryOption6Plus)
        elif user_data[message.chat.id]['color'] == IPhoneColor6s. ROSE_GOLD:
            memory_options = list(MemoryOption6s)
        elif user_data[message.chat.id]['color'] == IPhoneColor6s.GOLD:
            memory_options = list(MemoryOption6s)
        elif user_data[message.chat.id]['color'] == IPhoneColor6s.SILVER:
            memory_options = list(MemoryOption6s)
        elif user_data[message.chat.id]['color'] == IPhoneColor6s.SPACE_GRAY:
            memory_options = list(MemoryOption6s)
        elif user_data[message.chat.id]['color'] == IPhoneColor6splus. ROSE_GOLD:
            memory_options = list(MemoryOption6sPlus)
        elif user_data[message.chat.id]['color'] == IPhoneColor6splus.GOLD:
            memory_options = list(MemoryOption6sPlus)
        elif user_data[message.chat.id]['color'] == IPhoneColor6splus.SILVER:
            memory_options = list(MemoryOption6sPlus)
        elif user_data[message.chat.id]['color'] == IPhoneColor6splus.SPACE_GRAY:
            memory_options = list(MemoryOption6sPlus)
        elif user_data[message.chat.id]['color'] == IPhoneColor7.GOLD:
            memory_options = list(MemoryOption7)
        elif user_data[message.chat.id]['color'] == IPhoneColor7.SILVER:
            memory_options = list(MemoryOption7)
        elif user_data[message.chat.id]['color'] == IPhoneColor7.SPACE_GRAY:
            memory_options = list(MemoryOption7)
        elif user_data[message.chat.id]['color'] == IPhoneColor7.ROSE_GOLD:
            memory_options = list(MemoryOption7)
        elif user_data[message.chat.id]['color'] == IPhoneColor7.BLACK:
            memory_options = list(MemoryOption7)
        elif user_data[message.chat.id]['color'] == IPhoneColor7.BLACK_ONIX:
            memory_options = list(MemoryOption7)
        elif user_data[message.chat.id]['color'] == IPhoneColor7.RED:
            memory_options = list(MemoryOption7)
        elif user_data[message.chat.id]['color'] == IPhoneColor7plus.GOLD:
            memory_options = list(MemoryOption7Plus)
        elif user_data[message.chat.id]['color'] == IPhoneColor7plus.SILVER:
            memory_options = list(MemoryOption7Plus)
        elif user_data[message.chat.id]['color'] == IPhoneColor7plus.SPACE_GRAY:
            memory_options = list(MemoryOption7Plus)
        elif user_data[message.chat.id]['color'] == IPhoneColor7plus.ROSE_GOLD:
            memory_options = list(MemoryOption7Plus)
        elif user_data[message.chat.id]['color'] == IPhoneColor7plus.BLACK:
            memory_options = list(MemoryOption7Plus)
        elif user_data[message.chat.id]['color'] == IPhoneColor7plus.BLACK_ONIX:
            memory_options = list(MemoryOption7Plus)
        elif user_data[message.chat.id]['color'] == IPhoneColor7plus.RED:
            memory_options = list(MemoryOption7Plus)
        elif user_data[message.chat.id]['color'] == IPhoneColor8.GOLD:
            memory_options = list(MemoryOption8)
        elif user_data[message.chat.id]['color'] == IPhoneColor8.SILVER:
            memory_options = list(MemoryOption8)
        elif user_data[message.chat.id]['color'] == IPhoneColor8.SPACE_GRAY:
            memory_options = list(MemoryOption8)
        elif user_data[message.chat.id]['color'] == IPhoneColor8.RED:
            memory_options = list(MemoryOption8)
        elif user_data[message.chat.id]['color'] == IPhoneColor8plus.GOLD:
            memory_options = list(MemoryOption8Plus)
        elif user_data[message.chat.id]['color'] == IPhoneColor8plus.SILVER:
            memory_options = list(MemoryOption8Plus)
        elif user_data[message.chat.id]['color'] == IPhoneColor8plus.SPACE_GRAY:
            memory_options = list(MemoryOption8Plus)
        elif user_data[message.chat.id]['color'] == IPhoneColor8plus.RED:
            memory_options = list(MemoryOption8Plus)
        elif user_data[message.chat.id]['color'] == IPhoneColorX.SILVER:
            memory_options = list(MemoryOptionX)
        elif user_data[message.chat.id]['color'] == IPhoneColorX.SPACE_GRAY:
            memory_options = list(MemoryOptionX)
        elif user_data[message.chat.id]['color'] == IPhoneColorXs.GOLD:
            memory_options = list(MemoryOptionXS)
        elif user_data[message.chat.id]['color'] == IPhoneColorXs.SILVER:
            memory_options = list(MemoryOptionXS)
        elif user_data[message.chat.id]['color'] == IPhoneColorXs.SPACE_GRAY:
            memory_options = list(MemoryOptionXS)
        elif user_data[message.chat.id]['color'] == IPhoneColorXsMax.GOLD:
            memory_options = list(MemoryOptionXSMax)
        elif user_data[message.chat.id]['color'] == IPhoneColorXsMax.SILVER:
            memory_options = list(MemoryOptionXSMax)
        elif user_data[message.chat.id]['color'] == IPhoneColorXsMax.SPACE_GRAY:
            memory_options = list(MemoryOptionXSMax)
        elif user_data[message.chat.id]['color'] == IPhoneColorXR.RED:
            memory_options = list(MemoryOptionXR)
        elif user_data[message.chat.id]['color'] == IPhoneColorXR.BLACK:
            memory_options = list(MemoryOptionXR)
        elif user_data[message.chat.id]['color'] == IPhoneColorXR.WHITE:
            memory_options = list(MemoryOptionXR)
        elif user_data[message.chat.id]['color'] == IPhoneColorXR.KORALL:
            memory_options = list(MemoryOptionXR)
        elif user_data[message.chat.id]['color'] == IPhoneColorXR.YELLOW:
            memory_options = list(MemoryOptionXR)
        elif user_data[message.chat.id]['color'] == IPhoneColorXR.BLUE:
            memory_options = list(MemoryOptionXR)
        elif user_data[message.chat.id]['color'] == IPhoneColor11.RED:
            memory_options = list(MemoryOption11)
        elif user_data[message.chat.id]['color'] == IPhoneColor11.BLACK:
            memory_options = list(MemoryOption11)
        elif user_data[message.chat.id]['color'] == IPhoneColor11.WHITE:
            memory_options = list(MemoryOption11)
        elif user_data[message.chat.id]['color'] == IPhoneColor11.YELLOW:
            memory_options = list(MemoryOption11)
        elif user_data[message.chat.id]['color'] == IPhoneColor11.PURPLE:
            memory_options = list(MemoryOption11)
        elif user_data[message.chat.id]['color'] == IPhoneColor11.GREEN:
            memory_options = list(MemoryOption11)
        elif user_data[message.chat.id]['color'] == IPhoneColor11Pro.GOLD:
            memory_options = list(MemoryOption11Pro)
        elif user_data[message.chat.id]['color'] == IPhoneColor11Pro.SILVER:
            memory_options = list(MemoryOption11Pro)
        elif user_data[message.chat.id]['color'] == IPhoneColor11Pro.SPACE_GRAY:
            memory_options = list(MemoryOption11Pro)
        elif user_data[message.chat.id]['color'] == IPhoneColor11Pro.DARK_GREEN:
            memory_options = list(MemoryOption11Pro)
        elif user_data[message.chat.id]['color'] == IPhoneColor11ProMax.GOLD:
            memory_options = list(MemoryOption11ProMax)
        elif user_data[message.chat.id]['color'] == IPhoneColor11ProMax.SILVER:
            memory_options = list(MemoryOption11ProMax)
        elif user_data[message.chat.id]['color'] == IPhoneColor11ProMax.SPACE_GRAY:
            memory_options = list(MemoryOption11ProMax)
        elif user_data[message.chat.id]['color'] == IPhoneColor11ProMax.DARK_GREEN:
            memory_options = list(MemoryOption11ProMax)
        elif user_data[message.chat.id]['color'] == IPhoneColor12.RED:
            memory_options = list(MemoryOption12)
        elif user_data[message.chat.id]['color'] == IPhoneColor12.BLACK:
            memory_options = list(MemoryOption12)
        elif user_data[message.chat.id]['color'] == IPhoneColor12.WHITE:
            memory_options = list(MemoryOption12)
        elif user_data[message.chat.id]['color'] == IPhoneColor12.BLUE:
            memory_options = list(MemoryOption12)
        elif user_data[message.chat.id]['color'] == IPhoneColor12.PURPLE:
            memory_options = list(MemoryOption12)
        elif user_data[message.chat.id]['color'] == IPhoneColor12.GREEN:
            memory_options = list(MemoryOption12)
        elif user_data[message.chat.id]['color'] == IPhoneColor12mini.RED:
            memory_options = list(MemoryOption12mini)
        elif user_data[message.chat.id]['color'] == IPhoneColor12mini.BLACK:
            memory_options = list(MemoryOption12mini)
        elif user_data[message.chat.id]['color'] == IPhoneColor12mini.WHITE:
            memory_options = list(MemoryOption12mini)
        elif user_data[message.chat.id]['color'] == IPhoneColor12mini.BLUE:
            memory_options = list(MemoryOption12mini)
        elif user_data[message.chat.id]['color'] == IPhoneColor12mini.PURPLE:
            memory_options = list(MemoryOption12mini)
        elif user_data[message.chat.id]['color'] == IPhoneColor12mini.GREEN:
            memory_options = list(MemoryOption12mini)
        elif user_data[message.chat.id]['color'] == IPhoneColor12Pro.GOLD:
            memory_options = list(MemoryOption12Pro)
        elif user_data[message.chat.id]['color'] == IPhoneColor12Pro.SILVER:
            memory_options = list(MemoryOption12Pro)
        elif user_data[message.chat.id]['color'] == IPhoneColor12Pro.GRAPHIT:
            memory_options = list(MemoryOption12Pro)
        elif user_data[message.chat.id]['color'] == IPhoneColor12Pro.OCEAN_BLUE:
            memory_options = list(MemoryOption12Pro)
        elif user_data[message.chat.id]['color'] == IPhoneColor12ProMax.GOLD:
            memory_options = list(MemoryOption12ProMax)
        elif user_data[message.chat.id]['color'] == IPhoneColor12ProMax.SILVER:
            memory_options = list(MemoryOption12ProMax)
        elif user_data[message.chat.id]['color'] == IPhoneColor12ProMax.GRAPHIT:
            memory_options = list(MemoryOption12ProMax)
        elif user_data[message.chat.id]['color'] == IPhoneColor12ProMax.OCEAN_BLUE:
            memory_options = list(MemoryOption12ProMax)
        elif user_data[message.chat.id]['color'] == IPhoneColor13.RED:
            memory_options = list(MemoryOption13)
        elif user_data[message.chat.id]['color'] == IPhoneColor13.DARK_NIGHT:
            memory_options = list(MemoryOption13)
        elif user_data[message.chat.id]['color'] == IPhoneColor13.STAR:
            memory_options = list(MemoryOption13)
        elif user_data[message.chat.id]['color'] == IPhoneColor13.BLUE:
            memory_options = list(MemoryOption13)
        elif user_data[message.chat.id]['color'] == IPhoneColor13.PINK:
            memory_options = list(MemoryOption13)
        elif user_data[message.chat.id]['color'] == IPhoneColor13mini.RED:
            memory_options = list(MemoryOption13mini)
        elif user_data[message.chat.id]['color'] == IPhoneColor13mini.DARK_NIGHT:
            memory_options = list(MemoryOption13mini)
        elif user_data[message.chat.id]['color'] == IPhoneColor13mini.STAR:
            memory_options = list(MemoryOption13mini)
        elif user_data[message.chat.id]['color'] == IPhoneColor13mini.BLUE:
            memory_options = list(MemoryOption13mini)
        elif user_data[message.chat.id]['color'] == IPhoneColor13mini.PINK:
            memory_options = list(MemoryOption13mini)
        elif user_data[message.chat.id]['color'] == IPhoneColor13mini.GREEN:
            memory_options = list(MemoryOption13mini)
        elif user_data[message.chat.id]['color'] == IPhoneColor13Pro.GOLD:
            memory_options = list(MemoryOption13Pro)
        elif user_data[message.chat.id]['color'] == IPhoneColor13Pro.SILVER:
            memory_options = list(MemoryOption13Pro)
        elif user_data[message.chat.id]['color'] == IPhoneColor13Pro.GRAPHIT:
            memory_options = list(MemoryOption13Pro)
        elif user_data[message.chat.id]['color'] == IPhoneColor13Pro.SKY_BLUE:
            memory_options = list(MemoryOption13Pro)
        elif user_data[message.chat.id]['color'] == IPhoneColor13ProMax.GOLD:
            memory_options = list(MemoryOption13ProMax)
        elif user_data[message.chat.id]['color'] == IPhoneColor13ProMax.SILVER:
            memory_options = list(MemoryOption13ProMax)
        elif user_data[message.chat.id]['color'] == IPhoneColor13ProMax.GRAPHIT:
            memory_options = list(MemoryOption13ProMax)
        elif user_data[message.chat.id]['color'] == IPhoneColor13ProMax.SKY_BLUE:
            memory_options = list(MemoryOption13ProMax)
        elif user_data[message.chat.id]['color'] == IPhoneColor14.RED:
            memory_options = list(MemoryOption14)
        elif user_data[message.chat.id]['color'] == IPhoneColor14.DARK_NIGHT:
            memory_options = list(MemoryOption14)
        elif user_data[message.chat.id]['color'] == IPhoneColor14.STAR:
            memory_options = list(MemoryOption14)
        elif user_data[message.chat.id]['color'] == IPhoneColor14.BLUE:
            memory_options = list(MemoryOption14)
        elif user_data[message.chat.id]['color'] == IPhoneColor14.YELLOW:
            memory_options = list(MemoryOption14)
        elif user_data[message.chat.id]['color'] == IPhoneColor14.PURPLE:
            memory_options = list(MemoryOption14)
        elif user_data[message.chat.id]['color'] == IPhoneColor14PLUS.RED:
            memory_options = list(MemoryOption14Plus)
        elif user_data[message.chat.id]['color'] == IPhoneColor14PLUS.DARK_NIGHT:
            memory_options = list(MemoryOption14Plus)
        elif user_data[message.chat.id]['color'] == IPhoneColor14PLUS.STAR:
            memory_options = list(MemoryOption14Plus)
        elif user_data[message.chat.id]['color'] == IPhoneColor14PLUS.BLUE:
            memory_options = list(MemoryOption14Plus)
        elif user_data[message.chat.id]['color'] == IPhoneColor14PLUS.YELLOW:
            memory_options = list(MemoryOption14Plus)
        elif user_data[message.chat.id]['color'] == IPhoneColor14PLUS.PURPLE:
            memory_options = list(MemoryOption14Plus)
        elif user_data[message.chat.id]['color'] == IPhoneColor14Pro.GOLD:
            memory_options = list(MemoryOption14Pro)
        elif user_data[message.chat.id]['color'] == IPhoneColor14Pro.SILVER:
            memory_options = list(MemoryOption14Pro)
        elif user_data[message.chat.id]['color'] == IPhoneColor14Pro.BLACK:
            memory_options = list(MemoryOption14Pro)
        elif user_data[message.chat.id]['color'] == IPhoneColor14Pro.PURPLE:
            memory_options = list(MemoryOption14Pro)
        elif user_data[message.chat.id]['color'] == IPhoneColor14ProMax.GOLD:
            memory_options = list(MemoryOption14ProMax)
        elif user_data[message.chat.id]['color'] == IPhoneColor14ProMax.SILVER:
            memory_options = list(MemoryOption14ProMax)
        elif user_data[message.chat.id]['color'] == IPhoneColor14ProMax.BLACK:
            memory_options = list(MemoryOption14ProMax)
        elif user_data[message.chat.id]['color'] == IPhoneColor14ProMax.PURPLE:
            memory_options = list(MemoryOption14ProMax)
        elif user_data[message.chat.id]['color'] == IPhoneColor15.BLACK:
            memory_options = list(MemoryOption15)
        elif user_data[message.chat.id]['color'] == IPhoneColor15.BLUE:
            memory_options = list(MemoryOption15)
        elif user_data[message.chat.id]['color'] == IPhoneColor15.GREEN:
            memory_options = list(MemoryOption15)
        elif user_data[message.chat.id]['color'] == IPhoneColor15.YELLOW:
            memory_options = list(MemoryOption15)
        elif user_data[message.chat.id]['color'] == IPhoneColor15.PINK:
            memory_options = list(MemoryOption15)
        elif user_data[message.chat.id]['color'] == IPhoneColor15PLUS.BLACK:
            memory_options = list(MemoryOption15Plus)
        elif user_data[message.chat.id]['color'] == IPhoneColor15PLUS.BLUE:
            memory_options = list(MemoryOption15Plus)
        elif user_data[message.chat.id]['color'] == IPhoneColor15PLUS.GREEN:
            memory_options = list(MemoryOption15Plus)
        elif user_data[message.chat.id]['color'] == IPhoneColor15PLUS.YELLOW:
            memory_options = list(MemoryOption15Plus)
        elif user_data[message.chat.id]['color'] == IPhoneColor15PLUS.PINK:
            memory_options = list(MemoryOption15Plus)
        elif user_data[message.chat.id]['color'] == IPhoneColor15Pro.BLACK:
            memory_options = list(MemoryOption15Pro)
        elif user_data[message.chat.id]['color'] == IPhoneColor15Pro.WHITE:
            memory_options = list(MemoryOption15Pro)
        elif user_data[message.chat.id]['color'] == IPhoneColor15Pro.BLUE:
            memory_options = list(MemoryOption15Pro)
        elif user_data[message.chat.id]['color'] == IPhoneColor15Pro.NATURAL_TITANIUM:
            memory_options = list(MemoryOption15Pro)
        elif user_data[message.chat.id]['color'] == IPhoneColor15ProMax.BLACK:
            memory_options = list(MemoryOption15ProMax)
        elif user_data[message.chat.id]['color'] == IPhoneColor15ProMax.WHITE:
            memory_options = list(MemoryOption15ProMax)
        elif user_data[message.chat.id]['color'] == IPhoneColor15ProMax.BLUE:
            memory_options = list(MemoryOption15ProMax)
        elif user_data[message.chat.id]['color'] == IPhoneColor15ProMax.NATURAL_TITANIUM:
            memory_options = list(MemoryOption15ProMax)
        elif user_data[message.chat.id]['color'] == IPhoneColorSE2.BLACK:
            memory_options = list(MemoryOptionSE2)
        elif user_data[message.chat.id]['color'] == IPhoneColorSE2.WHITE:
            memory_options = list(MemoryOptionSE2)
        elif user_data[message.chat.id]['color'] == IPhoneColorSE3.BLACK:
            memory_options = list(MemoryOptionSE3)
        elif user_data[message.chat.id]['color'] == IPhoneColorSE3.WHITE:
            memory_options = list(MemoryOptionSE3)
        elif user_data[message.chat.id]['color'] == IPhoneColorSE3.RED:
            memory_options = list(MemoryOptionSE3)
        bot.send_message(message.chat.id, 'Выберите память:', reply_markup=create_keyboard(memory_options))
    except ValueError:
        bot.send_message(message.chat.id, 'Пожалуйста, выберите цвет из предложенного списка.')

@bot.message_handler(func=lambda message: get_user_state(message.chat.id) == UserState.CHOOSE_MEMORY)
def input_akb(message):
    try:
        user_data[message.chat.id]['memory'] = message.text
        set_user_state(message.chat.id, UserState.INPUT_AKB)
        bot.send_message(message.chat.id, 'Укажите состояние аккумулятора (пример: 87):')
    except ValueError:
        bot.send_message(message.chat.id, 'Пожалуйста, выберите объем памяти из предложенного списка.')

@bot.message_handler(func=lambda message: get_user_state(message.chat.id) == UserState.INPUT_AKB)
def input_sim(message):
    user_data[message.chat.id]['akb'] = message.text
    set_user_state(message.chat.id, UserState.INPUT_SIM)
    bot.send_message(message.chat.id, 'Укажите количество SIM (Пример: SIM + eSIM):')

@bot.message_handler(func=lambda message: get_user_state(message.chat.id) == UserState.INPUT_SIM)
def input_acondition(message):
    user_data[message.chat.id]['sim'] = message.text
    set_user_state(message.chat.id, UserState.INPUT_ACONDITION)
    bot.send_message(message.chat.id, 'Опишите внешнее состояние устройства:')

@bot.message_handler(func=lambda message: get_user_state(message.chat.id) == UserState.INPUT_ACONDITION)
def input_wcondition(message):
    user_data[message.chat.id]['acondition'] = message.text
    set_user_state(message.chat.id, UserState.INPUT_WCONDITION)
    bot.send_message(message.chat.id, 'Опишите рабочее состояние устройства:')


@bot.message_handler(func=lambda message: get_user_state(message.chat.id) == UserState.INPUT_WCONDITION)
def post_ad(message):
    chat_id = message.chat.id
    user_data[chat_id]['wcondition'] = message.text
    user_data[chat_id]['name'] = f"@{message.from_user.username}"
    print(user_data[chat_id])
    ad = Ad(
        title=f"{user_data[chat_id]['device'].value} {user_data[chat_id]['model'].value} {user_data[chat_id]['color'].value} {user_data[chat_id]['memory']} {user_data[chat_id]['device'].value} {user_data[chat_id]['akb']}  {user_data[chat_id]['sim']}",
        description=f"{user_data[chat_id]['acondition']} {user_data[chat_id]['wcondition']}",
    )
    ad.save()
    post = (f"Объявление:\n"
            f"Устройство: {user_data[chat_id]['device'].value}\n"
            f"Модель: {user_data[chat_id]['model'].value}\n"
            f"Цвет: {user_data[chat_id]['color'].value}\n"
            f"Объем памяти: {user_data[chat_id]['memory']}\n"
            f"Состояние аккумулятора: {user_data[chat_id]['akb']}\n"
            f"Количество SIM: {user_data[chat_id]['sim']}\n"
            f"Внешнее состояние: {user_data[chat_id]['acondition']}\n"
            f"Рабочее состояние: {user_data[chat_id]['wcondition']}\n"
            f"Продает: {user_data[chat_id]['name']}\n")

    bot.send_message(chat_id, post)

    if admin_chat_id:
        bot.send_message(admin_chat_id, f"Новое объявление от {message.from_user.username}:\n\n{post}")

    user_data[chat_id] = {}  # Сброс данных
    show_main_menu(chat_id)  # Показать главное меню

bot.polling(none_stop=True)
