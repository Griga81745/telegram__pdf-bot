from transliterate import translit


def translit_to_english(string: str) -> str:
  return translit(string, 'ru', reversed=True)
