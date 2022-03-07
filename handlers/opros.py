from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
#from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db
from keyboards import kb_1
from keyboards import inline_kb0, inl_1, inl_2, inl_3, inl_4, inl_5, inl_6, inl_7
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



class FSMAdmin(StatesGroup):
	day = State()
	music = State()


	

async def opros_start(message : types.Message):
	await FSMAdmin.next()
	await message.reply('Выбери любимый день недели:', reply_markup=inline_kb0)

async def week(callback : types.CallbackQuery, state:FSMContext):
	b = int(callback.data.split('_')[1])
	if b == 1:
		async with state.proxy() as data:
			data['day'] = 'Понедельник'
		await FSMAdmin.next()
		await callback.message.reply('Понедельник? Извращенец! Теперь выбери жанр музыки для этого дня (выбор ограничен):', reply_markup=inl_[b])
	elif b == 2:
		async with state.proxy() as data:
			data['day'] = 'Вторник'
		await FSMAdmin.next()
		await callback.message.reply('Вторник? Странный вы тип. Теперь выбери жанр музыки для этого дня (выбор ограничен):', reply_markup=inl_2)
	elif b == 3:
		async with state.proxy() as data:
			data['day'] = 'Среда'
		await FSMAdmin.next()
		await callback.message.reply('Среда? Половина рабочей недели? Теперь выбери жанр музыки для этого дня (выбор ограничен):', reply_markup=inl_3)
	elif b == 4:
		async with state.proxy() as data:
			data['day'] = 'Четверг'
		await FSMAdmin.next()
		await callback.message.reply('Четверг! Пятница уже близко! Теперь выбери жанр музыки для этого дня (выбор ограничен):', reply_markup=inl_4)
	elif b == 5:
		async with state.proxy() as data:
			data['day'] = 'Пятница'
		await FSMAdmin.next()
		await callback.message.reply('Пятница! Пора отрываться! Теперь выбери жанр музыки для этого дня (выбор ограничен):', reply_markup=inl_5)
	elif b == 6:
		async with state.proxy() as data:
			data['day'] = 'Суббота'
		await FSMAdmin.next()
		await callback.message.reply('Суббота, что ж передаем привет соседу. Теперь выбери жанр музыки для этого дня (выбор ограничен):', reply_markup=inl_6)
	elif b == 7:
		async with state.proxy() as data:
			data['day'] = 'Воскресенье'
		await FSMAdmin.next()
		await callback.message.reply('Воскресенье! Сегодня то уж точно отдохнешь! Теперь выбери жанр музыки для этого дня (выбор ограничен):', reply_markup=inl_7)
	


async def monday(callback : types.CallbackQuery, state:FSMContext):
	a = int(callback.data.split('_')[1])
	if a == 1:
		async with state.proxy() as data:
			data['music'] = 'Тяжелый рок'
	else:
		async with state.proxy() as data:
			data['music'] = 'Тяжелый дабстеп'
	await sqlite_db.sql_add2(state)
	await state.finish()
	await callback.message.reply("Ah, shit, here we go again", reply_markup=kb_1)


async def tuesday(callback : types.CallbackQuery, state:FSMContext):
	a = int(callback.data.split('_')[1])
	if a == 1:
		async with state.proxy() as data:
			data['music'] = 'Классика'
	else:
		async with state.proxy() as data:
			data['music'] = 'Попса'
	await sqlite_db.sql_add2(state)
	await state.finish()
	await callback.message.reply("Ah, shit, here we go again", reply_markup=kb_1)


async def wednesday(callback : types.CallbackQuery, state:FSMContext):
	a = int(callback.data.split('_')[1])
	if a == 1:
		async with state.proxy() as data:
			data['music'] = 'Мелодик дабстеп'
	else:
		async with state.proxy() as data:
			data['music'] = 'Шансон'
	await sqlite_db.sql_add2(state)
	await state.finish()
	await callback.message.reply("Ah, shit, here we go again", reply_markup=kb_1)


async def thursday(callback : types.CallbackQuery, state:FSMContext):
	a = int(callback.data.split('_')[1])
	if a == 1:
		async with state.proxy() as data:
			data['music'] = 'Латинос'
	else:
		async with state.proxy() as data:
			data['music'] = 'Джаз'
	await sqlite_db.sql_add2(state)
	await state.finish()
	await callback.message.reply("Ah, shit, here we go again", reply_markup=kb_1)


async def friday(callback : types.CallbackQuery, state:FSMContext):
	a = int(callback.data.split('_')[1])
	if a == 1:
		async with state.proxy() as data:
			data['music'] = 'Блюз'
	else:
		async with state.proxy() as data:
			data['music'] = 'Фонк'
	await sqlite_db.sql_add2(state)
	await state.finish()
	await callback.message.reply("Ah, shit, here we go again", reply_markup=kb_1)


async def saturday(callback : types.CallbackQuery, state:FSMContext):
	a = int(callback.data.split('_')[1])
	if a == 1:
		async with state.proxy() as data:
			data['music'] = 'Дрель соседа'
	else:
		async with state.proxy() as data:
			data['music'] = 'Рояль соседа'
	await sqlite_db.sql_add2(state)
	await state.finish()
	await callback.message.reply("Ah, shit, here we go again", reply_markup=kb_1)


async def sunday(callback : types.CallbackQuery, state:FSMContext):
	a = int(callback.data.split('_')[1])
	if a == 1:
		async with state.proxy() as data:
			data['music'] = 'Рок'
	else:
		async with state.proxy() as data:
			data['music'] = 'Электросвинг'
	await sqlite_db.sql_add2(state)
	await state.finish()
	await callback.message.reply("Ah, shit, here we go again", reply_markup=kb_1)






def register_handlers_opros(dp : Dispatcher):
	dp.register_message_handler(opros_start, commands=['Опрос'], state=None) #def+commands
	dp.register_callback_query_handler(week, Text(startswith='day_'), state=FSMAdmin.day)
	dp.register_callback_query_handler(monday, Text(startswith='music1_'), state=FSMAdmin.music)
	dp.register_callback_query_handler(tuesday, Text(startswith='music2_'), state=FSMAdmin.music)
	dp.register_callback_query_handler(wednesday, Text(startswith='music3_'), state=FSMAdmin.music)
	dp.register_callback_query_handler(thursday, Text(startswith='music4_'), state=FSMAdmin.music)
	dp.register_callback_query_handler(friday, Text(startswith='music5_'), state=FSMAdmin.music)
	dp.register_callback_query_handler(saturday, Text(startswith='music6_'), state=FSMAdmin.music)
	dp.register_callback_query_handler(sunday, Text(startswith='music7_'), state=FSMAdmin.music)
	