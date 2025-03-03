from bot import Bot
import pyrogram.utils

pyrogram.utils.MIN_CHANNEL_ID = -1002351859964

bot = Bot()

async def main():
    await bot.start()  # Start bot without use_qr
    print("Bot is running...")

    await idle()  # ✅ Correct method to keep bot running

    await bot.stop()  # Stop the bot when exiting

asyncio.run(main())
