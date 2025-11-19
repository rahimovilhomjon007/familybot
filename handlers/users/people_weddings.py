from aiogram import types

from loader import dp


@dp.message(lambda message: message.text == "To'ylar")
async def send_hello(msg: types.Message):
    await msg.answer("Va alaykum salom")

