from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from datetime import datetime
from typing import Callable, Coroutine, Any


def date_validator(date_format: str, error_message: str, now_possible: bool = False) -> Callable:

  def decorator(function: Coroutine) -> Coroutine:

    async def wrapper(message: Message, state: FSMContext) -> Any:
      message_text = message.text.strip()

      if now_possible:
        date = datetime.now()
      else:

        try:
          date = datetime.strptime(message_text, date_format)
        except ValueError:
          return await message.answer(error_message)

      return await function(message, state, date)

    return wrapper

  return decorator
