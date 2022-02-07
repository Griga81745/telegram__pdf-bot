from .entry_point import entry_point
from .cancel import cancel
from .name import name
from .surname import surname
from .sex import sex
from .location import location
from .date_of_birth import date_of_birth
from .passport_number import passport_number
from .datetime_creation import datetime_creation
from .datetime_sample_collection import datetime_sample_collection
from .datetime_result_report import datetime_result_report
from .datetime_registration import datetime_registration
from .confirmation import confirmation
from .promo_code import promo_code
from .payment import payment
from .confirm_payment import confirm_payment
from .pre_checkout_query import pre_checkout_query

from src.states import PdfState
from src.settings.settings import PROMO_CODE

from aiogram import Dispatcher
from aiogram.types import ContentType
from aiogram.dispatcher.filters import Text


def register_pdf_conversation_handlers(dispatcher: Dispatcher) -> None:
  dispatcher.register_callback_query_handler(entry_point, lambda c: c.data == 'c_helix')
  dispatcher.register_message_handler(cancel, Text(equals='Отменить'), state='*')
  dispatcher.register_message_handler(name, state=PdfState.name)
  dispatcher.register_message_handler(surname, state=PdfState.surname)
  dispatcher.register_message_handler(sex, state=PdfState.sex)
  dispatcher.register_message_handler(location, state=PdfState.location)
  dispatcher.register_message_handler(date_of_birth, state=PdfState.date_of_birth)
  dispatcher.register_message_handler(passport_number, state=PdfState.passport_number)
  dispatcher.register_message_handler(datetime_creation, state=PdfState.datetime_creation)
  dispatcher.register_message_handler(datetime_sample_collection, state=PdfState.datetime_sample_collection)
  dispatcher.register_message_handler(datetime_result_report, state=PdfState.datetime_result_report)
  dispatcher.register_message_handler(datetime_registration, state=PdfState.datetime_registration)
  dispatcher.register_message_handler(confirmation, state=PdfState.confirmation)
  dispatcher.register_message_handler(promo_code, Text(equals=PROMO_CODE), state=PdfState.payment)
  dispatcher.register_message_handler(payment, state=PdfState.payment)
  dispatcher.register_message_handler(confirm_payment, content_types=ContentType.SUCCESSFUL_PAYMENT, state=PdfState.confirm_payment)
  dispatcher.register_pre_checkout_query_handler(pre_checkout_query, state=PdfState.confirm_payment)


__all__ = ('register_pdf_conversation_handlers',)
