import os


class PdfFile:

  def __init__(self, filepath: str) -> None:
    self.filepath = filepath

  def remove(self) -> None:
    os.remove(self.filepath)
