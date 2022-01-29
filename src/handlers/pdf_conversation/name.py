from src.states import PdfState
from src.utils import translit_to_english

from asyncio import gather
from aiogram.types import Message
from aiogram.dispatcher import FSMContext


async def name(message: Message, state: FSMContext) -> None:
  message_text = message.text.strip().title()

  async with state.proxy() as data:
    data['name'] = {
      'ru': message_text.title(),
      'en': translit_to_english(message_text)
    }

  await gather(*[
    PdfState.next(),
    message.answer('Введите фамилию')
  ])
