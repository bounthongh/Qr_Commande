#### git (master)

[![pipeline status](https://gitlab.com/QRCommande/qrcommande/badges/master/pipeline.svg)](https://gitlab.com/QRCommande/qrcommande/commits/master)
[![coverage report](https://gitlab.com/QRCommande/qrcommande/badges/master/coverage.svg)](https://gitlab.com/QRCommande/qrcommande/commits/master)

#### git (dev)

[![pipeline status](http://192.168.1.19/root/daisy/badges/dev/pipeline.svg)](http://192.168.1.19/root/daisy/commits/dev)
[![coverage report](http://192.168.1.19/root/daisy/badges/dev/coverage.svg?job=test)](http://192.168.1.19/root/daisy/commits/dev)

# QRCOmmande

This program is an API that shows you the products available. You can choose and select what you want, and send the command list to the bar.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.


![alt text](doc/QRCommande_schema.png)

### Prerequisites

QRCommande need python3 on your linux (debian) production server.

```bash
$ sudo apt-get install python3 python3-pip
```

### Installing

The 'requirements.txt' include all the dependencies needed by QRCommande.

To install them without 'virtualenv', just type this command :

```bash
$ sudo pip3 install -r requirements.txt
```

With 'virtualenv' :

Take care!!! virtualenv have to run with python3 :

```bash
$ virtualenv -p python3 name_folder
```

```bash
$ pip install -r requirements.txt
```

### Running

```bash
$ python3 run.py
```
Or in a virtualenv :

```bash
$ python run.py
```


### Routing
