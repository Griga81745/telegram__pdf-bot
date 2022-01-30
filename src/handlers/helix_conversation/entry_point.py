from src.states import PdfState
from ..keyboards import cancel_keyboard

from aiogram.types import Message


async def entry_point(message: Message) -> None:
  await PdfState.name.set()
  await message.answer('Введите имя', reply_markup=cancel_keyboard())
