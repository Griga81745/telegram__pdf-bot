from .validators import date_validator

from asyncio import gather
from src.states import PdfState

from datetime import datetime
from aiogram.types import Message
from aiogram.dispatcher import FSMContext


@date_validator('%Y.%m.%d', 'Задайте datetime_result_report (Г.М.Д)\n2021.12.31', True)
async def datetime_result_report(message: Message, state: FSMContext, date: datetime) -> None:

  async with state.proxy() as data:
    data['datetime_result_report'] = date

  await gather(
    PdfState.next(),
    message.answer('Задайте datetime_registration (Г.М.Д)\n2021.12.31')
  )
