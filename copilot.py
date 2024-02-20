# Импортируем необходимые библиотеки
import os
import telebot
from telebot import types

# Получаем токен бота из переменной окружения
BOT_TOKEN = '6887415444:AAEtWlH_8DncXs0EgCjSUXKZ-Zu-L5_pHMA'

# Создаем экземпляр бота
bot = telebot.TeleBot(BOT_TOKEN)

# Создаем словарь для хранения языковых настроек пользователей
user_lang = {}

# Создаем функцию для генерации меню с выбором языка
def language_menu():
    # Создаем объект клавиатуры
    keyboard = types.InlineKeyboardMarkup()
    # Добавляем кнопки с языками
    keyboard.add(types.InlineKeyboardButton("Русский", callback_data='lang_ru'))
    keyboard.add(types.InlineKeyboardButton("Қазақша", callback_data='lang_kz'))
    # Возвращаем клавиатуру
    return keyboard

# Создаем функцию для генерации меню на русском языке
def menu_ru():
    # Создаем объект клавиатуры
    keyboard = types.InlineKeyboardMarkup()
    # Добавляем кнопки с пунктами меню
    keyboard.add(types.InlineKeyboardButton("О компании и продуктах", callback_data='company_ru'))
    keyboard.add(types.InlineKeyboardButton("Библиотека и контент", callback_data='library_ru'))
    keyboard.add(types.InlineKeyboardButton("Маркетинг План", callback_data='marketing_ru'))
    keyboard.add(types.InlineKeyboardButton("Адреса филиалов и пунктов выдачи", callback_data='locations_ru'))
    keyboard.add(types.InlineKeyboardButton("Горячая линия", callback_data='hotline_ru'))
    keyboard.add(types.InlineKeyboardButton("Бухгалтерия и отчетность", callback_data='accounting_ru'))
    keyboard.add(types.InlineKeyboardButton("Отзывы", callback_data='reviews_ru'))
    keyboard.add(types.InlineKeyboardButton("Важные объявления", callback_data='announcements_ru'))
    keyboard.add(types.InlineKeyboardButton("Бизнес школа SOLWELL", callback_data='school_ru'))
    # Возвращаем клавиатуру
    return keyboard

# Создаем функцию для генерации меню на казахском языке
def menu_kz():
    # Создаем объект клавиатуры
    keyboard = types.InlineKeyboardMarkup()
    # Добавляем кнопки с пунктами меню
    keyboard.add(types.InlineKeyboardButton("Компания және өнімдер туралы", callback_data='company_kz'))
    keyboard.add(types.InlineKeyboardButton("Кітапхана және контент", callback_data='library_kz'))
    keyboard.add(types.InlineKeyboardButton("Маркетинг жоспары", callback_data='marketing_kz'))
    keyboard.add(types.InlineKeyboardButton("Филиалдар және шығару орнының мекен-жайлары", callback_data='locations_kz'))
    keyboard.add(types.InlineKeyboardButton("Ысымды арна", callback_data='hotline_kz'))
    keyboard.add(types.InlineKeyboardButton("Есептілік және есептіліктік", callback_data='accounting_kz'))
    keyboard.add(types.InlineKeyboardButton("Пікірлер", callback_data='reviews_kz'))
    keyboard.add(types.InlineKeyboardButton("Маңызды хабарландырулар", callback_data='announcements_kz'))
    keyboard.add(types.InlineKeyboardButton("SOLWELL бизнес мектебі", callback_data='school_kz'))
    # Возвращаем клавиатуру
    return keyboard

# Создаем обработчик команд /start и /hello
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    # Отправляем приветственное сообщение с меню выбора языка
    bot.send_message(message.chat.id, "Привет, я телеграмм-бот. Пожалуйста, выберите язык:", reply_markup=language_menu())

# Создаем обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    # Получаем идентификатор пользователя
    user_id = call.from_user.id
    # Получаем данные кнопки
    data = call.data
    # Если пользователь выбрал язык
    if data.startswith('lang_'):
        # Сохраняем языковую настройку пользователя
        user_lang[user_id] = data[5:]
        # Отправляем сообщение с соответствующим меню
        if user_lang[user_id] == 'ru':
            bot.send_message(user_id, "Вы выбрали русский язык. Вот меню:", reply_markup=menu_ru())
        elif user_lang[user_id] == 'kz':
            bot.send_message(user_id, "Сіз қазақ тілін таңдадыңыз. Меню мында:", reply_markup=menu_kz())
    # Если пользователь выбрал пункт меню
    else:
        # Отправляем сообщение с подтверждением выбора
        bot.send_message(user_id, f"Вы выбрали {data}. Скоро я пришлю вам информацию по этому пункту.")
        # Здесь вы можете добавить свой код для обработки запросов по пунктам меню

# Запускаем бота
bot.polling()
