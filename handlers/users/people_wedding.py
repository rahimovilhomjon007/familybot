from aiogram import F
from aiogram.types import CallbackQuery

from loader import dp


@dp.callback_query(F.data == "ilhomjon")
async def people_wedding(call: CallbackQuery):
    await call.message.answer("😜 Hozircha mavjud emas")


@dp.callback_query(F.data == "dilfuz")
async def people_wedding(call: CallbackQuery):
    await call.message.answer_video(video="BAACAgIAAxkBAAIBBmkdjFNHx01DGvygviK-d3PfnXgQAAJ8ewACSvPpSFlrfehKsUsjNgQ")


@dp.callback_query(F.data == "parents")
async def people_wedding(call: CallbackQuery):
    # await call.message.answer("👌 marhamat")
    # video file_id ni qo'yish kerak
    await call.message.answer_video(video="BAACAgIAAxkBAAIBBmkdjFNHx01DGvygviK-d3PfnXgQAAJ8ewACSvPpSFlrfehKsUsjNgQ")


@dp.callback_query(F.data == "ilhomjon_sunnat")
async def people_wedding(call: CallbackQuery):
    await call.message.answer_video(video="BAACAgIAAxkBAAIBBmkdjFNHx01DGvygviK-d3PfnXgQAAJ8ewACSvPpSFlrfehKsUsjNgQ")


@dp.callback_query(F.data == "bonu")
async def people_wedding(call: CallbackQuery):
    await call.message.answer_video(video="BAACAgIAAxkBAAIBBmkdjFNHx01DGvygviK-d3PfnXgQAAJ8ewACSvPpSFlrfehKsUsjNgQ")


@dp.callback_query(F.data == "amma")
async def people_wedding(call: CallbackQuery):
    await call.message.answer_video(video="BAACAgIAAxkBAAIBBmkdjFNHx01DGvygviK-d3PfnXgQAAJ8ewACSvPpSFlrfehKsUsjNgQ")
