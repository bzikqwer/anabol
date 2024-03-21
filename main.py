import asyncio
import logging
import sys
from aiogram.methods.send_video import SendVideo
from aiogram import F
from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, FSInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardMarkup, ReplyKeyboardBuilder




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
        text="О компании",
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
        text="О продуктах",
        callback_data="products_ru")
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

    builder = InlineKeyboardBuilder()


    builder.row(types.InlineKeyboardButton(
        text="Компания туралы",
        callback_data="company_kz")
    )


    builder.row(types.InlineKeyboardButton(
        text="Кітапхана және контент",
        callback_data="library_kz")
    )


    builder.row(types.InlineKeyboardButton(
        text="Маркетинг жоспары",
        callback_data="marketing_kz")
    )


    builder.row(types.InlineKeyboardButton(
        text="Филиалдар мен шығару орнының мекенжайлары",
        callback_data="locations_kz")
    )




    builder.row(types.InlineKeyboardButton(
        text="Өнімдер туралы",
        callback_data="products_kz")
    )




    builder.row(types.InlineKeyboardButton(
        text="SOLWELL бизнес мектебі",
        callback_data="school_kz")
    )

    
    await callback.message.answer(
        """Мұнда негізгі мәзір👇

😊Мен сенге компания, өнімдер, маркетинг, сен компанияда қалай және неше зарабатай аласың және тағы басқа көп нәрсе туралы айтайын!

⬇️Бастаймыз дегенді таңда:""",
        reply_markup=builder.as_markup()
    )

@dp.callback_query(F.data == "company_ru")
async def send_kz_menu(callback: types.CallbackQuery):
    await callback.message.answer("""Компания SOLWELL - это
сообщество людей, своим главным приоритетом в жизни выбрали здоровье.

Мы направили наш опыт, наши знания и умения на то, чтобы помочь себе и другим минимализировать последствия 
уже накопившихся проблем со здоровьем, а в каких-то случаях и решить их полностью.
Подробно о нас Вы можете узнать на нашем сайте:
https://solwell.kz/""")
@dp.callback_query(F.data == "company_kz")
async def send_kz_menu(callback: types.CallbackQuery):
    await callback.message.answer("""SOLWELL - бұл өмірде басты приоритет ретінде денсаулықты таңдаған адамдардың қоғамы.

Мы тәжірибемізді, білімімізді және дағдыларымызды денсаулық мәселелерінің алдын алуға және оларды шешуге бағыттадық, 
кейде тіпті толықтай жоюға көмектесу үшін.
Біз туралы толығырақ сіз біздің сайттан біле аласыз:
https://solwell.kz/""")

@dp.callback_query(F.data == "library_ru")
async def send_kz_menu(callback: types.CallbackQuery):
    await callback.message.answer("""Отправляю вам краткую информацию о нас ожидайте""")
    agenda = FSInputFile("./files/presentation/SOLWELL.pdf")
    await bot.send_document(callback.message.chat.id, agenda)
@dp.callback_query(F.data == "library_kz")
async def send_kz_menu(callback: types.CallbackQuery):
    await callback.message.answer("""Сізге біз туралы қысқаша ақпарат жіберемін""")
    agenda = FSInputFile("./files/presentation/SOLWELL.pdf")
    await bot.send_document(callback.message.chat.id, agenda)
@dp.callback_query(F.data == "marketing_ru")
async def send_kz_menu(callback: types.CallbackQuery):
    pass
@dp.callback_query(F.data == "marketing_kz")
async def send_kz_menu(callback: types.CallbackQuery):
    pass
@dp.callback_query(F.data == "locations_ru")
async def send_kz_menu(callback: types.CallbackQuery):
    await callback.message.answer("""Центральный офис
Телефоны:
☎️ +7 777 552 94 59 - 🟢 WhatsApp | 🔵 Telegram | 🟣 Viber
📞 +7 702 701 79 68 - телефон для связи
Адрес: улица Бухар-жырау 33, офис 1""")
@dp.callback_query(F.data == "locations_kz")
async def send_kz_menu(callback: types.CallbackQuery):
    await callback.message.answer("""Орталық кеңсе
Телефондар:
☎️ +7 777 552 94 59 - 🟢 WhatsApp | 🔵 Telegram | 🟣 Viber
📞 +7 702 701 79 68 - байланыс телефоны
Мекен-жайы: Бұқар жырау көшесі 33, кеңсе 1""")
@dp.callback_query(F.data == "products_ru")
async def send_kz_menu(callback: types.CallbackQuery):
    await callback.message.answer("""Подробней о наших продуктах вы можете узнать на нашем сайте, там же вы найдете актуальные цены на них:
https://solwell.kz/ru/store """)
@dp.callback_query(F.data == "products_kz")
async def send_kz_menu(callback: types.CallbackQuery):
    await callback.message.answer("""Біздің өнімдер туралы толығырақ ақпаратты біздің веб-сайтымыздан біле аласыздар, сондай-ақ онда олардың актуалды бағаларын таба аласыздар:
https://solwell.kz/ru/store""")
@dp.callback_query(F.data == "school_ru")
async def send_kz_menu(callback: types.CallbackQuery):
    pass
@dp.callback_query(F.data == "school_kz")
async def send_kz_menu(callback: types.CallbackQuery):
    pass
# @dp.callback_query(F.data == "company_ru")
# async def send_kz_menu(callback: types.CallbackQuery):
#
#
#
#
#
#     ## передача файла
#     agenda = FSInputFile("./files/presentation/SOLWELL.pdf")
#     await bot.send_document(callback.message.chat.id, agenda)
#     # передача видео
#     # video = FSInputFile("tk.mp4")  # используем готовый класс
#     #
#     # await bot.send_video(callback.message.chat.id, video=video)  # отправляем видео

async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(API_TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
