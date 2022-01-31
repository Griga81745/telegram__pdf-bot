from aiogram.types import Message


async def offer(message: Message) -> None:
  await message.answer('https://vrbank.ru/docs/7.pdf')
