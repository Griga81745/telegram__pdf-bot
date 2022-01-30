from .date_validator import validate_date
from src.utils import translit_to_english

from datetime import datetime
from src.handlers.keyboards import (
  update_keyboard,
  sex_keyboard,
  date_keyboard
)

from aiogram.types import Message
from aiogram.dispatcher import FSMContext


class Updates:
  fields = {
    'имя': 'name',
    'фамилия': 'surname',
    'пол': 'sex',
    'дата рождения': 'date_of_birth',
    'серия/номер паспорта': 'passport_number',
    'datetime creation': 'datetime_creation',
    'datetime collection': 'datetime_sample_collection',
    'datetime result': 'datetime_result_report',
    'datetime registration': 'datetime_registration'
  }

  def __init__(self, message: Message, state: FSMContext) -> None:
    self.message, self.state = message, state
    self.message_text = message.text.strip().lower()

  async def run(self) -> None:
    async with self.state.proxy() as data:

      if not 'what_to_update' in data:
        field = self.fields.get(self.message_text)
        if not field: return await self.message.answer(f'Нет поля {self.message_text}')

        data['what_to_update'] = field
        return await getattr(self, f'label_{field}')()

      field = data.pop('what_to_update')

    return await getattr(self, f'update_{field}')(self.message, self.state)

  async def label_name(self) -> None:
    await self.message.answer('Введите новое имя')

  async def update_name(self, message: Message, state: FSMContext) -> None:
    async with state.proxy() as data:
      data['name'] = {
        'ru': message.text.title(),
        'en': translit_to_english(message.text).title()
      }

    await message.answer('Имя обновлено')

  async def label_surname(self) -> None:
    await self.message.answer('Введите новую фамилию')

  async def update_surname(self, message: Message, state: FSMContext) -> None:
    async with state.proxy() as data:
      data['surname'] = {
        'ru': message.text.title(),
        'en': translit_to_english(message.text).title()
      }

    await message.answer('Фамилия обновлена')

  async def label_sex(self) -> None:
    await self.message.answer('Выберете пол', reply_markup=sex_keyboard())

  async def update_sex(self, message: Message, state: FSMContext) -> None:
    message_text = message.text.strip().capitalize()
    async with state.proxy() as data:

      if message_text not in ('Мужской', 'Женский'):
        data['what_to_update'] = 'sex'
        return await message.answer('Вы можете выбрать между Мужской и Женский')

      data['sex'] = {
        'ru': message_text,
        'en': {'Мужской': 'Male', 'Женский': 'Female'}[message_text]
      }
      await message.answer('Пол обновлен', reply_markup=update_keyboard())

  async def label_date_of_birth(self) -> None:
    await self.message.answer('Введите новую дату рождения')

  async def update_date_of_birth(self, message: Message, state: FSMContext) -> None:
    message_text = message.text.strip()
    async with state.proxy() as data:

      if not (date := validate_date(message_text, '%Y.%m.%d')):
        data['what_to_update'] = 'date_of_birth'
        return await message.answer('Неверный формат')

      data['date_of_birth'] = date
      await message.answer('Дата рождения обновлена')

  async def label_passport_number(self) -> None:
    await self.message.answer('Введите новые данные паспорта')

  async def update_passport_number(self, message: Message, state: FSMContext) -> None:
    message_text = message.text.strip()
    async with state.proxy() as data:

      if len(message_text) != 10:
        data['what_to_update'] = 'passport_number'
        return await self.message.answer('Введите новые данные паспорта')

      data['passport_number'] = message_text
      await message.answer('Данные паспорта обновлены')

  async def label_datetime_creation(self) -> None:
    await self.message.answer('Введите новый date creation', reply_markup=date_keyboard())

  async def update_datetime_creation(self, message: Message, state: FSMContext) -> None:
    message_text = message.text.strip()
    async with state.proxy() as data:

      if message_text == 'Сейчас':
        date = datetime.now()

      elif not (date := validate_date(message_text, '%Y.%m.%d')):
        data['what_to_update'] = 'datetime_creation'
        return await message.answer('Неверный формат')

      data['datetime_creation'] = date
      await message.answer('datetime created обновлен', reply_markup=update_keyboard())

  async def label_datetime_sample_collection(self) -> None:
    await self.message.answer('Введите новый datetime sample collection', reply_markup=date_keyboard())

  async def update_datetime_sample_collection(self, message: Message, state: FSMContext) -> None:
    message_text = message.text.strip()
    async with state.proxy() as data:

      if message_text == 'Сейчас':
        date = datetime.now()

      elif not (date := validate_date(message_text, '%Y.%m.%d')):
        data['what_to_update'] = 'datetime_sample_collection'
        return await message.answer('Неверный формат')

      data['datetime_sample_collection'] = date
      await message.answer('datetime sample collection обновлен', reply_markup=update_keyboard())

  async def label_datetime_result_report(self) -> None:
    await self.message.answer('Введите новый datetime result report', reply_markup=date_keyboard())

  async def update_datetime_result_report(self, message: Message, state: FSMContext) -> None:
    message_text = message.text.strip()
    async with state.proxy() as data:

      if message_text == 'Сейчас':
        date = datetime.now()

      elif not (date := validate_date(message_text, '%Y.%m.%d')):
        data['what_to_update'] = 'datetime_result_report'
        return await message.answer('Неверный формат')

      data['datetime_result_report'] = date
      await message.answer('datetime result report обновлен', reply_markup=update_keyboard())

  async def label_datetime_registration(self) -> None:
    await self.message.answer('Введите новый datetime registration', reply_markup=date_keyboard())

  async def update_datetime_registration(self, message: Message, state: FSMContext) -> None:
    message_text = message.text.strip()
    async with state.proxy() as data:

      if message_text == 'Сейчас':
        date = datetime.now()

      elif not (date := validate_date(message_text, '%Y.%m.%d')):
        data['what_to_update'] = 'datetime_registration'
        return await message.answer('Неверный формат')

      data['datetime_registration'] = date
      await message.answer('datetime registration обновлен', reply_markup=update_keyboard())
