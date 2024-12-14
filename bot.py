import asyncio
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from Fsm_bones import fsm_stating
import bot_test


async def main():
    load_dotenv()
    bot = Bot(token=os.getenv("TG_KEY"))
    dp = Dispatcher()

    dp.include_router(fsm_stating.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

