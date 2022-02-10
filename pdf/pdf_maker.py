from .sync_to_async import sync_to_async

from .random_filename import random_filename
from .image_to_base64 import image_to_base64

import os
import pdfkit

from io import BytesIO
from base64 import b64encode

import qrcode
from datetime import date
from random import randint

from typing import Any
from jinja2 import Template


class PdfMaker:
  qr_url = 'https://helix.cov-ld.ru?{params}'
  html_path = 'html/page.html'

  def __init__(
    self,
    name: str,
    surname: str,
    sex: str,
    location: str,
    date_of_birth: str,
    passport_number: str,
    datetime_creation: str,
    datetime_sample_collection: str,
    datetime_result_report: str,
    datetime_registration: str,
    operation: str = 'Оплата',
    watermark: bool = True,
  ) -> None:

    self.data = {
      'document_number': randint(1, 99),
      'operation': operation,
      'name': name,
      'surname': surname,
      'sex': sex,
      'location': location,
      'date_of_birth': date_of_birth,
      'passport_number': passport_number,
      'datetime_creation': datetime_creation,
      'datetime_sample_collection': datetime_sample_collection,
      'datetime_result_report': datetime_result_report,
      'datetime_registration': datetime_registration,
      'watermark': watermark
    }

    if not os.path.exists('results/'):
      os.mkdir('results/')

  def get_age(self) -> int:
    today = date.today()
    birth = self.data['date_of_birth']
    return today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))

  @sync_to_async
  def __make_pdf(self) -> str:
    template = Template(self.get_html_code(self.html_path))
    result_html = template.render(data=self.data, images=image_to_base64, watermark=self.data['watermark'], qr_code=self.get_qr_code(), age=self.get_age())

    result_path = f'./results/{random_filename()}.pdf'
    pdfkit.from_string(result_html, result_path)
    return result_path

  def get_html_code(self, path: str) -> str:
    with open(path, 'r') as file:
      return file.read()

  def __getitem__(self, key: Any) -> Any:
    return self.data[key]

  def __setitem__(self, key: Any, value: Any) -> None:
    self.data[key] = value

  async def __aenter__(self) -> bytes:
    result_path = await self.__make_pdf()
    self.file_path = result_path
    self.file_object = open(result_path, 'rb')
    return self.file_object

  async def __aexit__(self, *args) -> None:
    self.file_object.close()
    os.remove(self.file_path)

  def get_qr_code(self) -> str:
    name = self.data['name']['en']
    surname = self.data['surname']['en']

    fields = {
      'sample_collection': self.data['datetime_sample_collection'].strftime('%Y.%m.%d'),
      'birth': self.data['date_of_birth'].strftime('%Y.%m.%d'),
      'patient': f'{surname[0].upper()}***{surname[-1].lower()} {name[0].upper()}'
    }

    params = '&'.join(f'{key}={value}' for key, value in fields.items())
    final_url = self.qr_url.format(params=params)

    qr = qrcode.make(final_url, box_size=25)
    qr.save(result := BytesIO())

    result = BytesIO(result.getvalue())
    return b64encode(result.read()).decode()
