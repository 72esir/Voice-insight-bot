import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

from handlers import start_handler

logging.basicConfig(level=logging.INFO)

API_TOKEN="7637384511:AAF3hQYWV0g1cOfHRwDEixHr-K-2BI__tgw"

async def main():
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher()

    dp.include_router(start_handler.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
