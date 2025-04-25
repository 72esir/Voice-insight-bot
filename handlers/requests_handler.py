import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

"""Requests to SpeechKit"""
FOLDER_ID = os.getenv("FOLDER_ID")
API_KEY = os.getenv("API_KEY")

def send_req_to_kit(file_name) -> str:
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


"""Requests to DeepSeek R-1"""
API_KEY_AI = os.getenv("API_KEY_AI")

def process_content(content):
    return content.replace('<think>', '').replace('</think>', '')

def send_req_to_DS(prompt) -> str:
    headers = {
        "Authorization": f"Bearer {API_KEY_AI}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "deepseek/deepseek-r1",
        "messages": [{"role": "user", "content": prompt}],
        "stream": True
    }

    with requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=data,
        stream=True
    ) as response:
        if response.status_code != 200:
            print("Ошибка API:", response.status_code)
            return ""

        full_response = []

        for chunk in response.iter_lines():
            if chunk:
                chunk_str = chunk.decode('utf-8').replace('data: ', '')
                try:
                    chunk_json = json.loads(chunk_str)
                    if "choices" in chunk_json:
                        content = chunk_json["choices"][0]["delta"].get("content", "")
                        if content:
                            cleaned = process_content(content)
                            print(cleaned, end='', flush=True)
                            full_response.append(cleaned)
                except:
                    pass

        print()
        return ''.join(full_response)
