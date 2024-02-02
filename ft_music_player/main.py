import flet as ft  # type: ignore
from views.playlist import Playlist
from views.currentsong import CurrentSong


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.window_width = 320
    page.window_height = 800

    def router(route):
        page.views.clear()

        if page.route == "/playlist":
            playlist = Playlist(page)
            page.views.append(playlist)

        if page.route == "/song":
            song = CurrentSong(page)
            page.views.append(song)

        page.update()

    page.on_route_change = router
    page.go("/playlist")


ft.app(target=main, assets_dir="assets")
