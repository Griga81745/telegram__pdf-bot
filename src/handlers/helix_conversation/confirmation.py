from pdf import PdfMaker
from .validators import Updates
from ..keyboards import payment_keyboard

from src.states import PdfState
from aiogram.types import Message
from aiogram.dispatcher import FSMContext


async def confirmation(message: Message, state: FSMContext) -> None:
  if message.text != 'Готово':
    updates = Updates(message, state)
    return await updates.run()

  async with state.proxy() as data:
    await message.answer('Отправка...')

    async with PdfMaker(**data.as_dict()) as file:
      await message.answer_document(file, reply_markup=payment_keyboard())

  await PdfState.next()
