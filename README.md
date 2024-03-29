# Polarisation Switch Control System
Based on Peter 2M0SQL Project https://github.com/magicbug/polarisation-switch 
MANY THANKS Peter :)

Control for the Wimo polarisation switch and LNA power using a [Raspberry Pi 8ch Relay Rxpansion Board](https://a.aliexpress.com/_mLenEXs)

Using Python Flask for the web server functions.

## Polarisation Options
* Horizontal 
* Vertical
* RHCP
* LHCP
* LNA ON/OFF


## How to Install
I used this commands on my RPI 3B+ with Raspberry Pi OS Lite(Legacy - Bullseye):

sudo apt update
sudo apt install git python3-pip
pip install flask flask-cors waitress
git clone https://github.com/PR8KW/polarisation-switch.git
cd polarisation-switch
sudo cp relays.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable relays.service
sudo systemctl start relays.service

## How to Use
Just access from any web browser on your local network: http://"your rpi ip":5000

I use port 5000, if you need to change, just edit app.py file.

FOR PRIVATE/INTERNAL NETWORK ONLY.
if your need external access, please read flask documentation, for security reasons...

Maybe in future will include some interconnection drawings...

73 de PR8KW