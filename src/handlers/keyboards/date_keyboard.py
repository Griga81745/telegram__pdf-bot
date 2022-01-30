from aiogram.types import (
  KeyboardButton,
  ReplyKeyboardMarkup
)


def date_keyboard() -> ReplyKeyboardMarkup:
  buttons = [
    [KeyboardButton('Сейчас')],
    [KeyboardButton('Отменить')]
  ]; return ReplyKeyboardMarkup(buttons, resize_keyboard=True)
