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

  with open('previews/datetime_creation.jpg', 'rb') as file:
    await gather(
      PdfState.next(),
      message.answer_photo(file, caption='Задайте дату создания отчёта (ГГГГ.ММ.ДД Ч:М)\nНапример:2021.12.31 13:30', reply_markup=date_keyboard())
    )
