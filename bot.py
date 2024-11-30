import asyncio
from aiogram import Bot, Dispatcher
from Fsm_bones import fsm_stating


async def main():
    bot = Bot(token="")
    dp = Dispatcher()

    dp.include_router(fsm_stating.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

