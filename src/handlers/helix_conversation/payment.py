from src.states import PdfState
from src.settings import settings
from src.settings.telegram_bot import telegram_bot

from aiogram.dispatcher import FSMContext
from aiogram.types import (
  Message,
  LabeledPrice
)


async def payment(message: Message, state: FSMContext) -> None:

  if message.text.strip().lower() == 'оплатить':
    await telegram_bot.send_invoice(
      chat_id=message.from_user.id,
      title='Покупка PDF',
      description='Текст с офертой',
      payload='buy_pdf_without_watermark',
      provider_token=settings.YMONEY_TOKEN,
      currency='rub',
      start_parameter='test_bot',
      prices=[LabeledPrice('ПДФ', 100000)]
    )
  else:
    return await message.answer('Нет такой оплаты')

  await PdfState.next()
