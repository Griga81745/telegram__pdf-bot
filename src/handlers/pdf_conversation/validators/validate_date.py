from typing import Union
from datetime import datetime


def validate_date(string: str, date_format: str) -> Union[None, datetime]:

  try:
    return datetime.strptime(string, date_format)
  except ValueError:
    return None
