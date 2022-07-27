import aiohttp
import logging
from pyrogram import Client
from config import Config
from telethon import TelegramClient


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

LOGGER = logging.getLogger(__name__)

bot = Client("pmbot", bot_token=os.getenv("BOT_TOKEN"), api_hash=os.getenv("API_HASH"), api_id=int(os.getenv("API_ID")),)
tele = TelegramClient("telethon", Config.API_ID, Config.API_HASH)
aiohttpsession = aiohttp.ClientSession()

