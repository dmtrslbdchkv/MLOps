import boto3
from botocore.client import Config
import sys
import os


def first_load(file_paths):
    minio_client = boto3.client(
        's3',
        endpoint_url='http://localhost:9000',
        aws_access_key_id='dmitry',
        aws_secret_access_key='admin0000',
        config=Config(signature_version='s3v4')
    )
    object_name = os.path.basename(file_paths)

    bucket_name = "datasets"
    try:
        minio_client.create_bucket(Bucket=bucket_name)
        print(f"Бакет '{bucket_name}' успешно создан!")
        minio_client.upload_file(file_paths, bucket_name, object_name)
    except minio_client.exceptions.BucketAlreadyExists:
        print(f"Бакет '{bucket_name}' уже существует.")
        minio_client.upload_file(file_paths, bucket_name, object_name)
    except minio_client.exceptions.BucketAlreadyOwnedByYou:
        print(f"Бакет '{bucket_name}' уже существует.")
        minio_client.upload_file(file_paths, bucket_name, object_name)
    except Exception as e:
        print(f"Ошибка при создании бакета: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python first_load.py <path_to_file> ")
        sys.exit(1)
    input_file = sys.argv[1]
    first_load(input_file)
