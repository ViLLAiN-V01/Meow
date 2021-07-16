from telethon import events
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User
from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot

from . import *

#-------------------------------------------------------------------------------

mew_pic = Config.ALIVE_PIC or "https://telegra.ph/file/9c7697cc000ea739d1986.jpg"
alive_c = f"__**🔥🔥ʍɛօաɮօȶ ɨs օռʟɨռɛ🔥🔥**__\n\n"
alive_c += f"__↼ Øwñêr ⇀__ : 『 {mew_mention} 』\n\n"
alive_c += f"•♦• Telethon     :  `{tel_ver}` \n"
alive_c += f"•♦• ℳêøաɮøƚ       :  __**{mew_ver}**__\n"
alive_c += f"•♦• Sudo            :  `{is_sudo}`\n"
alive_c += f"•♦• Channel      :  {mew_channel}\n"

#-------------------------------------------------------------------------------

@bot.on(mew_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def up(Meow):
    if Meow.fwd_from:
        return
    await Meow.get_chat()
    await Meow.delete()
    await bot.send_file(Meow.chat_id, mew_pic, caption=alive_c)
    await Meow.delete()

msg = f"""
**⚡ ʍɛօաɮօȶιѕ σиℓιиє ⚡**
{Config.ALIVE_MSG}
**🏅 𝙱𝚘𝚝 𝚂𝚝𝚊𝚝𝚞𝚜 🏅**
**Telethon :**  `{tel_ver}`
**ℳêøաɮøƚ  :**  **{mew_ver}**
**Uptime   :**  `{uptime}`
**Abuse    :**  **{abuse_m}**
**Sudo      :**  **{is_sudo}**
"""
botname = Config.BOT_USERNAME

@bot.on(mew_cmd(pattern="Meow$"))
@bot.on(sudo_cmd(pattern="Meow$", allow_sudo=True))
async def mew_a(event):
    try:
        Meow = await bot.inline_query(botname, "alive")
        await Meow[0].click(event.chat_id)
        if event.sender_id == ForGo10God:
            await event.delete()
    except (noin, dedbot):
        await eor(event, msg)


CmdHelp("alive").add_command(
  "alive", None, "Shows the Default Alive Message"
).add_command(
  "Meow", None, "Shows Inline Alive Menu with more details."
).add_warning(
  "✅ Harmless Module"
).add()
