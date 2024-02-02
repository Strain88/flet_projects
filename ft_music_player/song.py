class Song:
    def __init__(
            self,
            song_name: str,
            artist_name: str,
            audio_path: str,
            img_path: str,
            ) -> None:
        self.song_name = song_name
        self.artist_name = artist_name
        self.audio_path = audio_path
        self.img_path = img_path

    @property
    def name(self) -> str:
        return self.song_name

    @property
    def artist(self) -> str:
        return self.artist_name

    @property
    def path(self) -> str:
        return self.audio_path

    @property
    def path_img(self) -> str:
        return self.img_path


class AudioDirectory:
    playlist: list = [
        Song(
            song_name="Юморист",
            artist_name="Face",
            audio_path="../assets/humor.mp3",
            img_path="../assets/1.jpg"
        ),
        Song(
            song_name="Yes, for Money",
            artist_name="Instasamka",
            audio_path="../assets/samka.mp3",
            img_path="../assets/2.jpg"
        ),
    ]
