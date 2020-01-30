# Foodiebear Pet Feeder (Part I. Hardware)

## 1. Project Overview
Foodiebear Pet Feeder provides pet owners the freedom to feed their loved ones whenever, wherever. This project includes a DIY pet feeder powered by raspberry pi, a MERN web app powerd by Azure cloud platform, and a Alexa skill powered by AWS Lambda. Whether your pets need to be fed breakfast before you wake up, dinner while you're working late, or simply a treate when you are busy in the house, you should stay tuned and support this awesome porject :dog::cat::panda_face:

To learn more about this project, please read the initial product plan [here](https://gist.github.com/rinostar/a79a67ce073be1d7e5be2e4a55bb714e) or the final architecture diagrgam below:
![Foodiebear](https://user-images.githubusercontent.com/52188117/72955297-63148f00-3d93-11ea-8377-74b722fa7012.png)

## 2. Repo Description
This is the hardware part of the FoodieBear Pet Feeder project. This repo contains instructions to assemble the parts, create server on Raspberry Pi, and register the device with Azure IoT Hub.

## 3. Getting Started

### a). Assemble hardware parts:
Materials:
* Raspberry Pi Revision 2 (w/ SD Card, Wifi Adapter)
* [L298N Motor Driver](https://www.amazon.com/Controller-H-Bridge-Stepper-Mega2560-Duemilanove/dp/B01BWLICV4/ref=sr_1_2_sspa?keywords=kuman+l298n+driver&qid=1579745184&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUE0Qk9EOTZKMVpTTkImZW5jcnlwdGVkSWQ9QTAzOTUyNzQyQlFGNTlMTkk5NzdFJmVuY3J5cHRlZEFkSWQ9QTA2MjkzNzI5TkpKSUpHNTVBUTEmd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl)
* [DC Motor](https://www.amazon.com/gp/product/B00B1KXV3Q/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=diypetfeeder-20&creative=9325&linkCode=as2&creativeASIN=B00B1KXV3Q&linkId=756daa6a2c6ccf261b6fed7343b18aa8)
* [Motor Coupler](https://www.amazon.com/a15102700ux1222-Aluminium-Coupling-Connector-Aluminum/dp/B019DCWGUW)
* [Food Dispenser](https://www.amazon.com/gp/product/B000NW5RRG/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=diypetfeeder-20&creative=9325&linkCode=as2&creativeASIN=B000NW5RRG&linkId=7a9d90a3d771dbb2afa7379dab8f39fe)
* [Breadboard Jumper Wires](https://www.amazon.com/MCIGICM-Breadboard-Jumper-Wires-Female/dp/B07PLZC26F/ref=sr_1_5?keywords=mcigicm+breadboard+jumper+wires&qid=1579745144&sr=8-5)
* [AC Adapter](https://www.amazon.com/100-240V-Transformers-Switching-Applications-Connectors/dp/B077PW5JC3)

Connect Pi with the DC motor through L298N driver:
<br />https://www.youtube.com/watch?v=2bganVdLg5Q
<br />https://howchoo.com/g/mjg5ytzmnjh/controlling-dc-motors-using-your-raspberry-pi
<br />NOTE: Please refer to this GPIO Pinout [diagram](https://www.raspberrypi.org/forums/viewtopic.php?t=154124)

Attach DC motor to the food dispencer:
<br />Reference the "Modify Dispencer" session under "Setup Box Components" of this [tutorial](https://docs.google.com/document/d/12b4Bzq5u67sQ7vvfZI9Wh92H_r2RVhh2vrMzNrYyuPc/edit#heading=h.ebz1dxhpidc1)

### b). Add Python code to Raspberry Pi: 
Dependencies:
* python 3
* RPi.GPIO
* azure-iot-device
* azure-iot-hub
<br />NOTE: Please use `$ pip3 install <library-name>` for needed

Python code for server on Rasberry Pi:
See details in the pypi.py file within this repo

### c). Register the device with Azure IoT Hub:
Open an account with Azure and add the following services to your account:
[IoT hub] (https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-create-through-portal)

Create .env file and update the "DEVICE_CONNECTION_STRING" accordingly

### d). Turn on pet feeder & Run the server
Be sure to follow the orders:
* Plug in power for the moto driver first
* Plug in power for the Pi
* SSH into the Pi from your computer - [Instruction](https://electricnoodlebox.wordpress.com/tutorials/remote-view-your-raspberry-pi-on-mac-using-vnc/)
* Setup wifi on your Pi - [Instruction](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-3-network-setup/setting-up-wifi-with-occidentalis)
* cd into the root folder and run `$ python3 pypi.py`

## 4. Other Repos:
* Software (MERN app): https://github.com/rinostar/capstone-petfeeder-app
* Alexa Feature: https://github.com/rinostar/capstone-petfeeder-alexa

## 5. Author & Contact
Github: [@rinostar](https://github.com/rinostar)
<br />Email: codingrinostar@gmail.com

## 6. Acknowledgments
In addition to authors of the links mentioned above, I want to thank: 
* [diy petfeeder](https://www.youtube.com/channel/UCnDOhfA1Y8OODhTrmgLJAcg) on Youtube for the inspiration,
* [redklouds](https://github.com/redklouds) on github for the collobration, 
* and [Ada](https://adadevelopersacademy.org/) community for the support.

Thank you! Until next time 🌟
