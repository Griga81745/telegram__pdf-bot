from ..handlers import (
  start_help,

  pdf_entry_point,
  pdf_cancel,
  pdf_process_name,
  pdf_process_surname,
  pdf_process_sex,
  pdf_process_birth_date,
  process_passport_number,
  process_datetime_creation,
  process_datetime_sample_collection,
  process_datetime_result_report,
  process_datetime_registration
)

from ..states import PdfState
from .telegram_bot import telegram_bot

from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
dispatcher = Dispatcher(telegram_bot, storage=storage)

dispatcher.register_message_handler(start_help, commands=['start', 'help'])

dispatcher.register_message_handler(pdf_entry_point, commands=['pdf'])
dispatcher.register_message_handler(pdf_cancel, Text(equals='Отменить'), state='*')
dispatcher.register_message_handler(pdf_process_name, state=PdfState.name)
dispatcher.register_message_handler(pdf_process_surname, state=PdfState.surname)
dispatcher.register_message_handler(pdf_process_sex, state=PdfState.sex)
dispatcher.register_message_handler(pdf_process_birth_date, state=PdfState.date_of_birth)
dispatcher.register_message_handler(process_passport_number, state=PdfState.passport_number)
dispatcher.register_message_handler(process_datetime_creation, state=PdfState.datetime_creation)
dispatcher.register_message_handler(process_datetime_sample_collection, state=PdfState.datetime_sample_collection)
dispatcher.register_message_handler(process_datetime_result_report, state=PdfState.datetime_result_report)
dispatcher.register_message_handler(process_datetime_registration, state=PdfState.datetime_registration)
