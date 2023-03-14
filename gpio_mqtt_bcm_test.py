#! /usr/bin/python3.9
import sys
import time
# Import package
import paho.mqtt.client as mqtt
#add for output
import RPi.GPIO as GPIO


# Define Variables
MQTT_HOST = "192.168.50.240"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 45
MQTT_TOPIC = "pi/GPIO/18"

# BOARD Mode
# GPIO.setmode(GPIO.BOARD) 
# LED_R = 12
# LED_Y = 16
# LED_G = 18
# to use Raspberry Pi board pin numbers

# BCM Mode
GPIO.setmode(GPIO.BCM)
LED_R = 18
LED_Y = 23
LED_G = 24

# set up the GPIO channels - output 
GPIO.setup(LED_R, GPIO.OUT)
GPIO.setup(LED_Y, GPIO.OUT)
GPIO.setup(LED_G, GPIO.OUT)

GPIO.output(LED_R,GPIO.LOW)
GPIO.output(LED_Y,GPIO.LOW)
GPIO.output(LED_G,GPIO.LOW)
time.sleep(1.0)

try:
  # Define on connect event function
  # We shall subscribe to our Topic in this function
    def on_connect(self, mosq, obj, rc):
        mqttc.subscribe(MQTT_TOPIC, 0)
        print("Connect on "+MQTT_HOST)
  # Define on_message event function. 
  # This function will be invoked every time,
  # a new message arrives for the subscribed topic 
    def on_message(mosq, obj, msg):
        message_received=str(msg.payload.decode("utf-8"))
        print ("Topic: " + str(msg.topic)+ " Message: "+message_received)
        print (msg.payload)
        print ("QoS: " + str(msg.qos))
        print('Feed received new value: {0}'.format(msg))

        print ("Topic: " + str(msg.topic))
        print ("QoS: " + str(msg.qos))
        if (message_received=='ON'):
            GPIO.output(LED_R,GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(LED_R,GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(LED_Y,GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(LED_Y,GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(LED_G,GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(LED_G,GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(LED_R,GPIO.HIGH)
            GPIO.output(LED_Y,GPIO.HIGH)
            GPIO.output(LED_G,GPIO.HIGH)
            print ("Topic: " + str(msg.topic))
            print ("QoS: " + str(msg.qos))
        if (message_received=='OFF'):
            GPIO.output(LED_R,GPIO.LOW)
            GPIO.output(LED_Y,GPIO.LOW)
            GPIO.output(LED_G,GPIO.LOW)
            print ("Topic: " + str(msg.topic))
            print ("QoS: " + str(msg.qos))

    def on_subscribe(mosq, obj, mid, granted_qos):
        print("Subscribed to Topic: " + 
        MQTT_TOPIC + " with QoS: " + str(granted_qos))

    # Initiate MQTT Client
    mqttc = mqtt.Client()

    # Assign event callbacks
    mqttc.on_message = on_message
    mqttc.on_connect = on_connect
    mqttc.on_subscribe = on_subscribe

    # Connect with MQTT Broker
    mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)

    # Continue monitoring the incoming messages for subscribed topic
    mqttc.loop_forever()

except KeyboardInterrupt:  
    # here you put any code you want to run before the program   
    # exits when you press CTRL+C
    GPIO.cleanup()  
#finally:  
    #GPIO.cleanup() # this ensures a clean exit  