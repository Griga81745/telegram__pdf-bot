from pdf import PdfMaker
from .validators import Updates

from aiogram.dispatcher import FSMContext
from aiogram.types import (
  Message,
  ReplyKeyboardRemove
)


async def confirmation(message: Message, state: FSMContext) -> None:
  if message.text != 'Готово':
    updates = Updates(message, state)
    return await updates.run()

  async with state.proxy() as data:
    await message.answer('Отправка...')

    async with PdfMaker(**data.as_dict()) as file:
      await message.answer_document(file, reply_markup=ReplyKeyboardRemove())

  await state.finish()
