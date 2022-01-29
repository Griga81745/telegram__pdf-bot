from .utils import colored_info, colored_error
from .settings import dispatcher, telegram_bot

import asyncio
from aiogram.utils.exceptions import Unauthorized


async def start_bot() -> None:
  colored_info('info', 'Connecting...')

  try:
    bot_info = await telegram_bot.me
    colored_info('info', f'Polling started for {bot_info.first_name}@{bot_info.username}')
    await dispatcher.start_polling()

  except Unauthorized:
    colored_error('Token is invalid')

  finally:
    session = await telegram_bot.get_session()
    await session.close()


def launch() -> None:
  event_loop = asyncio.new_event_loop()
  event_loop.run_until_complete(start_bot())
  event_loop.close()
