from .validators import date_validator

from pdf import PdfMaker
from asyncio import create_task

from datetime import datetime
from aiogram.dispatcher import FSMContext

from aiogram.types import (
  Message,
  ReplyKeyboardRemove
)


@date_validator('%Y.%m.%d', 'Задайте datetime_registration (Г.М.Д)\n2021.12.31', True)
async def datetime_registration(message: Message, state: FSMContext, date: datetime) -> None:
  create_task(message.answer('Отправка...'))

  async with state.proxy() as data:
    data['datetime_registration'] = date

    async with PdfMaker(**data.as_dict()) as file:
      await message.answer_document(file, reply_markup=ReplyKeyboardRemove())

  await state.finish()
