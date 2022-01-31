from aiogram.types import (
  KeyboardButton,
  ReplyKeyboardMarkup
)


def payment_keyboard() -> ReplyKeyboardMarkup:
  buttons = [
    [KeyboardButton('Оплатить')],
    [KeyboardButton('Отменить')]
  ]; return ReplyKeyboardMarkup(buttons, resize_keyboard=True)
