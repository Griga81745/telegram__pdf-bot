from .validators import date_validator

from asyncio import gather
from src.states import PdfState

from datetime import datetime
from aiogram.types import Message
from aiogram.dispatcher import FSMContext


@date_validator('%Y.%m.%d', 'Неверный формат даты. %Y.%m.%d\nНапример 2000.12.25')
async def date_of_birth(message: Message, state: FSMContext, date: datetime) -> None:

  async with state.proxy() as data:
    data['date_of_birth'] = date

  with open('previews/passport_number.jpg', 'rb') as file:
    await gather(*[
      PdfState.next(),
      message.answer_photo(file, caption='Введите данные паспорта (СЕРИЯ НОМЕР)\nНапример: 75 2852735')
    ])
