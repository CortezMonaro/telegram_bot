from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

inline_kb0 = InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton(text='Понедельник', callback_data='day_1'),\
												   InlineKeyboardButton(text='Вторник', callback_data='day_2'),\
												   InlineKeyboardButton(text='Среда', callback_data='day_3'),\
												   InlineKeyboardButton(text='Четверг', callback_data='day_4'),\
												   InlineKeyboardButton(text='Пятница', callback_data='day_5'),\
												   InlineKeyboardButton(text='Суббота', callback_data='day_6'),\
												   InlineKeyboardButton(text='Воскресенье', callback_data='day_7'))

inl_1 = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Тяжелый рок', callback_data='music1_1'),\
											  InlineKeyboardButton(text='Тяжелый дабстеп', callback_data='music1_2'))

inl_2 = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Классика', callback_data='music2_1'),\
											  InlineKeyboardButton(text='Попса', callback_data='music2_2'))

inl_3 = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Мелодик дабстеп', callback_data='music3_1'),\
											  InlineKeyboardButton(text='Шансон', callback_data='music3_2'))

inl_4 = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Латинос', callback_data='music4_1'),\
											  InlineKeyboardButton(text='Джаз', callback_data='music4_2'))

inl_5 = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Блюз', callback_data='music5_1'),\
											  InlineKeyboardButton(text='Фонк', callback_data='music5_2'))

inl_6 = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Дрель соседа', callback_data='music6_1'),\
											  InlineKeyboardButton(text='Рояль соседа', callback_data='music6_2'))

inl_7 = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Рок', callback_data='music7_1'),\
											  InlineKeyboardButton(text='Электросвинг', callback_data='music7_2'))