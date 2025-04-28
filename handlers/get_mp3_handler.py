from aiogram import Router, F, Bot
from aiogram.types import Message, ContentType
from aiogram.enums import ParseMode

from processing_responses.processing_audio import processing_long_mp3
from processing_responses.processing_transcribation import processing_transcribation

router = Router()

@router.message(F.content_type.in_({ContentType.AUDIO, ContentType.DOCUMENT}))
async def send_answ_on_mp3(message: Message, bot: Bot):
    mp3 = message.audio
    if message.audio and mp3:
        file_id = mp3.file_id
        file_name = f"voice_{file_id}.ogg"

        if message.audio.mime_type == "audio/mpeg":
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
