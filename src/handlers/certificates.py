from .keyboards import certificates_keyboard
from aiogram.types import Message


async def certificates(message: Message) -> None:
  await message.answer('Список сертификатов ⬇️', reply_markup=certificates_keyboard())
