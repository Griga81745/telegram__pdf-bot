from asyncio import gather
from src.states import PdfState
from ..keyboards import date_keyboard

from aiogram.types import Message
from aiogram.dispatcher import FSMContext


async def passport_number(message: Message, state: FSMContext) -> None:
  message_text = message.text.strip()

  if len(message_text) != 10:
    return await message.answer('Введите данные паспорта (СЕРИЯ НОМЕР)\nНапример: 75 2852735')

  async with state.proxy() as data:
    data['passport_number'] = message_text

  await gather(
    PdfState.next(),
    message.answer('Задайте datetime_creation (Г.М.Д)\n2021.12.31', reply_markup=date_keyboard())
  )
