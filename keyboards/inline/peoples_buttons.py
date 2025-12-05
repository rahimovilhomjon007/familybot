from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Define inline buttons
btn1 = InlineKeyboardButton(text="Ilhomjon", callback_data="ilhomjon")
btn21 = InlineKeyboardButton(text="Ota-onam", callback_data="parents")
btn2 = InlineKeyboardButton(text="dilfuza", callback_data="dilfuz")
btn3 = InlineKeyboardButton(text="Ilhomjon sunnat", callback_data="ilhomjon_sunnat")
btn4 = InlineKeyboardButton(text="Bonu", callback_data="bonu")
btn5 = InlineKeyboardButton(text="Ammam", callback_data="amma")

# Create inline keyboard
people_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [btn1, btn21],   # First row
        [btn2, btn3],          # Second row
        [btn5, btn4],          # Second row
    ]
)
