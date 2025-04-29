from aiogram import Router, F, Bot
from aiogram.types import Message, ContentType
from aiogram.enums import ParseMode

from processing_responses.processing_audio import processing_long_mp3
from processing_responses.processing_transcribation import processing_transcribation

router = Router()

@router.message(F.content_type == ContentType.AUDIO)
async def send_answ_on_mp3(message: Message, bot: Bot):
    print("send_answ_on_mp3")
    mp3 = message.audio
    if message.audio and mp3:
        file_id = mp3.file_id
        file_name = mp3.file_name

        if mp3.mime_type == "audio/mpeg" and file_name:
            if mp3.duration < 30:
                transcribation = await processing_long_mp3(bot, file_name, file_id)
                print(transcribation)
                resp: str = await processing_transcribation(transcribation)
                print(resp)
            else:
                transcribation = await processing_long_mp3(bot, file_name, file_id)
                print(transcribation)
                resp: str = await processing_transcribation(transcribation)
                print("resp = " + resp)

        await message.answer(
            f"Транскрибация аудио: \n{transcribation}\n\nАнализ: \n{resp}",
            parse_mode=ParseMode.MARKDOWN
        )
