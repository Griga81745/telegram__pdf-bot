from aiogram.types import (
  KeyboardButton,
  ReplyKeyboardMarkup
)


def start_keyboard() -> ReplyKeyboardMarkup:
  buttons = [
      [KeyboardButton('Сертификаты 📄')],
      [KeyboardButton('Оферта 📌')]
  ]; return ReplyKeyboardMarkup(buttons, resize_keyboard=True)
