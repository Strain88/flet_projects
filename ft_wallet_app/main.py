import flet as ft  # type: ignore
from app import App


def start(page: ft.Page) -> None:
    page.title = "Wallite"
    page.vertical_alignment = ft.CrossAxisAlignment.START
    page.window_width = 320
    page.window_height = 600
    page.scroll = ft.ScrollMode.AUTO
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0
    page.update()

    app = App()
    page.add(app)


if __name__ == "__main__":
    ft.app(target=start, assets_dir="./assets")
