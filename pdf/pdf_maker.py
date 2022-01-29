from .pdf_file import PdfFile
from .sync_to_async import sync_to_async

from .random_filename import random_filename
from .image_to_base64 import image_to_base64

import os
import pdfkit

from typing import Any
from jinja2 import Template



class PdfMaker:
  html_path = 'html/page.html'

  def __init__(
    self,
    document_number: int,
    operation: str,
    name: str,
    surname: str,
    sex: str,
    date_of_birth: str,
    passport_number: str,
    datetime_creation: str,
    datetime_sample_collection: str,
    datetime_result_report: str,
    datetime_registration: str,
    watermark: bool = True,
  ) -> None:

    self.data = {
      'document_number': document_number,
      'operation': operation,
      'name': name,
      'surname': surname,
      'sex': sex,
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

  @sync_to_async
  def __make_pdf(self) -> str:
    template = Template(self.get_html_code(self.html_path))
    result_html = template.render(data=self.data, images=image_to_base64, watermark=self.data['watermark'])

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

  async def __aenter__(self) -> PdfFile:
    result_path = await self.__make_pdf()
    self.file = PdfFile(result_path)
    return self.file

  async def __aexit__(self, *args) -> None:
    self.file.remove()
