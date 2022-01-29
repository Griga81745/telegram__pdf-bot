from aiogram.dispatcher.filters.state import State, StatesGroup


class PdfState(StatesGroup):
  name = State()
  surname = State()
  sex = State()
  date_of_birth = State()
  passport_number = State()
  datetime_creation = State()
  datetime_sample_collection = State()
  datetime_result_report = State()
  datetime_registration = State()
