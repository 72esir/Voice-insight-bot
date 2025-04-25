from aiogram import Router, F, Bot
from aiogram.types import Message, Document

router = Router()

@router.message()
async def not_handled(message: Message, bot: Bot):
    doc: Document | None = message.document
    if doc is None:
        await message.answer("Вы не прислали документ.")
        return
    await message.answer(
        f"Вы выбрали неподходящий документ ({doc.mime_type})! Выберите audio (.ogg/.mp3/.wav)"
    )
