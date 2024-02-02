import flet as ft  # type: ignore
from song import Song, AudioDirectory  # type: ignore


class Playlist(ft.View):
    def __init__(self, page: ft.Page) -> None:
        super().__init__(
            route="/playlist",
            horizontal_alignment="center",
        )

        self.page = page
        self.playlist: list[Song] = AudioDirectory.playlist

        self.controls = [
            ft.Row(
                controls=[
                    ft.Text("PLAYLIST", size=21, weight="bold")
                ],
                alignment="center",
            ),
            ft.Divider(height=10, color="transparent"),
        ]

        self.generate_playlist_ui()

    def generate_playlist_ui(self):
        for song in self.playlist:
            self.controls.append(
                self.create_song_row(song)
            )

    def create_song_row(
            self,
            song: Song
            ) -> ft.Container:
        _obj = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Text(f"Title: {song.name}"),
                    ft.Text(f"{song.artist}"),
                ],
                alignment="spaceBetween",
            ),
            data=song,
            padding=10,
            on_click=self.toggle_song,
        )
        return _obj

    def toggle_song(self, e: ft.TapEvent):
        self.page.session.set("song", e.control.data)
        self.page.go("/song")
