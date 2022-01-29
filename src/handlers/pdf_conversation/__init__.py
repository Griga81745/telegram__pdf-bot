from .entry_point import entry_point
from .cancel import cancel
from .name import name
from .surname import surname
from .sex import sex
from .date_of_birth import date_of_birth
from .passport_number import passport_number
from .datetime_creation import datetime_creation
from .datetime_sample_collection import datetime_sample_collection
from .datetime_result_report import datetime_result_report
from .datetime_registration import datetime_registration

from src.states import PdfState

from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text


def register_pdf_conversation_handlers(dispatcher: Dispatcher) -> None:
  dispatcher.register_message_handler(entry_point, commands=['pdf'])
  dispatcher.register_message_handler(cancel, Text(equals='Отменить'), state='*')
  dispatcher.register_message_handler(name, state=PdfState.name)
  dispatcher.register_message_handler(surname, state=PdfState.surname)
  dispatcher.register_message_handler(sex, state=PdfState.sex)
  dispatcher.register_message_handler(date_of_birth, state=PdfState.date_of_birth)
  dispatcher.register_message_handler(passport_number, state=PdfState.passport_number)
  dispatcher.register_message_handler(datetime_creation, state=PdfState.datetime_creation)
  dispatcher.register_message_handler(datetime_sample_collection, state=PdfState.datetime_sample_collection)
  dispatcher.register_message_handler(datetime_result_report, state=PdfState.datetime_result_report)
  dispatcher.register_message_handler(datetime_registration, state=PdfState.datetime_registration)


__all__ = ('register_pdf_conversation_handlers',)
