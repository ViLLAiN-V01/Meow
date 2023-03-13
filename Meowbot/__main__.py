import glob
import sys
from pathlib import Path

import telethon.utils
from telethon import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest

from Meowbot import LOGS, bot, tbot
from Meowbot.config import Config
from Meowbot.utils import load_module
from Meowbot.version import __mew__ as mewver

hl = Config.HANDLER
MEOW_PIC = Config.ALIVE_PIC or "https://telegra.ph/file/9c7697cc000ea739d1986.jpg"


# let's get the bot ready
async def mew_bot(bot_token):
    try:
        await bot.start(bot_token)
        bot.me = await bot.get_me()
        bot.uid = telethon.utils.get_peer_id(bot.me)
    except Exception as e:
        LOGS.error(f"MEOWBOT_SESSION - {str(e)}")
        sys.exit()


# Meowbot starter...
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    try:
        if Config.BOT_USERNAME is not None:
            LOGS.info("Checking Telegram Bot Username...")
            bot.tgbot = TelegramClient(
                "BOT_TOKEN", api_id=Config.APP_ID, api_hash=Config.API_HASH
            ).start(bot_token=Config.BOT_TOKEN)
            LOGS.info("Checking Completed. Proceeding to next step...")
            LOGS.info("🔰 Starting MeowBot 🔰")
            bot.loop.run_until_complete(mew_bot(Config.BOT_USERNAME))
            LOGS.info("🔥 MeowBot Startup Completed 🔥")
        else:
            bot.start()
    except Exception as e:
        LOGS.error(f"BOT_TOKEN - {str(e)}")
        sys.exit()

# imports plugins...
path = "Meowbot/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))

# Extra Modules...
# extra_repo = Config.EXTRA_REPO or "https://github.com/TeamMew/Extra"
# if Config.EXTRA == "True":
#     try:
#         os.system(f"git clone {extra_repo}")
#     except BaseException:
#         pass
#     LOGS.info("Installing Extra Plugins")
#     path = "Meowbot/plugins/*.py"
#     files = glob.glob(path)
#     for name in files:
#         with open(name) as ex:
#             path2 = Path(ex.name)
#             shortname = path2.stem
#             load_module(shortname.replace(".py", ""))


# let the party begin...
LOGS.info("Starting Bot Mode !")
tbot.start()
LOGS.info("⚡ Your MeowBot Is Now Working ⚡")
LOGS.info(
    "Head to @Its_MeowBot for Updates. Also join chat group to get help regarding to MeowBot."
)


# that's life...
async def mew_is_on():
    try:
        if Config.LOGGER_ID != 0:
            await bot.send_file(
                Config.LOGGER_ID,
                MEOW_PIC,
                caption=f"#START \n\nDeployed ℳêøաɮøƚ Successfully\n\n**ℳêøաɮøƚ - {mewver}**\n\nType `{hl}ping` or `{hl}alive` to check! \n\nJoin [ℳêøաɮøƚ Channel](t.me/Its_MeowBot) for Updates & [ℳêøաɮøƚ Chat](t.me/MeowUbChat) for any query regarding ℳêøաɮøƚ",
            )
    except Exception as e:
        LOGS.info(str(e))

    # Join MeowBot Channel after deploying 🤐😅
    try:
        await bot(JoinChannelRequest("@Its_MeowBot"))
    except BaseException:
        pass


# Why not come here and chat??
#    try:
#        await bot(JoinChannelRequest("@MeowUbChat"))
#    except BaseException:
#        pass


bot.loop.create_task(mew_is_on())

if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    bot.run_until_disconnected()

# Meowbot
