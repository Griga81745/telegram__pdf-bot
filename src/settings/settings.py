from ..utils import get_env_var
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

TG_TOKEN = get_env_var('TG_TOKEN')
YMONEY_TOKEN = get_env_var('YTOKEN')

PROMO_CODE = get_env_var('PROMO_CODE')
