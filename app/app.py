from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from app.config import SpotifyConfig
from app.utility import CurrentPlayingMusic

auth_manager = SpotifyOAuth(scope=SpotifyConfig.SCOPE,
                            client_id=SpotifyConfig.CLIENT_ID,
                            client_secret=SpotifyConfig.CLIENT_SECRET,
                            redirect_uri=SpotifyConfig.REDIRECT_URI,
                            username=SpotifyConfig.USERNAME)


class SpotifyMiddleware(Spotify):

    def get_current_music(self) -> CurrentPlayingMusic:
        current_playing = self.current_user_playing_track()
        current_cls = CurrentPlayingMusic(current_playing)
        return current_cls
