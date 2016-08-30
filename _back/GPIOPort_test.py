#!/usr/python

###GPIO Port read testscript

###Import###
import time
import RPi.GPIO as GPIO

#use GPIO Layout from Raspberry
GPIO.setmode(GPIO.BCM)

#INPUT GPIO
GPIO.setup(17, GPIO.IN)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def function(channel):
	var_value = GPIO.input(17)
	if var_value == GPIO.HIGH:
		print("Pin 17 is HIGH")
	else:
		print("Pin 17 is LOW")

GPIO.add_event_detect(22, GPIO.FALLING, callback=function, bouncetime=300)
while 1:
	time.sleep(1)

