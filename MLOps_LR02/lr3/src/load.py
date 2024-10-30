import sys
import boto3
from botocore.client import Config


def load(name_file, object_name):
    minio_client = boto3.client(
        's3',
        endpoint_url='http://localhost:9000',
        aws_access_key_id='dmitry',
        aws_secret_access_key='admin0000',
        config=Config(signature_version='s3v4')
    )

    bucket_name = "datasets"
    minio_client.upload_file(name_file, bucket_name, object_name)


if __name__ == "__main__":

    if len(sys.argv) < 3:
        print("Usage: python extract.py <object_name> <name_file> ")
        sys.exit(1)

    file_name = sys.argv[1]
    save_file = sys.argv[2]
    load(file_name, save_file)
