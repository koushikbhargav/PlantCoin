
import RPi.GPIO as GPIO
import time
 
import os

channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
 
def callback(channel):
        if GPIO.input(channel):
                print ("Water not Detected!")
                os.system( 'python coin_request-1.py')
        else:
                print ("Water Detected!")
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(channel, callback)
 

while True:
        time.sleep(1)
