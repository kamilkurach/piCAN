# helper functions
from time import sleep 
import RPi.GPIO as GPIO

def GPIO_setup():
    # Direction PIN 
    DIR = 17 

    # Step PIN
    STEP = 27

    # Clockwise
    CLOCKWISE = 1

    # Counter Clockwise
    COUNTER_CLOCKWISE = 0

    # 360 / 0.9 (0.9*/step)
    STEPS_PER_REVOLUTIN = 400

    # GPIO BCM PIN  
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(DIR, GPIO.OUT)
    GPIO.setup(STEP, GPIO.OUT)

    # set current to 1.5A
    GPIO.setup(5, GPIO.OUT)
    GPIO.setup(6, GPIO.OUT)
    GPIO.output(5, GPIO.HIGH)
    GPIO.output(6, GPIO.LOW)
