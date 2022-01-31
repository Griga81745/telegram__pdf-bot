from src.states import PdfState
from ..keyboards import cancel_keyboard

from asyncio import gather
from aiogram.types import CallbackQuery


async def entry_point(callback_query: CallbackQuery) -> None:
  with open('previews/personal_info.jpg', 'rb') as file:
    await gather(*[
      PdfState.name.set(),
      callback_query.answer('💚'),
      callback_query.message.answer_photo(file, caption='Введите имя', reply_markup=cancel_keyboard())
    ])
