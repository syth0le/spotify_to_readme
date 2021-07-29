import os

from dotenv import load_dotenv

load_dotenv(override=True)


class SpotifyConfig:
    CLIENT_ID = os.getenv("CLIENT_ID")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    REDIRECT_URI = "http://localhost:8888"
    USERNAME = os.getenv("USERNAME")
    SCOPE = os.getenv("SCOPE")