import RPi.GPIO as GPIO
from time import sleep

# SETTING LEDs
RED = 19
GREEN = 38
BLUE = 31


# SETTING MODE
GPIO.setmode(GPIO.BOARD)


# SETTING USED GPIO PINS
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)


# LOOPING
try:
    while True:

        GPIO.output(RED, GPIO.HIGH)
        sleep(0.03)
        GPIO.output(RED, GPIO.LOW)

        GPIO.output(GREEN, GPIO.HIGH)
        sleep(0.03)
        GPIO.output(GREEN, GPIO.LOW)

        GPIO.output(BLUE, GPIO.HIGH)
        sleep(0.03)
        GPIO.output(BLUE, GPIO.LOW)

except KeyboardInterrupt:
        GPIO.cleanup()
