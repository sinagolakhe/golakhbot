#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = "7264464627:AAFF8SXbtGsamZi7w7wTPVHQZSxKhbXjt1Y"

#Your API ID from my.telegram.org
APP_ID = "28453201"

#Your API Hash from my.telegram.org
API_HASH = "2cc29365e02ff750682a9edd5d1ca14e"

#Your db channel Id
CHANNEL_ID = "-1002184727848"

#OWNER ID
OWNER_ID = "7433933634"

#Port
PORT = "8080"

#Database 
DB_URI = "mongodb+srv://shiroshare:shiroshare@golakh.nh074.mongodb.net/?retryWrites=true&w=majority&appName=golakh"
DB_NAME = "golakh"

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = "0"

TG_BOT_WORKERS = ""

#start message
START_MSG = "سلام {first}! با این بات می‌تونی به کار های شیروکامی دسترسی داشته باشی."
try:
    ADMINS="325065205"
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
