from .validators import date_validator

from asyncio import gather
from src.states import PdfState

from datetime import datetime
from aiogram.types import Message
from aiogram.dispatcher import FSMContext


@date_validator('%Y.%m.%d', 'Задайте datetime_sample_collection (Г.М.Д)\n2021.12.29', True)
async def datetime_sample_collection(message: Message, state: FSMContext, date: datetime) -> None:

  async with state.proxy() as data:
    data['datetime_sample_collection'] = date

  await gather(*[
    PdfState.next(),
    message.answer('Задайте datetime_result_report (Г.М.Д)\n2021.12.31')
  ])
