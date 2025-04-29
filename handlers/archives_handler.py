from aiogram import Bot, Router, types
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import F
import os

router = Router()

ALLOWED_ARCHIVES = {'zip', 'rar', '7z', 'tar', 'gz', 'bz2'}

@router.message(
    F.document &
    F.document.file_name.func(
        lambda name: name.split('.')[-1].lower() in ALLOWED_ARCHIVES
    )
)
async def get_archive(message: Message, bot: Bot):
    print("get_archive")
    archive = message.document
