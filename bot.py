import asyncio
import logging
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
import os

from handlers import start_handler, get_ogg_handler, no_file_message_handler, get_mp3_handler, get_wav_handler

logging.basicConfig(level=logging.INFO)

load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")

async def main():
    if API_TOKEN:
        bot = Bot(API_TOKEN)
    dp = Dispatcher()

    dp.include_router(start_handler.router)
    dp.include_router(get_ogg_handler.router)
    dp.include_router(get_mp3_handler.router)
    dp.include_router(get_wav_handler.router)
    dp.include_router(no_file_message_handler.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
