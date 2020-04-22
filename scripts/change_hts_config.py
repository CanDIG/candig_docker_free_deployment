import configparser
config = configparser.ConfigParser()
args = configparser.ConfigParser()
config.optionxform = lambda option: option
config.read('config.ini')
args.read('../../config.ini')

config.set("DEFAULT", "Port", args["htsget"]["Port"])
drs_address = args["DRS"]["Address"] 
drs_port = args["DRS"]["Port"] 
drs_endpoint = args["DRS"]["Endpoint"] 

config.set("paths", "DRSPath", "{}:{}{}".format(drs_address, drs_port, drs_endpoint))

config.set("minio", "EndPoint", args["minio"]["EndPoint"])
config.set("minio", "AccessKey", args["minio"]["AccessKey"])
config.set("minio", "SecretKey", args["minio"]["SecretKey"])

with open('config.ini', 'w') as configfile:
    config.write(configfile)
