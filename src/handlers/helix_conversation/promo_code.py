from pdf import PdfMaker
from ..keyboards import start_keyboard

from asyncio import create_task
from aiogram.types import Message
from aiogram.dispatcher import FSMContext


async def promo_code(message: Message, state: FSMContext) -> None:
  create_task(message.answer('Отправка...'))

  async with state.proxy() as data:

      async with PdfMaker(**data.as_dict(), watermark=False) as file:
        await message.answer_document(file, reply_markup=start_keyboard())

  await state.finish()
