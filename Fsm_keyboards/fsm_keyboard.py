from aiogram.types import InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def name_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Punch', callback_data='punch'),
                 InlineKeyboardButton(text='Pizza', callback_data='pizza'),
                 InlineKeyboardButton(text='Pie', callback_data='pie'))
    return keyboard.as_markup()


def size_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Large', callback_data='large'),
                 InlineKeyboardButton(text='Major', callback_data='major'),
                 InlineKeyboardButton(text='Small', callback_data='small'))
    return keyboard.as_markup()


def location():
    keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Show location", request_location=True)]]
                                   , resize_keyboard=True)
    return keyboard