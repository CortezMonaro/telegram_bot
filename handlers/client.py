from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_1
from aiogram.types import ReplyKeyboardRemove

#@dp.message_handler(commands=['start', 'restart'])
async def command_start(message : types.Message):
	try:
		await bot.send_message(message.from_user.id, 'Good morning', reply_markup=kb_1)
		await message.delete()
	except:
		await message.reply('Write to the bot, dumbass!')


def register_handlers_client(dp : Dispatcher):
	dp.register_message_handler(command_start, commands=['start']) 
	
	