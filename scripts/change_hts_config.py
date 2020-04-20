import configparser
config = configparser.ConfigParser()
args = configparser.ConfigParser()
config.optionxform = lambda option: option
config.read('config.ini')
args.read('../../config.ini')

config.set("DEFAULT", "Port", args["DEFAULT"]["Port"])
config.set("paths", "DRSPath", args["paths"]["DRSPath"])

config.set("minio", "EndPoint", args["minio"]["EndPoint"])
config.set("minio", "AccessKey", args["minio"]["AccessKey"])
config.set("minio", "SecretKey", args["minio"]["SecretKey"])

with open('config.ini', 'w') as configfile:
    config.write(configfile)
