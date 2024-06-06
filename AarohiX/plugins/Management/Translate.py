from pyrogram import filters
from pyrogram.types import *
from AarohiX import app
from gpytranslate import Translator

#.......

trans = Translator()

#......

@app.on_message(filters.command("ترجمه"))
async def translate(_, message) -> None:
    reply_msg = message.reply_to_message
    if not reply_msg:
        await message.reply_text("◍ قم بعمل ريبلي للترجمه علي الرساله\n\n √")
        return
    if reply_msg.caption:
        to_translate = reply_msg.caption
    elif reply_msg.text:
        to_translate = reply_msg.text
    try:
        args = message.text.split()[1].lower()
        if "//" in args:
            source = args.split("//")[0]
            dest = args.split("//")[1]
        else:
            source = await trans.detect(to_translate)
            dest = args
    except IndexError:
        source = await trans.detect(to_translate)
        dest = "ar"
    translation = await trans(to_translate, sourcelang=source, targetlang=dest)
    reply = (
        f"◍ تم بنجاح ترجمه اللغه\n"
        f"الترجمه :{translation.text}"
    )
    await message.reply_text(reply)
