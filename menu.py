import asyncio
import logging
import sys

from aiogram import F
from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder

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
        "Выберите язык для общения с меню",
        reply_markup=builder.as_markup()
    )
@dp.callback_query(F.data == "ru")
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
    builder.add(types.InlineKeyboardButton(
        text="Menu",
        callback_data="menu")
    )
    await callback.message.answer(
        "Красава давай еще",
        reply_markup=builder.as_markup()
    )
