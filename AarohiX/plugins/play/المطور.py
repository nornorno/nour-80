from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from strings.filters import command
from AarohiX import app
import config


@app.on_message(
    command(["مطور السورس", "مبرمج السورس", "المطور"])
)
async def maker(client: Client, message: Message):
    await message.reply_photo(
        photo="https://telegra.ph/file/3955f6d7c023440c11156.jpg",
        caption="• Dev Bot ↦ المطور \n ━━━━━━━━━━━━ \n • Dev ↦  Cr SoUrce . \n • Bio ↦ 𝗘𝗩𝗘 #𝗥𝗬𝗧𝗛𝗜𝗡𝗚 𝗧𝗛𝗜𝗦 #𝗔𝗖𝗖𝗢𝗨𝗡𝗧 { noordot.t.me } { vzs_a.t.me }{ sahnks.t.me }{ vza_o.t.me } { sw_no.t.me }{ vzo_a.t.me }",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "NooR Cr", url=f"tg://openmessage?user_id={config.OWNER_ID}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "Updates", url=config.SUPPORT_CHAT
                    ),
                ],
            ]
        ),
    )
