import os
import subprocess
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

minio_directory = config["minio"]["directory"]
MINIO_ACCESS_KEY = config["minio"]["AccessKey"]
MINIO_SECRET_KEY = config["minio"]["SecretKey"]

os.environ["MINIO_ACCESS_KEY"] = MINIO_ACCESS_KEY
os.environ["MINIO_SECRET_KEY"] = MINIO_SECRET_KEY

subprocess.run(["./minio", "server", minio_directory])
