from src.states import PdfState

from asyncio import gather
from aiogram.dispatcher import FSMContext

from aiogram.types import (
  Message,
  KeyboardButton,
  ReplyKeyboardMarkup
)


async def sex(message: Message, state: FSMContext) -> None:
  message_text = message.text.strip().capitalize()

  if message_text not in ('Мужской', 'Женский'):
    return await message.answer('Вы можете выбрать между Мужской и Женский')

  async with state.proxy() as data:
    data['sex'] = {
      'ru': message_text,
      'en': {'Мужской': 'Male', 'Женский': 'Female'}[message_text]
    }

  keyboard = ReplyKeyboardMarkup([[KeyboardButton('Отменить')]], resize_keyboard=True)

  await gather(*[
    PdfState.next(),
    message.answer('Выберете дату рождения', reply_markup=keyboard)
  ])
