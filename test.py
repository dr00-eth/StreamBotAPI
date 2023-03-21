from streambotapi import StreamBotAPI
from streambot import StreamBot
import constants
import os
import logging

# Create a logger object
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('your_log_file.log')
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

#Prompt 0 - Listing Bot
streambot1 = StreamBot(os.getenv('OPENAI_KEY'), "Paisley", genesis_prompt=constants.OPENAI_PROMPT[0], verbosity=1)

#Prompt 1 - Neighborhood Bot
streambot2 = StreamBot(os.getenv('OPENAI_KEY'), "Paisley", genesis_prompt=constants.OPENAI_PROMPT[1], verbosity=1)

#Prompt 2 - Coaching Bot
streambot3 = StreamBot(os.getenv('OPENAI_KEY'), "Paisley", genesis_prompt=constants.OPENAI_PROMPT[2], verbosity=1)

#Prompt 3 - Follow Up Bot
streambot4 = StreamBot(os.getenv('OPENAI_KEY'), "Paisley", genesis_prompt=constants.OPENAI_PROMPT[3], verbosity=1)


api = StreamBotAPI([streambot1,streambot2, streambot3, streambot4], origins=["http://localhost:3000","https://paisley-ui-hycvm.ondigitalocean.app"], verbosity=1, debug=True, port=8008, allow_model_override=True)

server = api.start()