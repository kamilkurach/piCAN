# helper functions
from time import sleep 
import RPi.GPIO as GPIO

def GPIO_setup():
    # Direction PIN 
    DIR = 17 

    # Step PIN
    STEP = 27

    # I1, I2
    I1 = 5
    I2 = 6

    # Sleep duration
    SLEEP = .02

    # Clockwise
    CLOCKWISE = 0

    # Counter Clockwise
    COUNTER_CLOCKWISE = 1

    # 360 / 0.9 (0.9*/step)
    STEPS_PER_REVOLUTIN = 400

    # 90 
    STEPS_PER_REVOLUTIN_90 = 100

    # GPIO BCM PIN  
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(DIR, GPIO.OUT)
    GPIO.setup(STEP, GPIO.OUT)

    # set current to 1.5A
    GPIO.setup(I1, GPIO.OUT)
    GPIO.setup(I2, GPIO.OUT)
    GPIO.output(I1, GPIO.HIGH)
    GPIO.output(I2, GPIO.LOW)

def do_360_clockwise():
    GPIO.output(DIR, CLOCKWISE)
    for x in range(STEPS_PER_REVOLUTIN):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(SLEEP)
        GPIO.output(STEP, GPIO.LOW)
        sleep(SLEEP)

def do_360_counter_clockwise():
    GPIO.output(DIR, COUNTER_CLOCKWISE)
    for x in range(STEPS_PER_REVOLUTIN):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(SLEEP)
        GPIO.output(STEP, GPIO.LOW)
        sleep(SLEEP)

def do_90_clockwise():
    GPIO.output(DIR, CLOCKWISE)
    for x in range(STEPS_PER_REVOLUTIN_90):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(SLEEP)
        GPIO.output(STEP, GPIO.LOW)
        sleep(SLEEP)

def do_90_counter_clockwise():
    GPIO.output(DIR, COUNTER_CLOCKWISE)
    for x in range(STEPS_PER_REVOLUTIN_90):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(.02)
        GPIO.output(STEP, GPIO.LOW)
        sleep(.02)
