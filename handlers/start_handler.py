from aiogram import Router, F
from aiogram.filters import Command
from aiogram.enums import ContentType
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards.yes_no_buttons import get_yes_no_kb

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "Привет! Выбери файл который ты хотел бы расшифровать.",
    )

@router.message(F.content_type == ContentType.AUDIO)
async def get_audio_answ(message: Message):
    await message.answer(
        "Документ получен!"
    )

@router.message()
async def not_handled(message: Message):
    await message.answer(
        "Вы выбрали неподходящий документ! Выберите audio (.ogg/.mp3/.wav)"
    )
