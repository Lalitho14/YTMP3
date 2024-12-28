import flet as ft
from Downloader import DescargarMP3
from AlertaSucces import AlertaDescarga
from VideoItem import VideoItem


def main(page: ft.Page):
  page.title = "Descargar Musica YouTube"
  page.window.width = 1000
  page.window.height = 700
  page.padding = 10
  page.bgcolor = ft.Colors.BLACK87
  page.theme_mode = ft.ThemeMode.DARK
  page.theme = ft.Theme(
    color_scheme_seed=ft.Colors.BLUE,
    visual_density=ft.VisualDensity.COMFORTABLE,
    color_scheme=ft.ColorScheme(
        primary=ft.Colors.BLUE,
        secondary=ft.Colors.ORANGE,
        background=ft.Colors.GREY_900,
        surface=ft.Colors.GREY_800
    )
  )

  folder_selected = ft.Ref[str]()
  lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)

  def SetUrl(e):
    url.value = e.data
    vi = VideoItem(url=url.value, path=folder_selected.current)
    list_container.visible = True
    lv.controls.append(vi)
    page.update()

  url = ft.SearchBar(
    view_elevation=4,
    divider_color=ft.Colors.PRIMARY,
    bar_hint_text="URL del video a convertir..",
    view_hint_text="URL de video YT",
    on_submit=SetUrl
  )

  anuncio = ft.Text(value="", visible=False)

  def FolderHandler(e: ft.FilePickerResultEvent):
    if e.path:
      folder_selected.current = e.path
      folder_selected.current = folder_selected.current.replace('\\', '\\\\')
      anuncio.value = "Carpeta Seleccionada: " + e.path
      anuncio.visible = True
      page.update()

  folder_picker = ft.FilePicker(on_result=FolderHandler)
  page.overlay.append(folder_picker)

  opciones_view = ft.Column(
    controls=[
      ft.Text(
        value="Comienza a descargar",
        size=28,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.BLUE_200,
      ),
      ft.ElevatedButton(
        text="Selecciona folder para guardar",
        icon=ft.Icons.FOLDER,
        color=ft.Colors.WHITE,
        bgcolor=ft.Colors.BLUE_900,
        on_click=lambda _: folder_picker.get_directory_path()
      ),
      anuncio,
      url,
    ],
    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    spacing=30
  )

  list_container = ft.Container(
    content=ft.Column(
      controls=[
        lv], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=30
    ),
    alignment=ft.alignment.center,
    expand=True,
    border=ft.border.all(5, ft.Colors.PINK_900),
    border_radius=ft.border_radius.all(30),
    visible=False
  )

  page.add(
    ft.Container(
      content=opciones_view,
      alignment=ft.alignment.center,
      expand=True,
      border=ft.border.all(5, ft.Colors.BLUE_900),
      border_radius=ft.border_radius.all(30)
    ),
    list_container
  )


if __name__ == "__main__":
  ft.app(target=main)
