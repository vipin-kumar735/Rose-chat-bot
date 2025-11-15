import os

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
ESPRO_API_KEY = os.environ.get("ESPRO_API_KEY")
ESPRO_API_URL = os.environ.get(
    "ESPRO_API_URL",
    "https://esproapi-9e00fce70d45.herokuapp.com"
)
DEFAULT_MODEL = os.environ.get("DEFAULT_MODEL", "")
