# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "9002178"))
API_HASH = getenv("API_HASH", "a315441ae0890980db3be9d404bc3c59")
BOT_TOKEN = getenv("BOT_TOKEN", "2029907704:AAGbD6_C8rRhV0D8Zfyun6pVtk6-H89XdDY")
OWNER_ID = list(map(int, getenv("OWNER_ID", "953267481").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://ajay:ajaytia05@ajay.ddt9w.mongodb.net/?retryWrites=true&w=majority&appName=ajay")
LOG_GROUP = getenv("LOG_GROUP", "")
CHANNEL_ID = int(getenv("CHANNEL_ID", ""))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", None)
INSTA_COOKIES = getenv("INSTA_COOKIES", None)
