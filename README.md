# Docker-free Candig Deployment

This script aims to automate the deployment of Candig in a Docker-free environment.

Before you run the installation script, you must change the configuration info on `config.ini` file. 

Bellow a description of each section/field in `config.ini`

#### htsget Section
`Address`: Address of htsget app

`Port`: Port where to run `htsget_app`

#### DRS Section
`Address`: Address of Chord DRS service

`Port`: Port where to run Chord DRS service

`Endpoint`: DRS endpoint (such as /ga4gh/dos/v1/)

#### Minio Section
`EndPoint`: Minio Endpoint

`AccessKey`: Minio Access Key

`SecretKey`: Minio Secret Key


## Running all the services

Once all the information on `config.ini` file were provided, you may browse the cloned repository and execute bellow command to start the services
```
sh install.sh
```
