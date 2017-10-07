import RPi.GPIO as gpio
import time
from . import views
while True:
    gpio.setmode(gpio.BCM)
    gpio.setup(21,gpio.OUT)

    moisture=views.aa()
    print(moisture)
    print moisture
    if(moisture>600):
        gpio.output(21,gpio.HIGH)
    else:
        gpio.output(21,gpio.LOW)
    time.sleep(2)
