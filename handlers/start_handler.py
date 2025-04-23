from aiogram import Router, F, Bot
from aiogram.filters import Command
from aiogram.enums import ContentType
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.types.audio import Audio
from aiogram.types.document import Document
from aiogram.types.voice import Voice
import os

from request import send_req

router = Router()

AUDIO_MIME_TYPES = {
    'audio/mpeg',  # mp3
    'audio/ogg',
    'audio/wav',
    'application/ogg'
}

DOWNLOADS_DIR = "C:\\Users\\Алексей\\source\\VI_bot\\downloads"

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "Привет! Выбери файл который ты хотел бы расшифровать.",
    )

@router.message(F.audio)
async def get_audio_answ(message: Message, bot: Bot):
    audio: Audio | None = message.audio

    if audio is not None:
        file_name = audio.file_name
        file_id = audio.file_id

        # Скачиваем файл
        file = await bot.get_file(file_id)
        #path = DOWNLOADS_DIR + file_name
        file_path = file.file_path

        if file_name:
            full_path = os.path.join(DOWNLOADS_DIR, file_name)

        if file_path:
            await bot.download_file(file_path=file_path, destination=full_path)

        await message.answer(
            "Документ mp3 получен!"
        )

@router.message(F.voice)
async def get_voice_answ(message: Message, bot: Bot):
    voice: Voice | None = message.voice

    if voice is not None:
        file_id = voice.file_id
        file_name = f"voice_{file_id}"

        # Скачиваем файл
        file = await bot.get_file(file_id)
        file_path = file.file_path

        full_path = os.path.join(DOWNLOADS_DIR, file_name)

        if file_path:
            print()
            await bot.download_file(file_path, full_path)

        tr = send_req(file_name)

        await message.answer(
            tr
        )

@router.message()
async def not_handled(message: Message, bot: Bot):
    doc: Document | None = message.document
    if doc is None:
        await message.answer("Вы не прислали документ.")
        return
    await message.answer(
        #"Вы выбрали неподходящий документ! Выберите audio (.ogg/.mp3/.wav)"
        f"Type = {doc.mime_type}"
    )
