from aiogram.types import Message


def get_user(message: Message) -> str:

  if (username := message.from_user.username):
    return f'@{username}'

  return f'id_{message.from_user.id}'
