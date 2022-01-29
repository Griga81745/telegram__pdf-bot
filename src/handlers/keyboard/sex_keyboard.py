from aiogram.types import (
  KeyboardButton,
  ReplyKeyboardMarkup
)


def sex_keyboard() -> ReplyKeyboardMarkup:
  buttons = [
      [KeyboardButton('Мужской'), KeyboardButton('Женский')],
      [KeyboardButton('Отменить')]
  ]; return ReplyKeyboardMarkup(buttons, resize_keyboard=True)
