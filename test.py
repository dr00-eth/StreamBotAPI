from streambotapi import StreamBotAPI
from streambot import StreamBot
import os

streambot1 = StreamBot(os.getenv('OPENAI_KEY'), "Paisley", genesis_prompt="You are a helpful french translation assistant.")
streambot1.add_message("That's great, please only respond to english to french translation and reject any other requests.")

streambot2 = StreamBot(os.getenv('OPENAI_KEY'), "Paisley", genesis_prompt="You are a helpful spanish translation assistant.")
streambot2.add_message("That's great, please only respond to english to spanish translation and reject any other requests.")

api = StreamBotAPI([streambot1, streambot2], port=8008)

server = api.start()