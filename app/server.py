from flask import Flask, render_template, Response

from app.app import SpotifyMiddleware, auth_manager
from app.html_generation import HTML

app = Flask(__name__)
spotify = SpotifyMiddleware(auth_manager=auth_manager)

FILE = "card.html.j2"
CACHE_FILE = "temp_file.html.j2"


@app.route("/")
def get_song_card():
    try:
        current_music = spotify.get_current_music()
        generator = HTML(current_music)
        rendered_data = generator.gen_html()
        cache_rendered_data = generator.gen_html_cache()
        with open("app/templates/temp_file.html.j2", "w") as w:
            w.write(render_template(FILE, **cache_rendered_data))
        template = render_template(FILE, **rendered_data)
    except TypeError:
        template = render_template(CACHE_FILE)
    response = Response(template, mimetype="image/svg+xml")
    response.headers["Cache-Control"] = "s-maxage=1"
    return response
