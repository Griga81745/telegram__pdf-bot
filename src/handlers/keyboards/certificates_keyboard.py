from aiogram.types import (
  KeyboardButton,
  ReplyKeyboardMarkup
)


def certificates_keyboard() -> ReplyKeyboardMarkup:
  buttons = [
      [KeyboardButton('Helix')],
      [KeyboardButton('Назад')]
  ]; return ReplyKeyboardMarkup(buttons, resize_keyboard=True)
