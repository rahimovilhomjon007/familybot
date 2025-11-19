from aiogram import types

from keyboards.inline.peoples_buttons import people_buttons
from loader import dp


@dp.message(lambda message: message.text == 'hello')
async def send_hello(msg: types.Message):
    await msg.answer("Va alaykum salom")



@dp.message(lambda message: message.text == "To'ylar")
async def send_hello(msg: types.Message):
    await msg.answer("To'yni tanlang:", reply_markup=people_buttons)