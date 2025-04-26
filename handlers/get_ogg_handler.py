from aiogram import Router, F, Bot
from aiogram.types import Message
from aiogram.enums import ParseMode

from processing_responses.processing_audio import processing_ogg
from processing_responses.processing_transcribation import processing_transcribation

router = Router()

@router.message(F.voice)
async def get_voice_answ(message: Message, bot: Bot):
    voice = message.voice
    if voice:
        transcribation = await processing_ogg(voice, bot)
        print(transcribation)
        resp: str = await processing_transcribation(transcribation)
        print(resp)

    await message.answer(
        f"Транскрибация аудио: \n{transcribation}\n\nАнализ: \n{resp}",
        parse_mode=ParseMode.MARKDOWN
    )
