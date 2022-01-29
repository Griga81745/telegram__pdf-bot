from src.states import PdfState
from src.utils import translit_to_english
from ..keyboard import sex_keyboard

from asyncio import gather
from aiogram.dispatcher import FSMContext

from aiogram.types import (
  Message,
  KeyboardButton,
  ReplyKeyboardMarkup
)


async def surname(message: Message, state: FSMContext) -> None:
  message_text = message.text.strip().title()

  async with state.proxy() as data:
    data['surname'] = {
      'ru': message_text,
      'en': translit_to_english(message_text)
    }

  await gather(*[
    PdfState.next(),
    message.answer('Выберете Пол', reply_markup=sex_keyboard())
  ])