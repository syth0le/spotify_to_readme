from flask import Flask, render_template

from app.app import SpotifyMiddleware, auth_manager
from app.html_generation import HTML

app = Flask(__name__)
spotify = SpotifyMiddleware(auth_manager=auth_manager)

FILE = "card.html.j2"


@app.route("/")
def get_song_card():
    current_music = spotify.get_current_music()
    generator = HTML(current_music)
    rendered_data = generator.gen_html()
    return render_template(FILE, **rendered_data)
