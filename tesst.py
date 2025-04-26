#!/usr/bin/env python
#-*- coding: utf-8 -*-
import boto3
session = boto3.Session()
s3 = session.client(
    service_name='s3',
    endpoint_url='https://storage.yandexcloud.net'
)

# Загрузить объекты в бакет

## Из строки
s3.put_object(Bucket='bucket-for-speech-kit', Key='C:\\Users\\Алексей\\source\\VI_bot\\downloads\\THE_MATRIX_Welcome_To_The_Future_Extended_mix_promodj_com.mp3', Body='TEST', StorageClass='COLD')

## Из файла
s3.upload_file('this_script.py', 'bucket-name', 'py_script.py')
s3.upload_file('this_script.py', 'bucket-name', 'script/py_script.py')

# Получить список объектов в бакете
for key in s3.list_objects(Bucket='bucket-name')['Contents']:
    print(key['Key'])

# Удалить несколько объектов
forDeletion = [{'Key':'object_name'}, {'Key':'script/py_script.py'}]
response = s3.delete_objects(Bucket='bucket-name', Delete={'Objects': forDeletion})

# Получить объект
get_object_response = s3.get_object(Bucket='bucket-name',Key='py_script.py')
print(get_object_response['Body'].read())
