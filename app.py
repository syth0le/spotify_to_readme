import spotipy as spoty
from spotipy.oauth2 import SpotifyOAuth
import pprint
import webbrowser

from config import SpotifyConfig
from template import template
from utility import CurrentPlayingMusic

spotify = spoty.Spotify(auth_manager=SpotifyOAuth(scope=SpotifyConfig.SCOPE,
                                                  client_id=SpotifyConfig.CLIENT_ID,
                                                  client_secret=SpotifyConfig.CLIENT_SECRET,
                                                  redirect_uri=SpotifyConfig.REDIRECT_URI,
                                                  username=SpotifyConfig.USERNAME))


def edit_html_template(template, artist, name, image):
    with open("card.html", "w") as w:
        DATA = template

        DATA = DATA.replace("@ARTIST", str(artist))
        DATA = DATA.replace("@SONG", str(name))
        DATA = DATA.replace("@IMAGE", image)

        w.write(DATA)


if __name__ == "__main__":
    current_playing = spotify.current_user_playing_track()
    current_cls = CurrentPlayingMusic(current_playing)
    current_cls.print_music()

    artist, name, image = current_cls.return_to_template()

    edit_html_template(template, artist, name, image)

    webbrowser.open('card.html')
