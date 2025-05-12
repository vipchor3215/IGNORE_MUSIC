import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from IGNORE_MUSIC import LOGGER, app, userbot
from IGNORE_MUSIC.core.call import ISTKHAR
from IGNORE_MUSIC.misc import sudo
from IGNORE_MUSIC.plugins import ALL_MODULES
from IGNORE_MUSIC.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("IGNORE_MUSIC.plugins" + all_module)
    LOGGER("IGNORE_MUSIC.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await ISTKHAR.start()
    try:
        await ISTKHAR.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("IGNORE_MUSIC").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await ISTKHAR.decorators()
    LOGGER("IGNORE_MUSIC").info("IGNORE_MUSICBot Started Successfully \n\n Yaha App ko nahi aana hai aapni hf jo bhej sakte hai @Cinderella_Updates ")
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("IGNORE_MUSIC").info("Stopping ISTKHAR Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
