from pyrogram import filters
from pyrogram.types import Message

from AnonXMusic import app
from AnonXMusic.misc import SUDOERS
from AnonXMusic.utils.database import autoend_off, autoend_on


@app.on_message(filters.command("autoend","انهاء تلقائي") & SUDOERS)
async def auto_end_stream(_, message: Message):
    usage = "<b>مثال :</b>\n\n/انهاء تلقائي [enable | disable]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip().lower()
    if state == "enable":
        await autoend_on()
        await message.reply_text(
            "تم تفعيل وضع مغادرة الدردشة الصوتية تلقائيا ً.\n\nالحساب المساعد سيغادر الدردشة الصوتية تلقائياً بعد بضع دقائق ان لم يكن احد يستمع."
        )
    elif state == "disable":
        await autoend_off()
        await message.reply_text("» تم الغاء تفعيل وضع المغادرة تلقائياً.")
    else:
        await message.reply_text(usage)
