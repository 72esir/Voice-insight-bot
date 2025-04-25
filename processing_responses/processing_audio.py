from aiogram import Bot
import os
from aiogram.types.voice import Voice

from handlers.requests_handler import send_req_to_kit

DOWNLOADS_DIR = "C:\\Users\\Алексей\\source\\VI_bot\\downloads"

async def processing_ogg(voice: Voice, bot: Bot) -> str:
    if voice is not None:
        file_id = voice.file_id
        file_name = f"voice_{file_id}"

        file = await bot.get_file(file_id)
        file_path = file.file_path

        full_path = os.path.join(DOWNLOADS_DIR, file_name)

        if file_path:
            print()
            await bot.download_file(file_path, full_path)

        transcribation = send_req_to_kit(file_name)
        return transcribation
