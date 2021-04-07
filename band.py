from RPi import GPIO
from time import sleep

class Aha:
    def __init__(self):
        # Direction PIN
        self.DIR = 17
        # Step PIN
        self.STEP = 27
        # I1, I2
        self.I1 = 5
        self.I2 = 6

        # Notes Freq
        self.A3 = 220
        self.F3 = 174.61
        self.D3 = 146.83
        self.G3 = 196
        self.B3 = 246.94
        self.C4 = 261.63
        self.D4 = 293.66
        self.E3 = 164.81

        # init setup
        self.GPIO_setup()
        self.notes = [(self.A3, 0.2), (self.A3, 0.2), (self.F3, 0.2), (self.D3, 0.3), (self.D3, 0.3), (self.G3, 0.2),
        (self.G3, 0.2), (self.G3, 0.2), (self.B3, 0.2), (self.B3, 0.2), (self.C4, 0.2), (self.D4, 0.2), 
        (self.C4, 0.2), (self.C4, 0.2), (self.C4, 0.2), (self.G3, 0.3), (self.E3, 0.3),
        (self.A3, 0.2), (self.A3, 0.2), (self.A3, 0.2), (self.G3, 0.2), (self.G3, 0.2), (self.A3, 0.2), (self.G3, 0.2)]
        
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

    def take_on_me(self): 
        init_freq = 50
        pwm = GPIO.PWM(self.STEP, init_freq)
        for _ in range(3):
            for tup in self.notes:
                _note = tup[0]
                _time = tup[1]
                pwm.ChangeFrequency(_note)
                pwm.start(1)
                sleep(_time)
                pwm.stop()
