from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot

from . import *

# -------------------------------------------------------------------------------

mew_pic = Config.ALIVE_PIC or "https://telegra.ph/file/3c2932815330a143fa1a8.png"
alive_c = f"__**πΊπΊΚΙΦΥ‘ Ι¨s ΦΥΌΚΙ¨ΥΌΙπΊπΊ**__\n\n"
alive_c += f"**ββββββββββββββββββββ**\n\n"
alive_c += f"β βͺΓΟΞ·ΡΡβ«β£  β± γ {mew_mention} γ\n\n"
alive_c += f"ββββββββββββββββββββ\n"
alive_c += f"β£β§Όβ’ ΡΞ΅βΞ΅ΡΠ½ΟΞ·  β±  `{tel_ver}` \n"
alive_c += f"β£β§Όβ’ ΠΌΞ΅ΟΟ        β±  __**{mew_ver}**__\n"
alive_c += f"β£β§Όβ’ sΟβΟ           β± `{is_sudo}`\n"
alive_c += f"β£β§Όβ’ cΠ½Ξ±Ξ·Ξ·Ξ΅β     β±  {mew_channel}\n"
alive_c += f"β£β§Όβ’ βΞΉcΞ΅Ξ·sΞ΅     β± [Meow](GitHub.com/TeamMew)\n"
alive_c += f"β£β§Όβ’ ΟΟΡΞΉΠΌΞ΅      β± `{uptime}`\n"
alive_c += f"ββββββββββββββββββββ\n"
# -------------------------------------------------------------------------------


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
**β¨ ΚΙΦΥ‘ ΞΉΡ ΟΠΈβΞΉΠΈΡ β¨**
{Config.ALIVE_MSG}
**πΉ Meow ππππππ πΉ**
**ΡΡβΡΡΠ½ΟΠΈ:**  `{tel_ver}`
**β³ΓͺΓΈΥ‘    :**  **{mew_ver}**
**ΟΟΡΞΉΠΌΡ    :**  `{uptime}`
**Ξ±Π²ΟΡΡ     :**  **{abuse_m}**
**ΡΟβΟ        :**  **{is_sudo}**
"""
botname = Config.BOT_USERNAME


@bot.on(mew_cmd(pattern="meow$"))
@bot.on(sudo_cmd(pattern="meow$", allow_sudo=True))
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
).add_command("Meow", None, "Shows Inline Alive Menu with more details.").add_warning(
    "β Harmless Module"
).add()
