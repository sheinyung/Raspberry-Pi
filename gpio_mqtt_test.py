#! /usr/bin/python3.9
import sys
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt

# Define GPIO parameters
GPIO.setmode(GPIO.BCM)	#set numbering scheme
LED_R = 18
LED_Y = 23
LED_G = 24
GPIO.setup(LED_R,GPIO.OUT) #set GPIO LED_R(18) as output.

# Define Variables
MQTT_HOST = "192.168.50.240"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 45
MQTT_TOPIC = "pi/GPIO/18"

# Creating a Client Instance
# client =mqtt.Client(client_name)

# Connecting To a Broker or Server
# connect(host, port=1883, keepalive=60, bind_address="")

# Publishing Messages
# publish(topic, payload=None, qos=0, retain=False)

# Subscribing To Topics
# subscribe(topic, qos=0)
# So our script outline becomes.
# 1. Create new client instance
# 2. Connect to broker
# 3. Subscribe to topic
# 4. Publish message


print("Creating new instance")
client = mqtt.Client() #create new instance
print("Connecting to broker： "+MQTT_HOST)
client.connect(MQTT_HOST) #connect to broker

print("Publishing message to topic："+MQTT_TOPIC)
print("GPIO LED_R value is ", GPIO.input(LED_R))

GPIO.output(LED_R,1) #set value of LED_R to True or 1
client.publish(MQTT_TOPIC,GPIO.input(LED_R))

print("Connect on： "+MQTT_HOST)
print("GPIO LED_R value is ",GPIO.input(LED_R))

GPIO.output(LED_R, False) #set value of LED_R to False or 0
print("GPIO LED_R value is ", GPIO.input(LED_R))
client.connect(MQTT_HOST) #connect to broker
client.publish(MQTT_TOPIC,GPIO.input(LED_R))
print("Connect on： "+MQTT_HOST)
print("GPIO LED_R value is ",GPIO.input(LED_R))
GPIO.cleanup()