from bot import Bot
import pyrogram.utils
import asyncio

pyrogram.utils.MIN_CHANNEL_ID = -1009147483647

bot = Bot()

async def main():
    await bot.start()  # Start bot without use_qr
    print("Bot is running...")
    await bot.idle()  # Keep the bot running

asyncio.run(main())
