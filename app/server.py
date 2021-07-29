from flask import Flask, render_template

from app.app import get_current_music, spotify
from app.html_generation import HTML

app = Flask(__name__)

FILE = "card.html"


@app.route("/")
def get_song_card():
    current_music = get_current_music(spotify)
    generator = HTML(current_music)
    rendered_data = generator.gen_html()
    return render_template(FILE, **rendered_data)
