from .validators import date_validator

from asyncio import gather
from src.states import PdfState

from datetime import datetime
from aiogram.types import Message
from aiogram.dispatcher import FSMContext


@date_validator('%Y.%m.%d', 'Задайт дату валидации (ГГГГ.ММ.ДД)\nСейчас: 2021.12.31', True)
async def datetime_result_report(message: Message, state: FSMContext, date: datetime) -> None:

  async with state.proxy() as data:
    data['datetime_result_report'] = date

  with open('previews/datetime_registration.jpg', 'rb') as file:
    await gather(
      PdfState.next(),
      message.answer_photo(file, caption='Задайте дату регистрации (Г.М.Д)\nСейчас: 2021.12.31')
    )
