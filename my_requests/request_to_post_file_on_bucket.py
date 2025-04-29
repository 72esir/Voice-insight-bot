import boto3

def post_file(file_name: str):
    print("from posting")
    session = boto3.Session()
    s3 = session.client(
        service_name='s3',
        endpoint_url='https://storage.yandexcloud.net',
    )

    with open(f'C:\\Users\\Алексей\\source\\VI_bot\\downloads\\{file_name}', 'rb') as file_data:
        s3.put_object(
            Bucket='bucket-for-speech-kit',
            Key=f'downloads/{file_name}',
            Body=file_data,
            StorageClass='COLD'
        )
    print("file posted")
