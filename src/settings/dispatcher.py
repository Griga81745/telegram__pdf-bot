from ..handlers import (
  start_help
)

from .telegram_bot import telegram_bot
from aiogram import Dispatcher

dispatcher = Dispatcher(telegram_bot)

dispatcher.register_message_handler(start_help, commands=['start', 'help'])