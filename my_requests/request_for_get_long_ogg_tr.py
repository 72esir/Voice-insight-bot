import requests
import time
import json
import os

from dotenv import load_dotenv

def get_long_ogg_tr(file_name: str) -> str:
    load_dotenv()

    print("from tr")
    print(file_name)
    key = os.getenv("API_KEY")
    filelink = f"https://storage.yandexcloud.net/bucket-for-speech-kit/downloads/{file_name}"

    POST = 'https://transcribe.api.cloud.yandex.net/speech/stt/v2/longRunningRecognize'

    body = {
        "config": {
            "specification": {
                "languageCode": "ru-RU"
            }
        },
        "audio": {
            "uri": filelink
        }
    }

    header = {'Authorization': f'Api-Key {key}'}

    req = requests.post(POST, headers=header, json=body)
    data = req.json()
    print(data)

    if 'error' in data:
        print(f"Ошибка транскрипции: {data['error']['message']}")
        return ""

    operation_id = data['id']

    while True:
        time.sleep(1)
        GET = f"https://operation.api.cloud.yandex.net/operations/{operation_id}"
        req = requests.get(GET, headers=header)
        req = req.json()

        if req.get('done'):
            break
        print("Not ready")

    print("Response:")
    print(json.dumps(req, ensure_ascii=False, indent=2))

    if 'error' in req:
        print(f"Ошибка в операции: {req['error']['message']}")
        return ""

    text = ""
    print("Text chunks:")
    for chunk in req['response']['chunks']:
        text += chunk['alternatives'][0]['text'] + " "

    return text
