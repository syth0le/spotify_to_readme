from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from config import SpotifyConfig
from utility import CurrentPlayingMusic

spotify = Spotify(auth_manager=SpotifyOAuth(scope=SpotifyConfig.SCOPE,
                                            client_id=SpotifyConfig.CLIENT_ID,
                                            client_secret=SpotifyConfig.CLIENT_SECRET,
                                            redirect_uri=SpotifyConfig.REDIRECT_URI,
                                            username=SpotifyConfig.USERNAME))


def edit_html_template(template, artist, name, image, song_url, is_playing):
    with open("templates/card.html", "w") as w:
        DATA = template

        DATA = DATA.replace("@ARTIST", str(artist))
        DATA = DATA.replace("@SONG", str(name))
        DATA = DATA.replace("@IMAGE", image)
        if is_playing:
            status_string = "Now playing on"
            DATA = DATA.replace("@BARS", BARS)
        else:
            status_string = "Recently played on"
            DATA = DATA.replace("@BARS", "")
        DATA = DATA.replace("@NOW_RECENTLY", status_string)
        print(song_url)
        DATA = DATA.replace("@URL_SONG", song_url)
        w.write(DATA)


def get_current_music(spoty: Spotify):
    current_playing = spoty.current_user_playing_track()
    current_cls = CurrentPlayingMusic(current_playing)
    return current_cls
