import flet as ft
from pytubefix import YouTube


class VideoItem(ft.Row):
  def __init__(self, path, url):
    super().__init__()
    self.path = path
    self.video = YouTube(url)
    self.info = ft.Text(self.video.title)
    self.btn_descargar = ft.IconButton(
      icon=ft.Icons.DOWNLOAD,
      icon_color=ft.Colors.WHITE,
      bgcolor=ft.Colors.BLUE_900,
      tooltip="Descargar esta cancion"
    )

    self.controls = [
      self.info,
      self.btn_descargar
    ]

    self.spacing = 25
    self.alignment = ft.MainAxisAlignment.CENTER
    self.vertical_alignment = ft.CrossAxisAlignment.CENTER
