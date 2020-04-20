# Docker-free Candig Deploy

This script aims to automate and deployment of Candig in a Docker-free environment.

Before you run the installation script, you must change the configuration info on `config.ini` file.

`Port`: Port where to run `htsget_app`

`htsget_path`: Address + port of `htsget` service

`DRSPort`: Port to run DRS

`DRSPath`: DRS Endpoint (ex: http://127.0.0.1:8080/ga4gh/dos/v1/)

`EndPoint`: Minio Endpoint

`AccessKey`: Minio Access Key

`SecretKey`: Minio Secret Key


## Running script

Once all the information on `config.ini` file were provided, you may start the installatiion executing the following script

`
sh install.sh
`
