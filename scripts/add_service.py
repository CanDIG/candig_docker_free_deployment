import json
import configparser

def read_json():
    with open("configs/services.json") as f:
        return json.load(f)

def write_json(services_dict):
    with open("configs/services.json", "w+") as f:
        json.dump(services_dict, f)

config = configparser.ConfigParser()
config.read('../../config.ini')

services = read_json()
services["services"]["htsget"] = config["htsget"]["path"]
write_json(services)
