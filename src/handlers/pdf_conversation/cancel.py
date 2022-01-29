from asyncio import gather
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove


async def cancel(message: Message, state: FSMContext) -> None:

  if await state.get_state() is None:
    return

  await gather(*[
    state.finish(),
    message.answer('Отановлено', reply_markup=ReplyKeyboardRemove())
  ])
