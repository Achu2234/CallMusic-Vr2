import os

from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat

from helpers.filters import command, other_filters, other_filters2


## ~ Simple Config ~ ##
FRIEND_BOT = "Achubiju6c"
USER_ACCNAME = os.getenv("USER_ACCNAME", "Achubiju6c")



@Client.on_message(command(["start", "start@YeageristMusic_bo"]))
async def start(_, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name} ðï¸!</b>

I'm The Yeagerist Music Streamer Bot. Friend of **@{FRIEND_BOT}** ðï¸.

I can play Music In Telegram Groups Via Voice Chat! ðï¸.

My Dev : @Amalbiju154

á´á´á´¡á´Êá´á´ ÊÊ Yá´á´É¢á´ÊÉªsá´ Bá´á´s #ðð¸ð½ð¼ðð®ð½ðð¸ð»ð´

Made with â¤ï¸ <b>@Animemusicarchive6</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ð¤¨ï¸ How To Use Me ð¤¨ï¸", url="https://telegra.ph/How-To-Use-Yeagerist-Music-Streamer-Bot-04-05"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "ð°ï¸ My Update Channel ð°ï¸", url="https://t.me/Animemusicarchive6"
                    ),
                    InlineKeyboardButton(
                        "âï¸ Support Group âï¸", url="https://t.me/Yeageristbots"
                    )
                ]
            ]
        )
    )
    
    
@Client.on_message(command(["help", "help@YeageristMusic_bot"]))
async def help(_, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name} ðï¸!</b>

Hi Do you need Help! ð¤ï¸ yea yea I know it! ðï¸

How To Use Me? ð§ï¸

If yo want vidio : https://t.me/Animemusicarchive6/3247

<b> 1. Add Me and @{USER_ACCNAME} To Your Group!

 2. Give Admin To Me and @{USER_ACCNAME} ! </b>
 
 Enjoy! ðï¸

Made with â¤ï¸ <b>@Animemusicarchive6</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ð°ï¸ My Update Channel ð°ï¸", url="https://t.me/Animemusicarchive6"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "âï¸ Support Group âï¸", url="https://t.me/Yeageristbots"
                    )
                ]
            ]
        )
    )

    
@Client.on_message(command(["cmdlist", "cmdlist@YeageristMusic_bot"]))
async def cmdlist(_, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name} ðï¸!</b>

Here is the list of available commands! ðï¸

<code>/play</code> - Reply to supported url or "/play supported url"
<code>/skip</code> - Skip currenly playing song!
<code>/pause</code> - Pause currently playing song!
<code>/resume</code> - Resume currently pushed song!
<code>/mute</code> - Mutes Streamer!
<code>/unmute</code> - Unmutes streamer!
<code>/vc</code> - Give voice chat link of your group! (Only For Public Groups)
<code>/yts (song name)</code> - Download song by it's name!

 Enjoy! ðï¸""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ðï¸ Supported Sites ðï¸", url="https://ytdl-org.github.io/youtube-dl/supportedsites.html"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "âï¸ Support Group âï¸", url="https://t.me/Yeageristbots"
                    )
                ],
                [
                    InlineKeyboardButton(
                    "ð°ï¸ My Update Channel ð°ï¸", url="https://t.me/Animemusicarchive6"
                    )
                ]
            ]
        )
    )
   
    
@Client.on_message(command("credits") & other_filters2)
async def credits2(_, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name} ðï¸!</b>

__Note!__ â ï¸: This Project Is <b>Not Fully Owned By Me</b> !

Credits To,

<b><a href="https://github.com/CallsMusic">CallsMusic</a></b> - For Callsmusic (Main Code â¤ï¸) !
<b><a href="https://github.com/nikhileashy">N A C</a></b> - For <code>/vc</code> Command

Made with â¤ï¸ by **@NexaBotsUpdates**

Respect To Code Owners! Not To Me!""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ð°ï¸ My Update Channel ð°ï¸", url="https://t.me/Animemusicarchive6"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "âï¸ Support Group âï¸", url="https://t.me/Yeageristbots"
                    )
                ]
            ]
        )
    )   


@Client.on_message(command(["vc", "vc@YeageristMusic_bot"]) & other_filters)
async def vc(_, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name} ðï¸!</b>


             ðï¸  **Voice Chat Link** ðï¸
____________________------------______________________

ðï¸ https://t.me/{message.chat.username}?voicechat   ðï¸
____________________------------______________________

Enjoy!ðï¸â¤ï¸""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ð°ï¸ My Update Channel ð°ï¸", url="https://t.me/Animemusicarchive6"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "âï¸ Support Group âï¸", url="https://t.me/Yeageristbots"
                    )
                ]
            ]
        )
    )

    
@Client.on_message(command(["search", "search@YeageristMusic_bot"]))
async def search(_, message: Message):
    await message.reply_text(
        "ðð»ââï¸ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "â Yeah", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "Nope â", callback_data="close"
                    )
                ]
            ]
        )
    )
