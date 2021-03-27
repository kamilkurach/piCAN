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

def do_360_clockwise():
    GPIO.output(DIR, CLOCKWISE)
    for x in range(STEPS_PER_REVOLUTIN):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(.02)
        GPIO.output(STEP, GPIO.LOW)
        sleep(.02)

def do_360_counter_clockwise():
    GPIO.output(DIR, COUNTER_CLOCKWISE)
    for x in range(STEPS_PER_REVOLUTIN):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(.02)
        GPIO.output(STEP, GPIO.LOW)
        sleep(.02)

def do_90_clockwise():
    GPIO.output(DIR, CLOCKWISE)
    for x in range(100):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(.02)
        GPIO.output(STEP, GPIO.LOW)
        sleep(.02)

def do_90_counter_clockwise():
    GPIO.output(DIR, COUNTER_CLOCKWISE)
    for x in range(100):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(.02)
        GPIO.output(STEP, GPIO.LOW)
        sleep(.02)
        