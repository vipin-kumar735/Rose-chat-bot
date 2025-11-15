import os

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
Rose_API_KEY = os.environ.get("Rose_API_KEY")
Rose_API_URL = os.environ.get(
    "Rose_API_URL",
    "https://esproapi-9e00fce70d45.herokuapp.com"
)
DEFAULT_MODEL = os.environ.get("DEFAULT_MODEL", "")
