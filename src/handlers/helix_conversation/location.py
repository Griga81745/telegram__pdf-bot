from src.states import PdfState
from ..keyboards import cancel_keyboard

from asyncio import gather
from aiogram.types import Message
from aiogram.dispatcher import FSMContext


async def location(message: Message, state: FSMContext) -> None:

  async with state.proxy() as data:
    data['location'] = message.text.strip()

  with open('previews/personal_info.jpg', 'rb') as file:
    await gather(*[
      PdfState.next(),
      message.answer_photo(file, caption='Выберете дату рождения (ГГГГ.ММ.ДД)', reply_markup=cancel_keyboard())
    ])
