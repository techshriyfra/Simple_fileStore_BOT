from bot import Bot
import asyncio

async def main():
    bot = Bot()
    await bot.start()
    # Keep the bot running until manually stopped
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
