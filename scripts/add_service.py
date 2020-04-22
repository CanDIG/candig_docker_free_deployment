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
hts_address = config["htsget"]["Address"]
htsget_port = config["htsget"]["Port"]

services["services"]["htsget"] = "{}:{}".format(hts_address, htsget_port)
write_json(services)
