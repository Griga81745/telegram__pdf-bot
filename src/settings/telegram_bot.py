from ..utils import colored_error
from .settings import TG_TOKEN

import sys
from aiogram import Bot
from aiogram.utils.exceptions import ValidationError

try:
  telegram_bot = Bot(TG_TOKEN)
except ValidationError:
  colored_error('Token validation failed')
  sys.exit(1)
