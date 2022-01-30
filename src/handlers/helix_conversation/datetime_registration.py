from src.states import PdfState
from .validators import date_validator
from ..keyboards import update_keyboard

from asyncio import gather
from datetime import datetime
from aiogram.types import Message
from aiogram.dispatcher import FSMContext


@date_validator('%Y.%m.%d', 'Задайте datetime_registration (Г.М.Д)\n2021.12.31', True)
async def datetime_registration(message: Message, state: FSMContext, date: datetime) -> None:

  async with state.proxy() as data:
    data['datetime_registration'] = date

    response_text = 'Изменить данные:\n'
    response_text += '\n'.join(f'{key}: <code>{str(value)}</code>' for key, value in data.as_dict().items())

  await gather(*[
    PdfState.next(),
    message.answer(response_text, parse_mode='HTML', reply_markup=update_keyboard())
  ])
