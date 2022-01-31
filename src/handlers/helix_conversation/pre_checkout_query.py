from aiogram.types import PreCheckoutQuery
from src.settings.telegram_bot import telegram_bot


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery) -> None:
  await telegram_bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)
