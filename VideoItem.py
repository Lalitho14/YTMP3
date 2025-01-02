import flet as ft
from pytubefix import YouTube
from AlertaSucces import AlertaDescarga

class VideoItem(ft.Row):
  def __init__(self, path, url, page):
    super().__init__()
    self.page = page
    self.path = path
    self.video = YouTube(url)
    self.info = ft.Text(self.video.title)
    self.info_edit = ft.TextField(self.video.title, visible=False, on_submit=self.SaveTitle)
    self.btn_descargar = ft.IconButton(
      icon=ft.Icons.DOWNLOAD,
      icon_color=ft.Colors.WHITE,
      bgcolor=ft.Colors.BLUE_900,
      tooltip="Descargar esta cancion",
      on_click=self.DownloadVideo
    )
    self.btn_edit = ft.IconButton(
      icon=ft.Icons.EDIT,
      icon_color=ft.Colors.WHITE,
      bgcolor=ft.Colors.BLUE_900,
      tooltip="Editar titulo",
      on_click=self.EditTitle
    )
    self.btn_save = ft.IconButton(
      icon=ft.Icons.SAVE,
      icon_color=ft.Colors.WHITE,
      bgcolor=ft.Colors.BLUE_900,
      tooltip="Guardar titulo",
      visible=False,
      on_click=self.SaveTitle
    )

    self.controls = [
      self.info,
      self.info_edit,
      self.btn_descargar,
      self.btn_edit,
      self.btn_save
    ]

    self.spacing = 25
    self.alignment = ft.MainAxisAlignment.CENTER
    self.vertical_alignment = ft.CrossAxisAlignment.CENTER

  def DownloadVideo(self, e):
    try:
      download = self.video.streams.get_audio_only()
      download.download(output_path=self.path,
                        filename=self.info.value + ".mp3")
      self.btn_descargar.visible = False
      self.btn_edit.visible = False
      self.info.value += "[ Descargado ]"
      self.info.color = ft.Colors.GREEN_500
      self.page.update()
      modal = AlertaDescarga("Descarga Completa", page=self.page)
      self.page.open(modal)
    except:
      modal = AlertaDescarga("Error en Descarga", page=self.page)
      self.page.open(modal)

  def EditTitle(self, e):
    self.info.visible = False
    self.btn_descargar.visible = False
    self.btn_edit.visible = False
    self.info_edit.visible = True
    self.btn_save.visible = True
    self.page.update()

  def SaveTitle(self, e):
    self.info.visible = True
    self.btn_descargar.visible = True
    self.btn_edit.visible = True
    self.info_edit.visible = False
    self.btn_save.visible = False
    self.info.value = self.info_edit.value
    self.page.update()
