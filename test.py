from streambotapi import StreamBotAPI
from streambot import StreamBot
import os

streambot = StreamBot(os.getenv('OPENAI_KEY'), "Paisley", genesis_prompt="You are a helpful spanish translation assistant.")
streambot.add_message("That's great, please only respond to english to spanish translation and reject any other requests.")

api = StreamBotAPI(streambot, port=8008)

server = api.start()