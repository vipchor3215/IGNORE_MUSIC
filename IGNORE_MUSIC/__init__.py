from IGNORE_MUSIC.core.bot import ISTKHAR
from IGNORE_MUSIC.core.dir import dirr
from IGNORE_MUSIC.core.git import git
from IGNORE_MUSIC.core.userbot import Userbot
from IGNORE_MUSIC.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = ISTKHAR()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
