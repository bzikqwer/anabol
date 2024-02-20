import asyncio
import logging
import sys

from aiogram import F
from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardMarkup, ReplyKeyboardBuilder


API_TOKEN = '6887415444:AAEtWlH_8DncXs0EgCjSUXKZ-Zu-L5_pHMA'

# Создаем бота и диспетчер
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot=bot)


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="🇷🇺 Русский",
        callback_data="ru")
    )
    builder.add(types.InlineKeyboardButton(
        text="🇰🇿 Қазақша",
        callback_data="kz")
    )
    await message.answer(
        "Выберите язык для общения с меню",
        reply_markup=builder.as_markup()
    )
@dp.callback_query(F.data == "menu")
async def send_ru_menu(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="🇷🇺 Русский",
        callback_data="ru")
    )
    builder.add(types.InlineKeyboardButton(
        text="🇰🇿 Қазақша",
        callback_data="kz")
    )

    await callback.message.answer(
        "На каком языке хотите получить информацию?",
        reply_markup=builder.as_markup()
    )

@dp.callback_query(F.data == "ru")
async def send_ru_menu(callback: types.CallbackQuery):


    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="О компании и продуктах",
        callback_data="company_ru")
    )

    builder.row(types.InlineKeyboardButton(
        text="Библиотека и контент",
        callback_data="library_ru")
    )
    builder.row(types.InlineKeyboardButton(
        text="Маркетинг План",
        callback_data="marketing_ru")
    )
    builder.row(types.InlineKeyboardButton(
        text="Адреса филиалов и пунктов выдачи",
        callback_data="locations_ru")
    )
    builder.row(types.InlineKeyboardButton(
        text="Горячая линия",
        callback_data="hotline_ru")
    )
    builder.row(types.InlineKeyboardButton(
        text="Бухгалтерия и отчетность",
        callback_data="accounting_ru")
    )
    builder.row(types.InlineKeyboardButton(
        text="Отзывы",
        callback_data="reviews_ru")
    )
    builder.row(types.InlineKeyboardButton(
        text="Важные объявления",
        callback_data="announcements_ru")
    )
    builder.row(types.InlineKeyboardButton(
        text="Бизнес школа SOLWELL",
        callback_data="school_ru")
    )
    await callback.message.answer(
        """Здесь главное меню👇

😊Я могу тебе рассказать о компании, продукции, маркетинге, о том, как и сколько ты сможешь зарабатывать в компании и многое другое!

⬇️Выбирай с чего начнем:""",
        reply_markup=builder.as_markup()
    )

@dp.callback_query(F.data == "kz")
async def send_kz_menu(callback: types.CallbackQuery):
    # InlineKeyboardBuilder сыныптың экземплярын жасаңыз
    builder = InlineKeyboardBuilder()

    # row әдісі арқылы бірінші жолға түймелерді қосыңыз
    builder.row(types.InlineKeyboardButton(
        text="Компания және өнімдер туралы",
        callback_data="company_kz")
    )

    # row әдісі арқылы екінші жолға түймелерді қосыңыз
    builder.row(types.InlineKeyboardButton(
        text="Кітапхана және контент",
        callback_data="library_kz")
    )

    # row әдісі арқылы үшінші жолға түймелерді қосыңыз
    builder.row(types.InlineKeyboardButton(
        text="Маркетинг жоспары",
        callback_data="marketing_kz")
    )

    # row әдісі арқылы төртінші жолға түймелерді қосыңыз
    builder.row(types.InlineKeyboardButton(
        text="Филиалдар мен шығару орнының мекенжайлары",
        callback_data="locations_kz")
    )

    # row әдісі арқылы бесінші жолға түймелерді қосыңыз
    builder.row(types.InlineKeyboardButton(
        text="Жылдам желі",
        callback_data="hotline_kz")
    )

    # row әдісі арқылы алтыншы жолға түймелерді қосыңыз
    builder.row(types.InlineKeyboardButton(
        text="Есептілік және есептілік",
        callback_data="accounting_kz")
    )

    # row әдісі арқылы жетінші жолға түймелерді қосыңыз
    builder.row(types.InlineKeyboardButton(
        text="Пікірлер",
        callback_data="reviews_kz")
    )

    # row әдісі арқылы сегізінші жолға түймелерді қосыңыз
    builder.row(types.InlineKeyboardButton(
        text="Маңызды хабарландырулар",
        callback_data="announcements_kz")
    )

    # row әдісі арқылы тоғызыншы жолға түймелерді қосыңыз
    builder.row(types.InlineKeyboardButton(
        text="SOLWELL бизнес мектебі",
        callback_data="school_kz")
    )

    # клавиатура бар хабарламаны жіберіңіз
    await callback.message.answer(
        """Мұнда негізгі мәзір👇

😊Мен сенге компания, өнімдер, маркетинг, сен компанияда қалай және неше зарабатай аласың және тағы басқа көп нәрсе туралы айтайын!

⬇️Бастаймыз дегенді таңда:""",
        reply_markup=builder.as_markup()
    )


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(API_TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())