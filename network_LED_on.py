#!/usr/bin/env python
import subprocess
import RPi.GPIO as GPIO
import time

#Initialize the LEDS
GPIO.setmode(GPIO.BCM)

LAN_LED = 23

GPIO.setup(LAN_LED, GPIO.OUT)
GPIO.output(LAN_LED, True)
