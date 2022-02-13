from .validators import date_validator

from asyncio import gather
from src.states import PdfState

from datetime import datetime
from aiogram.types import Message
from aiogram.dispatcher import FSMContext


@date_validator('%Y.%m.%d %H:%M', 'Задайт дату валидации (ГГГГ.ММ.ДД Ч:М)\nНапример: 2021.12.31 13:30', True)
async def datetime_result_report(message: Message, state: FSMContext, date: datetime) -> None:

  async with state.proxy() as data:
    data['datetime_result_report'] = date

  with open('previews/datetime_registration.jpg', 'rb') as file:
    await gather(
      PdfState.next(),
      message.answer_photo(file, caption='Задайте дату регистрации (ГГГГ.ММ.ДД Ч:М)\nНапример: 2021.12.31 13:30')
    )
