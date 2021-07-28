class CurrentPlayingMusic:
    def __init__(self, cp):
        self.name = cp["item"]["name"]
        self.artist = ', '.join([artist["name"] for artist in cp["item"]["artists"]])
        self.album = cp["item"]["album"]["name"]
        self.image = cp["item"]["album"]["images"][0]['url']
        self.progress_ms = cp["progress_ms"]
        self.duration_ms = cp["item"]["duration_ms"]
        self.song_url = cp["item"]["external_urls"]["spotify"]
        self.album_url = cp["item"]["album"]["external_urls"]["spotify"]
        self.artist_url = cp["item"]["artists"][0]["external_urls"]["spotify"]
        try:
            self.playlist_url = cp["context"]["external_urls"]["spotify"]
        except:
            self.playlist_url = self.song_url
        self.is_playing = cp["is_playing"]
        self.status = cp["actions"]["disallows"]

        self.cp = cp

    def print_music(self):
        print("\n",
              self.name, "\n",
              self.artist, "\n",
              self.album, "\n",
              self.song_url, "\n",
              self.album_url, "\n",
              self.artist_url, "\n",
              self.playlist_url, "\n",
              self.image, "\n",
              self.is_playing, "\n",
              self.progress_ms, "\n",
              self.duration_ms,"\n",
              self.status
              )
