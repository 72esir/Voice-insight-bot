import requests
import time
import json
import os

from dotenv import load_dotenv

def get_long_ogg_tr(file_name: str) -> str:
    load_dotenv()

    # Укажите ваш IAM-токен и ссылку на аудиофайл в Object Storage.
    key = os.getenv("API_KEY")
    filelink = f"https://storage.yandexcloud.net/bucket-for-speech-kit/downloads/{file_name}"

    POST ='https://transcribe.api.cloud.yandex.net/speech/stt/v2/longRunningRecognize'

    body ={
        "config": {
            "specification": {
                "languageCode": "ru-RU"
            }
        },
        "audio": {
            "uri": filelink
        }
    }

    header = {'Authorization': 'Api-Key {}'.format(key)}

    # Отправьте запрос на распознавание.
    req = requests.post(POST, headers=header, json=body)
    data = req.json()
    print(data)

    id = data['id']

    # Запрашивайте на сервере статус операции, пока распознавание не будет завершено.
    while True:

        time.sleep(1)

        GET = "https://operation.api.cloud.yandex.net/operations/{id}"
        req = requests.get(GET.format(id=id), headers=header)
        req = req.json()

        if req['done']: break
        print("Not ready")

    # Покажите полный ответ сервера в формате JSON.
    print("Response:")
    print(json.dumps(req, ensure_ascii=False, indent=2))

    # Покажите только текст из результатов распознавания.
    text = ""
    print("Text chunks:")
    for chunk in req['response']['chunks']:
        print(chunk['alternatives'][0]['text'])
        text = text + (chunk['alternatives'][0]['text']) + " "

    return text
