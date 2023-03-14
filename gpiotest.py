#! /usr/bin/python3.9
import sys
import RPi.GPIO as GPIO
# import paho.mqtt.client as mqtt
# cpio_channels=[4,5,6,12,13,16,17,18,19,20,21,22,23,24,25,26,27]# base channels
#print("using ",sys.version) #what version of python
#mode=GPIO.getmode()
#print("mode is ",mode)
#GPIO.setmode(GPIO.BCM)
#mode=GPIO.getmode()
#print("mode is ",mode)
#GPIO.setup(4,GPIO.OUT)
#GPIO.output(4,1)
#print("value is ",GPIO.input(4))
#GPIO.setup(5,GPIO.IN)
#print("input value is ",GPIO.input(5))
#GPIO.cleanup()
#print("board ",GPIO.BOARD)
#print("bcm ",GPIO.BCM)

# Define Variables

# BOARD Mode
# GPIO.setmode(GPIO.BOARD) 
# LED_R = 12
# LED_Y = 16
# LED_G = 18
# to use Raspberry Pi board pin numbers

print("using ",sys.version) #what version of python
mode=GPIO.getmode()
print("mode is ",mode)

# BCM Mode
GPIO.setmode(GPIO.BCM)
LED_R = 18
LED_Y = 23
LED_G = 24

mode=GPIO.getmode()
print("mode is ",mode)

#
# set up the GPIO channels: 18 is output; 23 is input; 24 is output
#
GPIO.setup(LED_R, GPIO.OUT)
GPIO.setup(LED_Y, GPIO.IN)
GPIO.setup(LED_G, GPIO.OUT)

# Assign 1 to GPIO LED_R channel
GPIO.output(LED_R,1)
print("GPIO LED_R channel value is ",GPIO.input(LED_R))

# Print out GPIO LED_Y value
print("input GPIO LED_Y channel value is ",GPIO.input(LED_Y))

GPIO.cleanup()
print("board ",GPIO.BOARD)
print("bcm ",GPIO.BCM)