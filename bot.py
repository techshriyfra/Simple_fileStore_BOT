from aiohttp import web
from plugins import web_server

import pyromod.listen
from pyrogram import Client
from pyrogram.enums import ParseMode
import sys
from datetime import datetime

from config import API_HASH, APP_ID, LOGGER, TG_BOT_TOKEN, TG_BOT_WORKERS, FORCE_SUB_CHANNEL, FORCE_SUB_CHANNEL2, CHANNEL_ID, PORT


class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={
                "root": "plugins"
            },
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.uptime = datetime.now()

        # Note => This is old method and it is not compatible with the latest telegram version (( YT or TG : @LazyDeveloperr ))
        # So replacing the force sub method with req to join feature 🚀 (( YT or TG : @LazyDeveloperr ))
        #  
        # if FORCE_SUB_CHANNEL:
        #     try:
        #         link = (await self.get_chat(FORCE_SUB_CHANNEL)).invite_link
        #         if not link:
        #             await self.export_chat_invite_link(FORCE_SUB_CHANNEL)
        #             link = (await self.get_chat(FORCE_SUB_CHANNEL)).invite_link
        #         self.invitelink = link
        #     except Exception as a:
        #         self.LOGGER.warning(a)
        #         self.LOGGER.warning("Bot can't Export Invite link from Force Sub Channel!")
        #         self.LOGGER.warning(f"Please Double check the FORCE_SUB_CHANNEL value and Make sure Bot is Admin in channel with Invite Users via Link Permission, Current Force Sub Channel Value: {FORCE_SUB_CHANNEL}")
        #         self.LOGGER.info("\nBot Stopped. https://t.me/LazyDeveloper for support")
        #         sys.exit()
        # if FORCE_SUB_CHANNEL2:
        #     try:
        #         link = (await self.get_chat(FORCE_SUB_CHANNEL2)).invite_link
        #         if not link:
        #             await self.export_chat_invite_link(FORCE_SUB_CHANNEL2)
        #             link = (await self.get_chat(FORCE_SUB_CHANNEL2)).invite_link
        #         self.invitelink2 = link
        #     except Exception as a:
        #         self.LOGGER.warning(a)
        #         self.LOGGER.warning("Bot can't Export Invite link from Force Sub Channel!")
        #         self.LOGGER.warning(f"Please Double check the FORCE_SUB_CHANNEL2 value and Make sure Bot is Admin in channel with Invite Users via Link Permission, Current Force Sub Channel Value: {FORCE_SUB_CHANNEL2}")
        #         self.LOGGER.info("\nBot Stopped. https://t.me/LazyDeveloper for support")
        #         sys.exit()
        
        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id=db_channel.id, text="Test Message")
            await test.delete()
        except Exception as e:
            self.LOGGER.warning(e)
            self.LOGGER.warning(f"Make Sure bot is Admin in DB Channel, and Double check the CHANNEL_ID Value, Current Value {CHANNEL_ID}")
            self.LOGGER.info("\nBot Stopped. Join channel https://t.me/LazyDeveloper for support")
            sys.exit()  # if bot is admin & you are getting admin issue again and again then u can also remove this line of code 

        self.set_parse_mode(ParseMode.HTML)
        self.LOGGER.info(f"Bot Running..!\n\n❤ with love  \n ıllıllı🚀🌟 L͙a͙z͙y͙D͙e͙v͙e͙l͙o͙p͙e͙r͙r͙ 🌟🚀ıllıllı")
        self.username = usr_bot_me.username
        # web-response
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER.info("Bot stopped.")
