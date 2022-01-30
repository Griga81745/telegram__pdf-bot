from .validate_date import validate_date

from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from datetime import datetime
from typing import Callable, Coroutine, Any


def date_validator(date_format: str, error_message: str, now_possible: bool = False) -> Callable:

  def decorator(function: Coroutine) -> Coroutine:

    async def wrapper(message: Message, state: FSMContext) -> Any:
      message_text = message.text.strip()

      if now_possible and message_text == 'Сейчас':
        date = datetime.now()
      else:

        if not (date := validate_date(message_text, date_format)):
          return await message.answer(error_message)

      return await function(message, state, date)

    return wrapper

  return decorator
