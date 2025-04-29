from aiogram import Bot, Router
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram import F

from processing_responses.processing_archives import processing_archive
from processing_responses.processing_transcribation import processing_transcribation

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
    if archive:
        arc_name = archive.file_name
        arc_id = archive.file_id
        arc_type = archive.mime_type
        print(arc_type)
    if arc_name and arc_type:
        transcribation = await processing_archive(bot, arc_name, arc_id, arc_type)
        print(transcribation)
        analize = await processing_transcribation(transcribation)
        print("resp = " + analize)

    await message.answer(
        f"Транскрибация аудио: \n{transcribation}\n\nАнализ: \n{analize}",
        parse_mode=ParseMode.MARKDOWN
    )
