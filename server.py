from flask import Flask, Response, jsonify, render_template, redirect, request

from app import spotify, get_current_music
from html_generation import HTML

app = Flask(__name__)


@app.route("/")
def get_song_card():
    current_music = get_current_music(spotify)
    generator = HTML(current_music)
    rendered_data = generator.gen_html()
    return render_template("card.html", **rendered_data)


if __name__ == "__main__":
    app.run(debug=True, port=5003)
