import os
import configparser
import subprocess

config = configparser.ConfigParser()
config.read('../../config.ini')
MINIO_URL = config["minio"]["EndPoint"] 
MINIO_USERNAME = config["minio"]["AccessKey"]
MINIO_PASSWORD = config["minio"]["SecretKey"]
MINIO_BUCKET = config["minio"]["Bucket"]

drs_port = config["DRS"]["Port"] 

os.environ["MINIO_URL"] = MINIO_URL
os.environ["MINIO_USERNAME"] = MINIO_USERNAME
os.environ["MINIO_PASSWORD"] = MINIO_PASSWORD
os.environ["MINIO_BUCKET"] = MINIO_BUCKET

subprocess.run(["flask", "run", "-p", drs_port])
