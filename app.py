'''

Polarisation Switching Flask application

Developed by Peter Goodhall 2M0SQL
Complete project details: https://github.com/magicbug/polarisation-switch

'''

import RPi.GPIO as GPIO
from os import popen
from flask import Flask, render_template, request, redirect
from flask_cors import CORS
from waitress import serve

app = Flask(__name__)
CORS(app)

GPIO.setmode(GPIO.BCM)

# Create a dictionary called pins to store the pin number, name, and pin state:
pins = {
   5 : {'name' : 'GPIO 5', 'state' : GPIO.LOW},
   6 : {'name' : 'GPIO 6', 'state' : GPIO.LOW},
   13 : {'name' : 'GPIO 13', 'state' : GPIO.LOW},
   16 : {'name' : 'GPIO 16', 'state' : GPIO.LOW},
   19 : {'name' : 'GPIO 19', 'state' : GPIO.LOW},
   20 : {'name' : 'GPIO 20', 'state' : GPIO.LOW},
   21 : {'name' : 'GPIO 21', 'state' : GPIO.LOW},
   26 : {'name' : 'GPIO 26', 'state' : GPIO.LOW},
   }

Phase_70cm = 'v'
Phase_2m = 'v'
LNA_2m = 'off'
LNA_70cm = 'off'
temp = '0'

def get_temp():
    temperature = popen('vcgencmd measure_temp').readline()
    return (temperature.replace("\n", "").replace("temp=", "").replace("'C", ""))

def set_2m_v():
	GPIO.output(5, GPIO.HIGH)
	GPIO.output(6, GPIO.HIGH)
	GPIO.output(13, GPIO.HIGH)

def set_2m_h():
	GPIO.output(5, GPIO.LOW)
	GPIO.output(6, GPIO.HIGH)
	GPIO.output(13, GPIO.HIGH)

def set_2m_rhcp():
	GPIO.output(5, GPIO.LOW)
	GPIO.output(6, GPIO.LOW)
	GPIO.output(13, GPIO.HIGH)

def set_2m_lhcp():
	GPIO.output(5, GPIO.LOW)
	GPIO.output(6, GPIO.LOW)
	GPIO.output(13, GPIO.LOW)

def set_2m_lnaON():
	GPIO.output(16, GPIO.LOW)

def set_2m_lnaOFF():
	GPIO.output(16, GPIO.HIGH)

def set_70cm_v():
	GPIO.output(19, GPIO.HIGH)
	GPIO.output(20, GPIO.HIGH)
	GPIO.output(21, GPIO.HIGH)

def set_70cm_h():
	GPIO.output(19, GPIO.LOW)
	GPIO.output(20, GPIO.HIGH)
	GPIO.output(21, GPIO.HIGH)

def set_70cm_rhcp():
	GPIO.output(19, GPIO.LOW)
	GPIO.output(20, GPIO.LOW)
	GPIO.output(21, GPIO.HIGH)

def set_70cm_lhcp():
	GPIO.output(19, GPIO.LOW)
	GPIO.output(20, GPIO.LOW)
	GPIO.output(21, GPIO.LOW)

def set_70cm_lnaON():
	GPIO.output(26, GPIO.LOW)

def set_70cm_lnaOFF():
	GPIO.output(26, GPIO.HIGH)

# Set each pin as an output and make it high:
for pin in pins:
   GPIO.setup(pin, GPIO.OUT)
   GPIO.output(pin, GPIO.HIGH)

@app.route("/")
def main():
   global Phase_70cm 
   global Phase_2m
   global LNA_2m
   global LNA_70cm
   global temp
   temp = get_temp()
   
   templateData = {
      'Phase_2m' : Phase_2m,
      'Phase_70cm': Phase_70cm,
      'LNA_2m': LNA_2m,
      'LNA_70cm': LNA_70cm,
      'temp': temp
      }
   # Pass the template data into the template main.html and return it to the user
   return render_template('main.html', **templateData)

@app.route("/2m/<phase>")
def set2mphase(phase):
   global Phase_2m
   global LNA_2m

   deviceName = phase

   if phase== "rhcp":
      set_2m_rhcp()
      Phase_2m = "rhcp"

   if phase == "lhcp":
      set_2m_lhcp()
      Phase_2m = "lhcp"

   if phase == "v":
      set_2m_v()
      Phase_2m = "v"

   if phase == "h":
      set_2m_h()
      Phase_2m = "h"

   if phase == "lnaon":
      set_2m_lnaON()
      LNA_2m = "on"

   if phase == "lnaoff":
      set_2m_lnaOFF()
      LNA_2m = "off"

   return redirect("/")

@app.route("/70cm/<phase>")
def set70cmphase(phase):
   global Phase_70cm 
   global LNA_70cm

   deviceName = phase

   if phase== "rhcp":
      set_70cm_rhcp()
      Phase_70cm = "rhcp"

   if phase == "lhcp":
      set_70cm_lhcp()
      Phase_70cm = "lhcp"

   if phase == "v":
      set_70cm_v()
      Phase_70cm = "v"

   if phase == "h":
      set_70cm_h()
      Phase_70cm = "h"

   if phase == "lnaon":
      set_70cm_lnaON()
      LNA_70cm = "on"

   if phase == "lnaoff":
      set_70cm_lnaOFF()
      LNA_70cm = "off"

   return redirect("/")

if __name__ == "__main__":
   serve(app, host='0.0.0.0', port=5000)
