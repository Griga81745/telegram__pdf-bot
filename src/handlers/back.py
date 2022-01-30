from .keyboards import start_keyboard
from aiogram.types import Message


async def back(message: Message) -> None:
  await message.answer('Стартовое меню', reply_markup=start_keyboard())
