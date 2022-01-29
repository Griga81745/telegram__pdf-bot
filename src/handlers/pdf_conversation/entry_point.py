from src.states import PdfState

from aiogram.types import (
  Message,
  KeyboardButton,
  ReplyKeyboardMarkup
)


async def entry_point(message: Message) -> None:
  await PdfState.name.set()

  keyboard = ReplyKeyboardMarkup([[KeyboardButton('Отменить')]], resize_keyboard=True)
  await message.answer('Введите имя', reply_markup=keyboard)
