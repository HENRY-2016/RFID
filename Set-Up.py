

RFID and Raspberry Pi Connections : (BOARD Mode)

SDA ===> Pin 24  
SCK ===> Pin 23 
MOSI ===> Pin 19  
MISO ===> Pin 21
GND ===> Pin 6  
RST ===> Pin 22 
3.3v ===> Pin 1


CMDS 04-01-2024
===============

sudo raspi-config
sudo reboot
sudo atp-get update
sudo atp-get upgrade
sudo apt-get install python3-dev python3-pip

Create a dir and virtual env
    python3 -m venv .venv
        source .venv/bin/activate
        python3 -m pip install spidev
        python3 -m pip install mfrc522
    Running Scripts
        source .venv/bin/activate
        python3 write.py
        python3 read.py 

Raspberry pi
    Username :: mogahenze
    Password :: mogahenze
