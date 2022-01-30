from src.states import PdfState
from ..keyboards import cancel_keyboard

from asyncio import gather
from aiogram.types import Message
from aiogram.dispatcher import FSMContext


async def sex(message: Message, state: FSMContext) -> None:
  message_text = message.text.strip().capitalize()

  if message_text not in ('Мужской', 'Женский'):
    return await message.answer('Вы можете выбрать между Мужской и Женский')

  async with state.proxy() as data:
    data['sex'] = {
      'ru': message_text,
      'en': {'Мужской': 'Male', 'Женский': 'Female'}[message_text]
    }

  await gather(*[
    PdfState.next(),
    message.answer('Выберете дату рождения', reply_markup=cancel_keyboard())
  ])
