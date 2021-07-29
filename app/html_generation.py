from app.utility import CurrentPlayingMusic


class HTML:

    def __init__(self, current_music: CurrentPlayingMusic):
        self._bars = 75
        self._song_max = 27
        self._artist_max = 35
        self.current_music = current_music

    def _gen_div_bar(self) -> str:
        if self.current_music.is_playing:
            return "".join(['<div class="bar"></div>' for _ in range(self._bars)])
        else:
            return ""

    def _gen_status_bar(self) -> str:
        return "Now playing on" if self.current_music.is_playing else "Recently played on"

    def _gen_image(self) -> str:
        IMAGE_TEMPLATE = """
        <a href="{}" target="_BLANK">
            <center>
              <img src="{}" width="300" height="300" class="cover" />
            </center>
        </a>""".format(
            self.current_music.song_url,
            self.current_music.image
        )
        return IMAGE_TEMPLATE

    def _gen_song_title(self):
        if len(self.current_music.name) > self._song_max:
            song_template = """<marquee behavior="scroll" direction="left">{}</marquee>"""\
                .format(self.current_music.name)
        else:
            song_template = self.current_music.name

        if len(self.current_music.artist) > self._artist_max:
            artist_template = self.current_music.artist.split(", ")[0]
        else:
            artist_template = self.current_music.artist

        return song_template, artist_template

    def gen_html(self):
        song_title, artist_name = self._gen_song_title()
        rendered_data = {
            "bars": self._gen_div_bar(),
            "status": self._gen_status_bar(),
            "image": self._gen_image(),
            "title": self._gen_song_title(),
            "song_title": song_title,
            "artist_name": artist_name,
        }
        return rendered_data


