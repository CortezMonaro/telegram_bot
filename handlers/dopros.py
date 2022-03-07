from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db
from keyboards import kb_1

class FSMAdmin(StatesGroup):
	name = State()
	weight = State()
	height = State()


async def fsm_start(message : types.Message):
	await FSMAdmin.next()
	await message.reply('Имя, фамилия, отчество?', reply_markup=ReplyKeyboardRemove())

async def load_name(message : types.Message, state:FSMContext):
	async with state.proxy() as data:
		data['name'] = message.text
	await FSMAdmin.next()
	await message.reply('Вес?')

async def load_weight(message : types.Message, state:FSMContext):
	async with state.proxy() as data:
		data['weight'] = message.text
	await FSMAdmin.next()
	await message.reply('Рост?')

async def load_height(message : types.Message, state:FSMContext):
	async with state.proxy() as data:
		data['height'] = message.text

	await sqlite_db.sql_add(state)

	await state.finish()

	await bot.send_message(message.from_user.id, "Ah, shit, here we go again", reply_markup=kb_1)

'''async def cancel_state(message : types.Message, state: FSMContext):
	current_state = await state.get_state()
	if current_state is None:
		return
	await state.finish()
	await bot.send_message(message.from_user.id, 'Back to start!', reply_markup=kb_1)
	await message.delete()'''

def register_handlers_dopros(dp : Dispatcher):
	dp.register_message_handler(fsm_start, commands=['Допрос'], state=None) #def+commands
	dp.register_message_handler(load_name, state=FSMAdmin.name)
	dp.register_message_handler(load_weight, state=FSMAdmin.weight)
	dp.register_message_handler(load_height, state=FSMAdmin.height)
	#dp.register_message_handler(cancel_state, state="*", commands='return')
	#dp.register_message_handler(cancel_state, Text(equals='/return', ignore_case=True), state="*")