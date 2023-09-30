# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open("{}/SaitamaRobot/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 26019444  # integer value, dont use ""
    API_HASH = "a308fac723905cdbd836414b18f3b3d6"
    TOKEN = "6227746263:AAFu7wTinTlxklY0gaDG1EYrNFaA9tfsges"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 6046532356  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "MonsterKatakuri"
    SUPPORT_CHAT = "RealmBotSupport"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        -1001809696061
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1001961814954
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "postgres://etdiqawv:S-_PRj7jd90sCBfbei3L-WyFEQfkiMwB@castor.db.elephantsql.com/etdiqawv"  # needed for any database modules # its "URI" and not "URL" as herok and similar ones only accept it as such
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = "G7M~Cyah5NsAqpETbOT6KtnHwciRLgHUIAWBBA4VE5nVLyw_wt9ZP46gpuN09vv2"  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list("elevated_users.json", "5860097723 5925926828")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list("elevated_users.json", "supports")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = "CAACAgIAAxkBAAEIwVtkStKzlE3ximDkVx_7pTKnB8JR5gACIx0AAvBceEhkJz2QJ7CZ_S8E"  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "TCYFLC8EVUBR8QLM"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "KU49805AW29R"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "awoo"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = "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"  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
