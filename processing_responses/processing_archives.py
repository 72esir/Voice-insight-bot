from aiogram import Bot
import zipfile, tarfile, py7zr

from my_requests.request_for_get_long_ogg_tr import get_long_ogg_tr
from my_requests.request_to_post_file_on_bucket import post_file
from processing_responses.converting_audio import convert_to_ogg

async def processing_archive(bot: Bot, arc_name: str, file_id: str, arc_type: str) -> str:
    processed_arc_type = await get_arc_type(arc_type)
    if processed_arc_type:
        file_name = await extract_arc(bot, arc_name, file_id, processed_arc_type)

    if file_name == ">1":
        return ">1"
    elif file_name == "=0":
        return "=0"

    type = file_name.split(".")[1]
    if type == "ogg":
        post_file(file_name)
        transcribation = get_long_ogg_tr(file_name)
    elif type == "mp3":
        file_name = convert_to_ogg(file_name, "audio/mpeg")
        post_file(file_name)
        transcribation = get_long_ogg_tr(file_name)
    elif type == "wav" or "WAV":
        file_name = convert_to_ogg(file_name, "audio/vnd.wave")
        post_file(file_name)
        transcribation = get_long_ogg_tr(file_name)
    else:
        pass

    return transcribation

async def extract_arc(bot: Bot, arc_name: str, file_id: str, arc_type: str) -> str:
    file = await bot.get_file(file_id)
    file_path = file.file_path
    dst = f"downloads/{arc_name}"
    if file_path:
        await bot.download_file(file_path, dst)
        print("download_arc")

    if arc_type == "zip":
        with zipfile.ZipFile(f'downloads/{arc_name}', 'r') as zip_ref:
            files_list = zip_ref.namelist()
            if len(files_list) > 1:
                #вывести сообщение о том что много файлов в апхиве
                return ">1"

            elif len(files_list) == 0:
                #вывести сообщение что нет файлов в архиве
                return "=0"

            else:
                file_name = files_list[0]

            zip_ref.extractall('downloads/')
            print("extract")
    elif arc_type == "tar":
        with tarfile.open(f'downloads/{arc_name}', 'r:*') as tar:
            files_list = tar.getnames()
            if len(files_list) > 1:
                #вывести сообщение о том что много файлов в апхиве
                return ">1"

            elif len(files_list) == 0:
                #вывести сообщение что нет файлов в архиве
                return "=0"

            else:
                file_name = files_list[0]

            tar.extractall('downloads/')
    elif arc_type == "7z":
        with py7zr.SevenZipFile(f'downloads/{arc_name}', mode='r') as z:
            files_list = z.getnames()
            if len(files_list) > 1:
                #вывести сообщение о том что много файлов в апхиве
                return ">1"

            elif len(files_list) == 0:
                #вывести сообщение что нет файлов в архиве
                return "=0"

            else:
                file_name = files_list[0]

            z.extractall('downloads/')

    return file_name

async def get_arc_type(type: str) -> str | None:
    if type == "application/x-tar":
        return "tar"
    elif type == "application/zip":
        return "zip"
    elif type == "application/x-7z-compressed":
        return "7z"
    else:
        return None
