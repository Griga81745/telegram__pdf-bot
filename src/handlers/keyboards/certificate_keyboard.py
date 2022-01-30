from aiogram.types import (
  InlineKeyboardButton,
  InlineKeyboardMarkup
)


def certificate_keyboard(certificate: str) -> InlineKeyboardMarkup:
  buttons = [
      [InlineKeyboardButton('Получить', callback_data=f'c_{certificate}')]
  ]; return InlineKeyboardMarkup(inline_keyboard=buttons)
