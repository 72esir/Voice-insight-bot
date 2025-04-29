from aiogram import Bot
import os
from aiogram.types.voice import Voice

from processing_responses.converting_audio import convert_to_ogg

from my_requests.request_to_speech_kit import send_req_to_kit
from my_requests.request_for_get_long_ogg_tr import get_long_ogg_tr
from my_requests.request_to_post_file_on_bucket import post_file

DOWNLOADS_DIR = "C:\\Users\\Алексей\\source\\VI_bot\\downloads"

async def download_audio(bot: Bot, file_name: str, file_id: str):
    file = await bot.get_file(file_id)
    file_path = file.file_path

    full_path = os.path.join(DOWNLOADS_DIR, file_name)

    if file_path:
        print()
        await bot.download_file(file_path, full_path)

async def processing_short_ogg(bot: Bot, file_name: str, file_id: str) -> str:
    await download_audio(bot, file_name, file_id)
    transcribation = send_req_to_kit(file_name)

    return transcribation

async def processing_long_ogg(bot: Bot, file_name: str, file_id: str) -> str:
    print(file_name)
    await download_audio(bot, file_name, file_id)
    post_file(file_name)
    transcribation = get_long_ogg_tr(file_name)

    return transcribation

async def processing_long_mp3(bot: Bot, file_name: str, file_id: str):
    print(file_name)
    await download_audio(bot, file_name, file_id)

    file_name = convert_to_ogg(file_name, "audio/mpeg")
    print("file_name from proc mp3: " + file_name)

    post_file(file_name)
    transcribation = get_long_ogg_tr(file_name)

    return transcribation

async def processing_wav(bot: Bot, file_name: str, file_id: str):
    print(file_name)
    await download_audio(bot, file_name, file_id)

    file_name = convert_to_ogg(file_name, "audio/vnd.wave")

    post_file(file_name)
    transcribation = get_long_ogg_tr(file_name)

    return transcribation
