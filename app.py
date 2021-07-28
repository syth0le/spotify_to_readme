import spotipy as spoty
from spotipy.oauth2 import SpotifyOAuth
import pprint

from config import SpotifyConfig
from utility import CurrentPlayingMusic

spotify = spoty.Spotify(auth_manager=SpotifyOAuth(scope=SpotifyConfig.SCOPE,
                                                  client_id=SpotifyConfig.CLIENT_ID,
                                                  client_secret=SpotifyConfig.CLIENT_SECRET,
                                                  redirect_uri=SpotifyConfig.REDIRECT_URI,
                                                  username=SpotifyConfig.USERNAME))

if __name__ == "__main__":
    current_playing = spotify.current_user_playing_track()
    current = CurrentPlayingMusic(current_playing).print_music()
    # print(current_playing)
    # print('currently_playing_type', smt['currently_playing_type'])
    # print('actions', smt['actions'])
    # print('is_playing', smt['is_playing'])
    # print('context', smt['context'])
    # print('timestamp', smt['timestamp'])
    # print(current_playing['item'].keys())
    # print(current_playing)
