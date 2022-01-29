from ..utils import colored_info, get_user
from aiogram.types import Message


async def start_help(message: Message):
  colored_info(get_user(message), message.text)
  await message.answer('Wassup')
