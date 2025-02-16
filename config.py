# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "14859014"))
API_HASH = getenv("API_HASH", "e635f9ea6d9c8397c34c0f65bf540a8b")
BOT_TOKEN = getenv("BOT_TOKEN", "7018837791:AAEv2AHKwXpJY1kKGXYffdYUKwsYHFc2C2k")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7379452737").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://karauraofficial:WDTStpioolgAgu7o@cluster0.vkalo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002463093492")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002361967961"))
