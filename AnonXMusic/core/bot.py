from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus, ParseMode

import config

from ..logging import LOGGER


class Anony(Client):
    def __init__(self):
        LOGGER(__name__).info(f"جر تشغيل البوت...")
        super().__init__(
            name="AnonXMusic",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            parse_mode=ParseMode.HTML,
            max_concurrent_transmissions=7,
        )

    async def start(self):
        await super().start()
        self.id = self.me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.username = self.me.username
        self.mention = self.me.mention

        try:
            await self.send_message(
                chat_id=config.LOGGER_ID,
                text=f"<u><b>» {self.mention} تم تشغيل البوت :</b><u>\n\nالايدي : <code>{self.id}</code>\nالاسم : {self.name}\nالمعرف : @{self.username}",
            )
        except (errors.ChannelInvalid, errors.PeerIdInvalid):
            LOGGER(__name__).error(
                "فشل البوت في الوصول لـ اللوج في الجروب/القناة. تأكد انك اضفت بوتك لـ اللوج في الجروب/القناة."
            )
            exit()
        except Exception as ex:
            LOGGER(__name__).error(
                f"فشل البوت في الوصول لـ اللوج في الجروب/القناة.\n  السبب : {type(ex).name}."
            )
            exit()

        a = await self.get_chat_member(config.LOGGER_ID, self.id)
        if a.status != ChatMemberStatus.ADMINISTRATOR:
            LOGGER(__name__).error(
                "من فضلك ارفع البوت مشرف في جروب اللوج /القناة."
            )
            exit()
        LOGGER(__name__).info(f"بوت القران اشتغل كـ{self.name}")

    async def stop(self):
        await super().stop()
