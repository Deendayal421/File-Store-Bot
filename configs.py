import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "16681004"))
  API_HASH = os.environ.get("API_HASH", "161b61f5a06dd299a3d88a3384b9f104")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "6431557817:AAG4duOW33YXU9U7lF56cGbYdOj9xFRp03w")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "Deendayal_Storage_bot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002137665979"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "ziplinker.net")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "4859713bcbf09f6fca6de13b5f88bbf29ea5ea6c")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "6646028262"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://sonamdhakad432:ysfYedQ39BKpq0Q1@cluster0.aap18zd.mongodb.net/?retryWrites=true&w=majority")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001786865459")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002021571773"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 
