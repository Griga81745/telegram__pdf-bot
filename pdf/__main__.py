from .pdf_maker import PdfMaker
import asyncio


async def main() -> None:
  maker = PdfMaker(
    'Сара',
    'Лайтборн',
    'Женский',
    '1500.02.10',
    '75 2852735',
    '2021.12.31 16:09:27',
    '2021.12.31 16:09:27',
    '2021.12.31 19:26:12',
    '31.12.2021 16:13:53',
    True
  )

  async with maker as file:
    print(file)


if __name__ == '__main__':
  asyncio.run(main())
