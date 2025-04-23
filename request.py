import os
import requests
from dotenv import load_dotenv


load_dotenv()
FOLDER_ID = os.getenv("FOLDER_ID")
API_KEY = os.getenv("API_KEY")

def send_req(file_name) -> str:
    headers = {
        'Authorization': f'Api-Key {API_KEY}',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    params = {
        'folderId': FOLDER_ID,
        'lang': 'ru-RU',
    }

    with open(f'downloads/{file_name}', 'rb') as f:
        data = f.read()

    os.remove(f'downloads/{file_name}')

    response = requests.post('https://stt.api.cloud.yandex.net/speech/v1/stt:recognize', params=params, headers=headers, data=data)
    if response.status_code == 200:
        response_json = response.json()
        return response_json.get('result', 'Ключ "result" не найден')
    else:
        return f"Ошибка: {response.status_code}"
