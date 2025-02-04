import os

API_ID = API_ID =  27862677

API_HASH = os.environ.get("API_HASH", "e343ce2c81b2b6c2c0d6bee58284e3bd")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7594440755:AAHtdnGt9YWGfp4RKynABmAdhoKEGI1ViH8")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 7521176146))

LOG = -1002434329665,

# UPDATE_GRP = -1002140332321, # bot sat group

# auth_chats = [7521176146]

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "7521176146").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


