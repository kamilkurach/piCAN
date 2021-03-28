# helper functions
from time import sleep 
import RPi.GPIO as GPIO

class Motor:
    def __init__(self):
        # Direction PIN 
        self.DIR = 17 
        # Step PIN
        self.STEP = 27
         # I1, I2
        self.I1 = 5
        self.I2 = 6
        # Sleep duration
        self.SLEEP = .02
        # Clockwise
        self.CLOCKWISE = 0
        # Counter Clockwise
        self.COUNTER_CLOCKWISE = 1
        # 360 / 0.9 (0.9*/step)
        self.STEPS_PER_REVOLUTIN = 400
        # 90 
        self.STEPS_PER_REVOLUTIN_90 = 100
        # setup
        self.GPIO_setup()

    def GPIO_setup(self):
        # GPIO BCM PIN  
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.DIR, GPIO.OUT)
        GPIO.setup(self.STEP, GPIO.OUT)

        # set current to 1.5A
        GPIO.setup(self.I1, GPIO.OUT)
        GPIO.setup(self.I2, GPIO.OUT)
        GPIO.output(self.I1, GPIO.HIGH)
        GPIO.output(self.I2, GPIO.LOW)

    def do_360_clockwise(self):
        GPIO.output(self.DIR, self.CLOCKWISE)
        for x in range(self.STEPS_PER_REVOLUTIN):
            GPIO.output(self.STEP, GPIO.HIGH)
            sleep(self.SLEEP)
            GPIO.output(self.STEP, GPIO.LOW)
            sleep(self.SLEEP)

    def do_360_counter_clockwise(self):
        GPIO.output(self.DIR, self.COUNTER_CLOCKWISE)
        for x in range(self.STEPS_PER_REVOLUTIN):
            GPIO.output(self.STEP, GPIO.HIGH)
            sleep(self.SLEEP)
            GPIO.output(self.STEP, GPIO.LOW)
            sleep(self.SLEEP)

    def do_90_clockwise(self):
        GPIO.output(self.DIR, self.CLOCKWISE)
        for x in range(self.STEPS_PER_REVOLUTIN_90):
            GPIO.output(self.STEP, GPIO.HIGH)
            sleep(self.SLEEP)
            GPIO.output(self.STEP, GPIO.LOW)
            sleep(self.SLEEP)

    def do_90_counter_clockwise(self):
        GPIO.output(self.DIR, self.COUNTER_CLOCKWISE)
        for x in range(self.STEPS_PER_REVOLUTIN_90):
            GPIO.output(self.STEP, GPIO.HIGH)
            sleep(self.SLEEP)
            GPIO.output(self.STEP, GPIO.LOW)
            sleep(self.SLEEP)

    def do_360_clockwise_set_sleep(self, sleep_value):
        GPIO.output(self.DIR, self.CLOCKWISE)
        for x in range(self.STEPS_PER_REVOLUTIN):
            GPIO.output(self.STEP, GPIO.HIGH)
            sleep(sleep_value)
            GPIO.output(self.STEP, GPIO.LOW)
            sleep(sleep_value)
