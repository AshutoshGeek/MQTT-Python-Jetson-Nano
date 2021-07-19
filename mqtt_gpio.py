#!/usr/bin/env python
# Author: Ashutosh Mohanty
# Date created: 19/07/2021

import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
import time

print("Starting demo now! Press CTRL+C to exit")
GPIO.setwarnings(False)

def print_msg(client, userdata, message):
    # Pin Definitions
    output_pin = 7
    # Pin Setup:
    # GPIO.setmode(GPIO.BCM)  # BCM pin-numbering scheme from Raspberry Pi
    GPIO.setmode(GPIO.BOARD)
    # set pin as an output pin with optional initial state of HIGH
    GPIO.setup(output_pin, GPIO.OUT, initial=GPIO.HIGH)

    message_topic = message.topic
    message_payload = message.payload
    message_payload = message_payload.decode('utf-8')
    print("%s : %s" % (message.topic, message.payload))

    if message_payload == '1':
        print("Outputting {} to pin {}".format(GPIO.HIGH, output_pin))
        GPIO.output(output_pin, GPIO.HIGH)
        print("Light 1 turned ON")
    elif message_payload == '0':
        print("Outputting {} to pin {}".format(GPIO.LOW, output_pin))
        GPIO.output(output_pin, GPIO.LOW)
        print("Light 1 turned OFF")
    print("======================")
subscribe.callback(print_msg, "sensors/light1", hostname="mqtt.eclipseprojects.io")