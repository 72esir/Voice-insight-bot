from os import path
from pydub import AudioSegment
import sys

def convert_to_ogg(file_name: str, type) -> str:
    src = "downloads/" + file_name
    dst = "downloads/conv_" + file_name.split(".")[0] + ".ogg"

    if type == "audio/mpeg":
        sound = AudioSegment.from_mp3(src)
        sound.export(dst, format="ogg", codec='libopus')

    if type == "audio/vnd.wave":
        sound = AudioSegment.from_wav(src)
        sound.export(dst, format="ogg",  codec="libopus")

    print("dst = " + dst.split("/")[1])
    return dst.split("/")[1]
