from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Define buttons
btn1 = KeyboardButton(text="To'ylar")
btn2 = KeyboardButton(text="inlines")
btn3 = KeyboardButton(text="Yopish")

# Create keyboard
menu_btn = ReplyKeyboardMarkup(
    keyboard=[
        [btn1, btn2],   # First row
        [btn3]          # Second row
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
