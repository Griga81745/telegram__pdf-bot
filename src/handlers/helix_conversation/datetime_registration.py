from src.states import PdfState
from .validators import date_validator
from ..keyboards import update_keyboard

from asyncio import gather
from datetime import datetime
from aiogram.types import Message
from aiogram.dispatcher import FSMContext


@date_validator('%Y.%m.%d', 'Задайте дату регистрации (Г.М.Д)\n2021.12.31', True)
async def datetime_registration(message: Message, state: FSMContext, date: datetime) -> None:

  async with state.proxy() as data:
    data['datetime_registration'] = date

    response_text = 'Изменить данные:\n'
    response_text += (
      f"Имя:{data['name']['ru']}\n"
      f"Фамилия:{data['surname']['ru']}\n"
      f"Пол: {data['sex']['ru']}\n"
      f"Адрес: {data['location']}\n"
      f"Номер паспорта: {data['passport_number']}\n"
      f"Дата рождения: {data['date_of_birth']}\n"
      f"Дата регистрации: {data['datetime_registration']}\n"
      f"Дата взятия образца: {data['datetime_sample_collection']}\n"
      f"Дата создания отчёта: {data['datetime_creation']}\n"
      f"Дата валидации: {data['datetime_result_report']}"
    )

  await gather(*[
    PdfState.next(),
    message.answer(response_text, parse_mode='HTML', reply_markup=update_keyboard())
  ])
