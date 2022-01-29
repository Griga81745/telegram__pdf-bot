from .colored import colored_error
from typing import Any

import sys
from os import environ


def get_env_var(variable_name: str) -> Any:

  try:
    return environ[variable_name]
  except KeyError:
    colored_error(f"Can't load {variable_name}. It should be added to environment variables")
    sys.exit(1)
