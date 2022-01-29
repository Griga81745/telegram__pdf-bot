from aiogram.types import (
  KeyboardButton,
  ReplyKeyboardMarkup
)


def update_keyboard() -> ReplyKeyboardMarkup:
  buttons = [
    [KeyboardButton('Имя'), KeyboardButton('Фамилия'), KeyboardButton('Пол')],
    [KeyboardButton('Дата рождения'), KeyboardButton('Серия/Номер паспорта'), KeyboardButton('Datetime creation')],
    [KeyboardButton('Datetime collection'), KeyboardButton('Datetime result'), KeyboardButton('Datetime registration')],
    [KeyboardButton('Готово'), KeyboardButton('Отменить')]
  ]; return ReplyKeyboardMarkup(buttons, resize_keyboard=True)
