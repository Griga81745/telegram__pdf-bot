from ..utils import colored_info, get_user
from .keyboards import start_keyboard
from aiogram.types import Message


async def start_help(message: Message) -> None:
  colored_info(get_user(message), message.text)
  await message.answer('Стартовое сообщение', reply_markup=start_keyboard())
