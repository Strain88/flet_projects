import flet as ft  # type: ignore
# from song import Song, AudioDirectory  # type: ignore


class CurrentSong(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__(
            route="/song",
            horizontal_alignment="center",
            vertical_alignment="center"
        )

        self.page = page
        self.song = self.page.session.get("song")
        self.create_audio_track()

        self.duration: int = 0
        self.start: int = 0
        self.end: int = 0

        self.is_playing: bool = False

        self.txt_start = ft.Text(self.format_time(self.start))
        self.txt_end = ft.Text(f"-{self.format_time(self.start)}")

        self.slider = ft.Slider(
            min=0,
            thumb_color="transparent",
            on_change_end=lambda e: self.toggle_seek(
                round(float(e.data))
            )
        )

        self.back_btn = ft.TextButton(
            content=ft.Text(
                value="Playlist",
                color="black" if self.page.theme_mode == ft.ThemeMode.LIGHT
                else "white",
            ),
            on_click=self.toggle_playlist,
        )

        self.play_btn = self.create_toggle_button(
            ft.icons.PLAY_ARROW_ROUNDED, 2, self.play,
        )

        self.controls = [
            ft.Row(
                controls=[
                    self.back_btn
                ],
                alignment="start",
            ),
            ft.Container(
                height=120,
                expand=True,
                border_radius=8,
                shadow=ft.BoxShadow(
                    spread_radius=8,
                    blur_radius=10,
                    color=ft.colors.with_opacity(0.35, "black")
                ),
                image_fit="cover",
                image_src=self.song.path_img,
            ),
            ft.Divider(
                height=10,
                color="transparent",
            ),
            ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Text(
                                self.song.name,
                                size=18,
                                weight="bold",
                            ),
                            ],
                    ),
                    ft.Row(
                        controls=[
                            ft.Text(
                                self.song.artist,
                                size=15,
                                opacity=0.81,
                            ),
                            ],
                    ),
                ],
                spacing=1,
            ),
            ft.Divider(
                height=10,
                color="transparent",
            ),
            ft.Column(
                controls=[
                    ft.Row(
                        [self.txt_start, self.txt_end],
                        alignment="spaceBetween",
                    ),
                    self.slider,
                ],
                spacing=0,
            ),
            ft.Divider(
                height=10,
                color="transparent",
            ),
            ft.Row(
                controls=[
                    self.create_toggle_button(
                        ft.icons.REPLAY_10_SHARP,
                        0.9,
                        lambda e: self.__update_position(-5000)
                    ),
                    self.play_btn,
                    self.create_toggle_button(
                        ft.icons.FORWARD_10_SHARP,
                        0.9,
                        lambda e: self.__update_position(5000)
                    ),

                ],
                alignment="spaceEvently"
            ),
            ft.Divider(
                height=10,
                color="transparent",
            ),
        ]

    def play(self, e: ft.TapEvent):
        self.toggle_play_pause()
        self.duration = self.audio.get_duration()
        self.end = self.duration
        self.slider.max = self.duration

    def toggle_play_pause(self, event=None):
        if self.is_playing:
            self.play_btn.icon = ft.icons.PLAY_ARROW_ROUNDED
            self.audio.pause()
        else:
            self.play_btn.icon = ft.icons.PAUSE_ROUNDED
            try:
                self.audio.resume()
            except Exception:
                self.audio.play()

        self.is_playing = False if self.is_playing else True

        # self.play_btn.on_click = self.toggle_play_pause()
        self.play_btn.update()

    def __update_start_end(self):
        if self.start < 0:
            self.start = 0

        if self.end > self.duration:
            self.end = self.duration

    def __update_position(self, delta: int):
        self.__update_start_end()

        if self.start > 0:
            if delta == 5000:
                pos_change = 5000
            elif delta == -5000:
                pos_change = -5000

            pos: int = self.start + pos_change
            self.audio.seek(pos)

            self.start += pos_change
            self.end -= pos_change

    def __update_time_stamp(self, start: int, end: int):
        self.txt_start.value = self.format_time(start)
        self.txt_end.value = f"-{self.format_time(end)}"

        self.txt_start.update()
        self.txt_end.update()

    def format_time(self, value: int):
        milliseconds = value
        minutes, seconds = divmod(milliseconds/1000, 60)
        formatted_time = f"{int(minutes):02}:{int(seconds):02}"
        return formatted_time

    def __update_slider(self, delta: int):
        self.slider.value = delta
        self.slider.update()

    def toggle_seek(self, delta):
        self.start = delta
        self.end = self.duration - delta

        self.audio.seek(self.start)
        self.__update_slider(delta)

    def __update(self, delta: int):
        self.start += 1000
        self.end -= 1000

        self.__update_slider(delta)
        self.__update_time_stamp(self.start, self.end)

    def create_audio_track(self):
        self.audio = ft.Audio(
            src=self.song.path,
            on_position_changed=lambda e: self.__update(int(e.data)),
        )

        self.page.overlay.append(self.audio)

    def create_toggle_button(self, icon, scale, function) -> ft.IconButton:
        return ft.IconButton(
            icon=icon,
            scale=scale,
            on_click=function,
        )

    def toggle_playlist(self, e: ft.TapEvent):
        self.audio.pause()
        self.page.session.clear()
        self.page.go("/playlist")
