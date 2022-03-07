import sqlite3 as sq


def sql_start():
	global base, cur
	base = sq.connect('baza_mayora.db')
	cur = base.cursor()
	if base:
		print('This is working somehow')
	base.execute('CREATE TABLE IF NOT EXISTS baza(name TEXT PRIMARY KEY, weight TEXT, height TEXT)')
	base.execute('CREATE TABLE IF NOT EXISTS days(day TEXT PRIMARY KEY, music TEXT)')
	base.commit()

async def sql_add(state):
	async with state.proxy() as data:
		cur.execute('INSERT INTO baza VALUES (?, ?, ?)', tuple(data.values()))
		base.commit()

async def sql_add2(state):
	async with state.proxy() as data:
		cur.execute('INSERT INTO days VALUES (?, ?)', tuple(data.values()))
		base.commit()