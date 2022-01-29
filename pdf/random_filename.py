from random import choice

LETTERS = {chr(unicode) for unicode in range(ord('a'), ord('z') + 1)}
NUMBERS = {number for number in range(0, 10)}
SYMBOLS = LETTERS | NUMBERS | {letter.upper() for letter in LETTERS}
SYMBOLS = [str(symbol) for symbol in SYMBOLS]


def random_filename(length: int = 5) -> str:
  return ''.join(choice(SYMBOLS) for _ in range(length))
