from aiogram import Router, F, Bot
from aiogram.types import Message
from aiogram.enums import ParseMode

from processing_responses.processing_audio import processing_wav
from processing_responses.processing_transcribation import processing_transcribation

router = Router()

@router.message(F.document & (F.document.file_name.endswith('.wav') | F.document.file_name.endswith('.WAV')))
async def send_answ_on_wav(message: Message, bot: Bot):
    print("send_answ_on_wav")
    wav = message.document
    if wav:
        file_id = wav.file_id
        file_name = wav.file_name

        if file_name and wav.mime_type == "audio/vnd.wave":
            transcribation = await processing_wav(bot, file_name, file_id)
            print(transcribation)
            resp: str = await processing_transcribation(transcribation)
            print("resp = " + resp)

    await message.answer(
        f"Транскрибация аудио: \n{transcribation}\n\nАнализ: \n{resp}",
        parse_mode=ParseMode.MARKDOWN
    )
