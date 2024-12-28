import flet as ft


class AlertaDescarga(ft.AlertDialog):
  def __init__(self, text, page):
    super().__init__()
    self.page = page
    self.modal = True
    self.title = ft.Text("Descargando...")
    self.content = ft.Text(text)
    self.actions = [ft.TextButton("Ok", on_click=self.handle_close)]
    self.actions_alignment = ft.MainAxisAlignment.END

  def handle_close(self,e):
    self.page.close(self)