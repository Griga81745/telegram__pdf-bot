from src.states import PdfState
from ..keyboards import cancel_keyboard

from asyncio import gather
from aiogram.types import CallbackQuery


async def entry_point(callback_query: CallbackQuery) -> None:
  await gather(*[
    PdfState.name.set(),
    callback_query.answer('💚'),
    callback_query.message.answer('Введите имя', reply_markup=cancel_keyboard())
  ])
