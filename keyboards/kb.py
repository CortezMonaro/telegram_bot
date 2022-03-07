from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton ('/Допрос')
b2 = KeyboardButton ('/Опрос')

kb_1 = ReplyKeyboardMarkup(resize_keyboard=True)

kb_1.row(b1, b2)