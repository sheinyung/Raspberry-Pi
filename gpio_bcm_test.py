#! /usr/bin/python3.9
import sys
import time
# Import package
import RPi.GPIO as GPIO

cpio_channels=[4,5,6,12,13,16,17,18,19,20,21,22,23,24,25,26,27]# base channels

# Define Variables
# BOARD Mode
# to use Raspberry Pi board pin numbers
# GPIO.setmode(GPIO.BOARD) 
# LED_R = 12
# LED_Y = 16
# LED_G = 18


# BCM Mode
GPIO.setmode(GPIO.BCM)
LED_R = 18
LED_Y = 23
LED_G = 24

# set up the GPIO channels - output 
GPIO.setup(LED_R, GPIO.OUT)
GPIO.setup(LED_Y, GPIO.OUT)
GPIO.setup(LED_G, GPIO.OUT)

GPIO.output(LED_R,GPIO.HIGH)
GPIO.output(LED_Y,GPIO.HIGH)
GPIO.output(LED_G,GPIO.HIGH)
time.sleep(1.0)
GPIO.output(LED_R,GPIO.LOW)
GPIO.output(LED_Y,GPIO.LOW)
GPIO.output(LED_G,GPIO.LOW)
time.sleep(1.0)

try:
    
    GPIO.output(LED_R,GPIO.HIGH)
    time.sleep(1.0)
    GPIO.output(LED_R,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(LED_R,GPIO.HIGH)
    GPIO.output(LED_Y,GPIO.HIGH)
    time.sleep(1.0)
    GPIO.output(LED_Y,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(LED_Y,GPIO.HIGH)
    GPIO.output(LED_G,GPIO.HIGH)
    time.sleep(1.0)
    GPIO.output(LED_G,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(LED_G,GPIO.HIGH)
    time.sleep(3.0)
except KeyboardInterrupt:  
    # here you put any code you want to run before the program   
    # exits when you press CTRL+C
    GPIO.cleanup()  
finally:  
    GPIO.cleanup() # this ensures a clean exit  