import re
from os import environ
import asyncio
import json
from collections import defaultdict
from typing import Dict, List, Union
from pyrogram import Client
from time import time
from Script import script

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.strip().lower() in ["on", "true", "yes", "1", "enable", "y"]:
        return True
    elif value.strip().lower() in ["off", "false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
PORT = environ.get("PORT", "8080")
WEBHOOK = bool(environ.get("WEBHOOK", True)) # for web support on/off
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
PICS = (environ.get('PICS' ,'https://telegra.ph/file/517bc12dd5c1347df10f6.jpg')).split()
BOT_START_TIME = time()
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', 0))

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '0').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_grp = environ.get('AUTH_GROUP')
auth_channel = environ.get('AUTH_CHANNEL')
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')
MAX_RIST_BTNS = int(environ.get('MAX_RIST_BTNS', "10"))

# Script Import Direct
START_MESSAGE = environ.get('START_MESSAGE', '👋 𝙷𝙴𝙻𝙾 {user}\n\n𝙼𝚈 𝙽𝙰𝙼𝙴 𝙸𝚂 {bot},\n𝙸 𝙲𝙰𝙽 𝙿𝚁𝙾𝚅𝙸𝙳𝙴 𝙼𝙾𝚅𝙸𝙴𝚂, 𝙹𝚄𝚂𝚃 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 𝙰𝙽𝙳 𝙼𝙰𝙺𝙴 𝙼𝙴 𝙰𝙳𝙼𝙸𝙽...')
BUTTON_LOCK_TEXT = environ.get("BUTTON_LOCK_TEXT", script.BUTTON_LOCK_TEXT)
FORCE_SUB_TEXT = environ.get('FORCE_SUB_TEXT', script.FORCE_SUB_TEXT)
WELCOM_PIC = environ.get("WELCOM_PIC", '')
WELCOM_TEXT = environ.get("WELCOM_TEXT", 'Hai {user}\nwelcome to {chat}')

# True Or False 
IMDB = is_enabled(environ.get('IMDB', "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
PM_IMDB = is_enabled(environ.get('PM_IMDB', "True"), True)
G_FILTER = is_enabled(environ.get("G_FILTER", "True"), True)
PMFILTER = is_enabled(environ.get('PMFILTER', "True"), True)
BUTTON_LOCK = is_enabled(environ.get("BUTTON_LOCK", "True"), True)
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))
SINGLE_BUTTON = is_enabled(environ.get('SINGLE_BUTTON', "True"), True)
P_TTI_SHOW_OFF = is_enabled(environ.get('P_TTI_SHOW_OFF', "True"), True)
PUBLIC_FILE_STORE = is_enabled(environ.get('PUBLIC_FILE_STORE', "True"), True)
PROTECT_CONTENT = is_enabled(environ.get('PROTECT_CONTENT', "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MELCOW_NEW_USERS = is_enabled(environ.get('MELCOW_NEW_USERS', "True"), True)
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)

# Bg Remove 
RemoveBG_API = environ.get("RemoveBG_API", '')

# url shortner
SHORT_URL = environ.get("SHORT_URL")
SHORT_API = environ.get("SHORT_API")

#Rrq Fsub
FSUB_MODE = "REQ"
REQ_CHANNEL = environ.get("REQ_CHANNEL", "")
JOIN_REQS_DB = environ.get("JOIN_REQS_DB", DATABASE_URI)
REQ_CHANNEL = int(REQ_CHANNEL) if REQ_CHANNEL and id_pattern.search(REQ_CHANNEL) else AUTH_CHANNEL

# Rename & Stream Feature True or False 
#Rename Mode - True or False 🤔
RENAME_MODE = bool(environ.get('RENAME_MODE', True)) # Set True or False

# Stream Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
STREAM_MODE = bool(environ.get('STREAM_MODE', True)) # Set True or False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
MULTI_CLIENT = False
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
URL = environ.get("URL", "https://aesthetic-ally-theblackxyz-84907c5f.koyeb.app/") # Fill env at deoplyment time Stream Mode Is True else avoide

# Others
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', '')
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", None)
IMDB_DELET_TIME = int(environ.get('IMDB_DELET_TIME', "300"))
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", script.IMDB_TEMPLATE)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", script.CUSTOM_FILE_CAPTION)

# Log Str 
LOG_STR = "Current Cusomized Configurations are:-\n"
#LOG_STR += ("RENAME_MODE are enabled, Bot Renaming will be show rename feature for you. \n if RENAME_MODE else "RENAME_MODE are disabled.\n")
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_RIST_BTNS} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"











