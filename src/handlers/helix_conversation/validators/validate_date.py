from typing import Union
from random import randint
from datetime import datetime


def validate_date(string: str, date_format: str) -> Union[None, datetime]:

  try:
    date = datetime.strptime(string, date_format)
    return datetime(
      year=date.year,
      month=date.month,
      day=date.day,
      hour=date.hour,
      minute=date.minute,
      second=randint(1, 59)
      )
  except ValueError:
    return None
