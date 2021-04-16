from telethon import Button, custom, events, functions
import telethon, os, sys

api_id = os.environ.get("API_KEY", None)
api_hash = os.environ.get("API_HASH", None)
bot_token = os.environ.get("TOKEN", None)


bot = TelegramClient("bot", api_id=api_id, api_hash=api_hash)
try:
 tbot = bot.start(bot_token=TOKEN)
except:
 print("Network Error")
 sys.exit(1)


async def check_if_subbed(channel_id, event, bot):
    try:
            result = await bot(
                functions.channels.GetParticipantRequest(
                    channel=channel_id, user_id=event.sender_id
                )
            )
            if result.participant:
                return True
    except telethon.errors.rpcerrorlist.UserNotParticipantError:
        return False

grp = "t.me/RedHubGiveaway"

@tbot.on(events.NewMessage(pattern=None))
async def hmm(event):
 rexy = await check_if_subbed('RedHubGiveaway', event, tbot)
 if rexy is False:
     await event.reply("**I am Sorry To Say That, To Access Me You Have To Be The Member Of Our Channel To Use This Bot..!**", buttons=[[custom.Button.url("Join Channel", grp)]])
