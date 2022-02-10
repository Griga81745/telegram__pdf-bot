from aiogram.types import (
  KeyboardButton,
  ReplyKeyboardMarkup
)


def update_keyboard() -> ReplyKeyboardMarkup:
  buttons = [
    [KeyboardButton('Имя'), KeyboardButton('Фамилия'), KeyboardButton('Пол')],
    [KeyboardButton('Дата рождения'), KeyboardButton('Серия/Номер паспорта'), KeyboardButton('Дата создания отчёта')],
    [KeyboardButton('Дата взятия образца'), KeyboardButton('Дата валидации'), KeyboardButton('Дата регистрации')],
    [KeyboardButton('Адрес')],
    [KeyboardButton('Готово'), KeyboardButton('Отменить')]
  ]; return ReplyKeyboardMarkup(buttons, resize_keyboard=True)
