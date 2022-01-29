from ..states import PdfState
from ..utils import translit_to_english

from aiogram.dispatcher import FSMContext

from pdf import PdfMaker
from datetime import datetime

from aiogram.types import (
  Message,
  KeyboardButton,
  ReplyKeyboardMarkup,
  ReplyKeyboardRemove
)


async def pdf_entry_point(message: Message) -> None:
  await PdfState.name.set()

  keyboard = ReplyKeyboardMarkup(
    [
      [KeyboardButton('Отменить')]
    ],
    resize_keyboard=True
  )

  await message.answer('Введите имя', reply_markup=keyboard)


async def pdf_cancel(message: Message, state: FSMContext) -> None:

  if await state.get_state() is None:
    return

  await state.finish()
  await message.answer('Остановлено', reply_markup=ReplyKeyboardRemove())


async def pdf_process_name(message: Message, state: FSMContext) -> None:

  async with state.proxy() as data:
    data['name'] = {
      'ru': message.text,
      'en': translit_to_english(message.text)
    }

  await PdfState.next()
  await message.answer('Введите фамилию')


async def pdf_process_surname(message: Message, state: FSMContext) -> None:

  async with state.proxy() as data:
    data['surname'] = {
      'ru': message.text,
      'en': translit_to_english(message.text)
    }

  keyboard = ReplyKeyboardMarkup(
    [
      [KeyboardButton('Мужской'), KeyboardButton('Женский')],
      [KeyboardButton('Отменить')]
    ],
    resize_keyboard=True
  )

  await PdfState.next()
  await message.answer('Выберете пол', reply_markup=keyboard)


async def pdf_process_sex(message: Message, state: FSMContext) -> None:
  if message.text not in ['Мужской', 'Женский']:
    await message.answer('Вы можете выбрать только Мужской или Женский пол')
    return

  async with state.proxy() as data:
    data['sex'] = {
      'ru': message.text,
      'en': {'Мужской': 'Male', 'Женский': 'Female'}[message.text]
    }

  keyboard = ReplyKeyboardMarkup(
    [
      [KeyboardButton('Отменить')]
    ],
    resize_keyboard=True
  )

  await PdfState.next()
  await message.answer('Выберете дату рождения в формате (Г.М.Д)', reply_markup=keyboard)


async def pdf_process_birth_date(message: Message, state: FSMContext) -> None:

  try:
    birth_date = datetime.strptime(message.text, '%Y.%m.%d')
  except ValueError:
    await message.answer('Неверный формат даты. Должно быть ГОД.МЕСЯЦ.ДЕНЬ\nНапример: 2000.12.25')
    return

  async with state.proxy() as data:
    data['date_of_birth'] = birth_date

  await PdfState.next()
  await message.answer('Введите данные паспорта (СЕРИЯ НОМЕР)\nНапример: 75 2852735')


async def process_passport_number(message: Message, state: FSMContext) -> None:
  if len(message.text) != 10:
    await message.answer('Введите данные паспорта (СЕРИЯ НОМЕР)\nНапример: 75 2852735')
    return

  async with state.proxy() as data:
    data['passport_number'] = message.text

  keyboard = ReplyKeyboardMarkup(
    [
      [KeyboardButton('Сейчас')],
      [KeyboardButton('Отменить')]
    ],
    resize_keyboard=True
  )

  await PdfState.next()
  await message.answer('Задайте datetime_creation (Г.М.Д)\n2021.12.31', reply_markup=keyboard)


async def process_datetime_creation(message: Message, state: FSMContext) -> None:

  if message.text == 'Сейчас':
    date = datetime.now()
  else:

    try:
      date = datetime.strptime(message.text, '%Y.%m.%d')
    except ValueError:
      await message.answer('Задайте datetime_creation (Г.М.Д)\n2021.12.31')
      return

  async with state.proxy() as data:
    data['datetime_creation'] = date

  await PdfState.next()
  await message.answer('Задайте datetime_sample_collection (Г.М.Д)\n2021.12.31')


async def process_datetime_sample_collection(message: Message, state: FSMContext):

  if message.text == 'Сейчас':
    date = datetime.now()
  else:

    try:
      date = datetime.strptime(message.text, '%Y.%m.%d')
    except ValueError:
      await message.answer('Задайте datetime_sample_collection (Г.М.Д)\n2021.12.31')
      return

  async with state.proxy() as data:
    data['datetime_sample_collection'] = date

  await PdfState.next()
  await message.answer('Задайте datetime_result_report (Г.М.Д)\n2021.12.31')


async def process_datetime_result_report(message: Message, state: FSMContext):

  if message.text == 'Сейчас':
    date = datetime.now()
  else:

    try:
      date = datetime.strptime(message.text, '%Y.%m.%d')
    except ValueError:
      await message.answer('Задайте datetime_result_report (Г.М.Д)\n2021.12.31')
      return

  async with state.proxy() as data:
    data['datetime_result_report'] = date

  await PdfState.next()
  await message.answer('Задайте datetime_registration (Г.М.Д)\n2021.12.31')


async def process_datetime_registration(message: Message, state: FSMContext):

  if message.text == 'Сейчас':
    date = datetime.now()
  else:

    try:
      date = datetime.strptime(message.text, '%Y.%m.%d')
    except ValueError:
      await message.answer('Задайте datetime_registration (Г.М.Д)\n2021.12.31')
      return

  await message.answer('Отправка...')

  async with state.proxy() as data:
    data['datetime_registration'] = date

    async with PdfMaker(**data.as_dict()) as file:
      await message.answer_document(file)

  await state.finish()
