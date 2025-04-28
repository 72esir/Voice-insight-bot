from aiogram import Router, F, Bot
from aiogram.types import Message
from aiogram.enums import ParseMode

from processing_responses.processing_audio import processing_short_ogg, processing_long_ogg
from processing_responses.processing_transcribation import processing_transcribation

router = Router()

@router.message(F.voice)
async def send_answ_on_voice(message: Message, bot: Bot):
    voice = message.voice
    if voice:
        file_id = voice.file_id
        file_name = f"voice_{file_id}.ogg"

        if voice.duration < 30:
            transcribation = await processing_short_ogg(bot, file_name, file_id)
            print(transcribation)
            resp: str = await processing_transcribation(transcribation)
            print(resp)
        else:
            transcribation = await processing_long_ogg(bot, file_name, file_id)
            print(transcribation)
            resp: str = await processing_transcribation(transcribation)
            print(resp)

    await message.answer(
        f"Транскрибация аудио: \n{transcribation}\n\nАнализ: \n{resp}",
        parse_mode=ParseMode.MARKDOWN
    )
