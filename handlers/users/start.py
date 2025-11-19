from aiogram import types
from aiogram.filters import CommandStart

from keyboards.default import menu_btn
from loader import dp


@dp.message(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=menu_btn)
