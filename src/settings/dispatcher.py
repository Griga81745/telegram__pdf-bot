from ..handlers import (
  start_help,
  register_pdf_conversation_handlers
)

from ..states import PdfState
from .telegram_bot import telegram_bot

from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
dispatcher = Dispatcher(telegram_bot, storage=storage)

dispatcher.register_message_handler(start_help, commands=['start', 'help'])
register_pdf_conversation_handlers(dispatcher)
