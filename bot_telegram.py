from aiogram.utils import executor
from create_bot import dp
from data_base import sqlite_db


async def on_startup(_):
	print("It's alive!")
	sqlite_db.sql_start()

from handlers import client, dopros, opros

client.register_handlers_client(dp)
dopros.register_handlers_dopros(dp)
opros.register_handlers_opros(dp)



executor.start_polling(dp, skip_updates=True, on_startup=on_startup)