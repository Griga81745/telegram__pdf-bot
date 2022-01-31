from pdf import PdfMaker
from ..keyboards import start_keyboard

from asyncio import create_task
from aiogram.types import Message
from aiogram.dispatcher import FSMContext


async def confirm_payment(message: Message, state: FSMContext) -> None:
  if message.successful_payment.invoice_payload == 'buy_pdf_without_watermark':
    create_task(message.answer('Отправка...'))

    async with state.proxy() as data:

      async with PdfMaker(**data.as_dict(), watermark=False) as file:
        await message.answer_document(file, reply_markup=start_keyboard())

  await state.finish()
