# RPI Config PiCar

## Prerequisite
* python 3.4
* pip3

## Build process

Install required packages using pip3 and the requirements.txt

```
pip3 install -r requirements.tx
```

Create a config.yml from the config.yml.template populating values for your picar setup.

machine = meta-raspberry machine specification to populate on the local.conf
wireless_ssid = wireless ssid that you want the raspberry pi to connect to if you want wifi
wireless_psk = Password for the wireless ssid that you want to connect to
root_passoword = Password for the root user on the yocto installation
