from .keyboards import certificate_keyboard
from aiogram.types import Message


async def helix(message: Message) -> None:

  with open('previews/helix_preview.pdf', 'rb') as file:
    await message.answer_document(file, reply_markup=certificate_keyboard('helix'))
