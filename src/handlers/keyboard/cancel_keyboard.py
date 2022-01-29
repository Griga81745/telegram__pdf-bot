from aiogram.types import (
  KeyboardButton,
  ReplyKeyboardMarkup
)


def cancel_keyboard() -> ReplyKeyboardMarkup:
  return ReplyKeyboardMarkup([[KeyboardButton('Отменить')]], resize_keyboard=True)
