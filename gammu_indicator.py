#!/usr/bin/env python
import subprocess
import RPi.GPIO as GPIO
import time

#Initialize the LEDS
GPIO.setmode(GPIO.BCM)

GSM_LED = 18
LAN_LED = 23

#Set frequency with which to check the settings
GSM_CHECK_FREQ = 60 #60 Seconds

GPIO.setup(GSM_LED, GPIO.OUT)
GPIO.setup(LAN_LED, GPIO.OUT)
while True:

    if subprocess.call(["sudo", "gammu", "--identify"]) == 0:
        GPIO.output(GSM_LED, True)
        print "Success!"
    else:
        GPIO.output(GSM_LED, False)
        print "Error"
    time.sleep(GSM_CHECK_FREQ)
