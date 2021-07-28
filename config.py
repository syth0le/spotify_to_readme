import os

from dotenv import load_dotenv

load_dotenv(override=True)


class VkConfig:
    VK_TOKEN = os.getenv("VK_TOKEN")
    STATUS = os.getenv("STATUS")
    EMPTY_STATUS = os.getenv("EMPTY_STATUS")


class SpotifyConfig:
    CLIENT_ID = os.getenv("CLIENT_ID")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    REDIRECT_URI = "http://localhost:8888"
    USERNAME = os.getenv("USERNAME")
    SCOPE = os.getenv("SCOPE")