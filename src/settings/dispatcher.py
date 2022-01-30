from ..handlers import (
  start_help,
  certificates,
  back,
  register_pdf_conversation_handlers
)

from .telegram_bot import telegram_bot

from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
dispatcher = Dispatcher(telegram_bot, storage=storage)

dispatcher.register_message_handler(start_help, commands=['start', 'help'])
dispatcher.register_message_handler(certificates, Text(equals='Сертификаты'))
dispatcher.register_message_handler(back, Text(equals='Назад'))
register_pdf_conversation_handlers(dispatcher)
