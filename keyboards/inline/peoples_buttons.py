from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Define inline buttons
btn1 = InlineKeyboardButton(text="Ilhomjon", callback_data="ilhomjon")
btn2 = InlineKeyboardButton(text="Ota-onam", callback_data="parents")
btn3 = InlineKeyboardButton(text="Ilhomjon sunnat", callback_data="ilhomjon_sunnat")
btn4 = InlineKeyboardButton(text="Bonu", callback_data="bonu")
btn5 = InlineKeyboardButton(text="Ammam", callback_data="amma")

# Create inline keyboard
people_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [btn1, btn2],   # First row
        [btn3, btn4],          # Second row
        [btn5],          # Second row
    ]
)
