


if user_data[“chat_id”][“model”] == IPhoneModel.IPHONE_6:
    colors = list(IPhone6Color)
elif user_data[“chat_id”][“model”] == IPhoneModel.IPHONE_X:
    colors = list(IPhoneXColor)


    CHOOSE_DEVICE = 1
    CHOOSE_MODEL = 2
    CHOOSE_COLOR = 3
    CHOOSE_MEMORY = 4
    INPUT_AKB = 5
    INPUT_SIM = 6
    INPUT_ACONDITION = 7
    INPUT_WCONDITION = 8



class IPhoneModel(Enum):
    IPHONE_6= 'iPhone 6'
    IPHONE_6_PLUS = 'iPhone 6 Plus'
    IPHONE_6S= 'iPhone 6s'
    IPHONE_6S_PLUS = 'iPhone 6s Plus'
    PHONE_7= 'iPhone 7'
    IPHONE_7_PLUS = 'iPhone 7 Plus'
    IPHONE_8= 'iPhone 8'
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



class IPhoneColorSE1(Enum):
    BLACK = 'Черный'
    WHITE = 'Белый'

class IPhoneColorSE2(Enum):
    BLACK = 'Черный'
    WHITE = 'Белый'
    RED = '(PRODUCT)RED'

class MemoryOption6(Enum):
    GB_16 = '16гб'
    GB_32 = '32гб'
    GB_64 = '64гб'
    GB_128 = '128гб'

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