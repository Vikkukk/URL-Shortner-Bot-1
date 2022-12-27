import os
from pyrogram import Client


bot_token = os.environ.get("5870865507:AAHE0fOTqboGP41g2hflvdnQNzxwmAfQzBQ")
api_id = int(os.environ.get("16869866"))
api_hash = os.environ.get("b6defd08178346ef6d0539e4db127acf")
plugins = dict(root="plugins")

Bot = Client(
    "URL-Shortner-Bot",
    bot_token=bot_token,
    api_id=api_id,
    api_hash=api_hash,
    plugins=plugins,
    workers=50,
    sleep_threshold=10
)

Bot.run()
