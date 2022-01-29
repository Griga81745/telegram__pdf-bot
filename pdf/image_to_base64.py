import os
import base64


def image_to_base64(path: str) -> bytes:
  if not os.path.exists(path):
    raise FileNotFoundError(path)

  with open(path, 'rb') as file:
    return base64.b64encode(file.read()).decode()
