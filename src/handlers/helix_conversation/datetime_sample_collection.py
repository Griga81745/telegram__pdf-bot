from .validators import date_validator

from asyncio import gather
from src.states import PdfState

from datetime import datetime
from aiogram.types import Message
from aiogram.dispatcher import FSMContext


@date_validator('%Y.%m.%d', 'Задайте дату взятия образца (ГГГГ.ММ.ДД)\nСегодня: 2021.12.31', True)
async def datetime_sample_collection(message: Message, state: FSMContext, date: datetime) -> None:

  async with state.proxy() as data:
    data['datetime_sample_collection'] = date

  await gather(*[
    PdfState.next(),
    message.answer('Задайте дату валидации (ГГГГ.ММ.ДД)\nСейчас: 2021.12.31')
  ])
