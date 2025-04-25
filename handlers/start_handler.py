from aiogram import Router, F, Bot
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types.document import Document

router = Router()

AUDIO_MIME_TYPES = {
    'audio/mpeg',  # mp39
    'audio/ogg',
    'audio/wav',
    'application/ogg'
}

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "Привет! Выбери файл который ты хотел бы расшифровать.",
    )
