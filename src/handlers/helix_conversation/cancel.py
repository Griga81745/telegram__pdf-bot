from ..keyboards import start_keyboard

from asyncio import gather
from aiogram.types import Message
from aiogram.dispatcher import FSMContext


async def cancel(message: Message, state: FSMContext) -> None:

  if await state.get_state() is None:
    return

  await gather(*[
    state.finish(),
    message.answer('Отановлено', reply_markup=start_keyboard())
  ])
