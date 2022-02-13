from .validators import date_validator

from asyncio import gather
from src.states import PdfState

from datetime import datetime
from aiogram.types import Message
from aiogram.dispatcher import FSMContext


@date_validator('%Y.%m.%d %H:%M', 'Задайте дату создания отчёта (ГГГГ.ММ.ДД Ч:М)\nНапример: 2021.12.31 13:30', True)
async def datetime_creation(message: Message, state: FSMContext, date: datetime) -> None:

  async with state.proxy() as data:
    data['datetime_creation'] = date

  with open('previews/other_dates.jpg', 'rb') as file:
    await gather(
      PdfState.next(),
      message.answer_photo(file, caption='Задайте дату взятия образца (ГГГГ.ММ.ДД Ч:М)\nСегодня: 2021.12.31 13:30')
    )
