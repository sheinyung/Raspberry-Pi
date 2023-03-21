import os
import time
# Import package
import paho.mqtt.client as mqtt
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

# Define Variables
MQTT_HOST = "192.168.50.240"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 45
MQTT_TOPIC = "pi/GPIO/18"

# Initiate MQTT Client
mqttc = mqtt.Client()
# Assign event callbacks


# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D5)

# create the mcp object
mcp = MCP.MCP3008(spi, cs)

# create an analog input channel on pin 0
chan = AnalogIn(mcp, MCP.P0)
STATUS = "OFF"

while True:
    def on_connect(self, mosq, obj, rc):
        print("Connect on "+MQTT_HOST)


    print('Raw ADC Value: ', chan.value)
    print('ADC Voltage: ' + str(chan.voltage) + 'V')
    if (chan.value < 56000):
        if (STATUS=="ON"):
            # Connect with MQTT Broker
            STATUS = "OFF"
            mqttc.on_connect = on_connect
            mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)
            mqttc.publish(MQTT_TOPIC, payload= STATUS, qos=0, retain=False)
            print('Send message '+ STATUS)
    elif (chan.value > 65000):
        if (STATUS=='OFF'):
            STATUS = "ON"
            mqttc.on_connect = on_connect
            mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)
            mqttc.publish(MQTT_TOPIC, payload= STATUS, qos=0, retain=False)
            print('Send message '+ STATUS)
    time.sleep(0.5)

