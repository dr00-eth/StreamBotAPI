from streambotapi import StreamBotAPI
from streambot import StreamBot
import os

streambot = StreamBot(os.getenv('OPENAI_KEY'), "Paisley", genesis_prompt="You are a helpful spanish translation assistant.")

api = StreamBotAPI(streambot, port=8001)

server = api.start()