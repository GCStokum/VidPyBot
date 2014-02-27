import sys
import os
import RPi.GPIO as GPIO
import time


DEBUG = False
RUNNING = True

GPIO.setmode(GPIO.BCM)

LEDR = 24
LEDG = 18
LEDB = 23

LEDRoll = 0

GPIO.setup(LEDR, GPIO.OUT)
GPIO.setup(LEDG, GPIO.OUT)
GPIO.setup(LEDB, GPIO.OUT)

print ('Hello World!')

if DEBUG:
    print('Debug Powers ACTIVATE!')
    RunCount = 1

GPIO.output(LEDR, True)
GPIO.output(LEDG, True)
GPIO.output(LEDB, True)
time.sleep(3)

while RUNNING:

    '''
    #######
    #COLORS
    #######

    if LEDRoll < 5:
        LEDRoll += 1
    else:
        LEDRoll = 0

    if LEDRoll == 0:  # Red
        LEDC = 'Red'
        GPIO.output(LEDR, True)
        GPIO.output(LEDG, False)
        GPIO.output(LEDB, False)

    if LEDRoll == 1:  # Yellow
        LEDC = 'Yellow'
        GPIO.output(LEDR, True)
        GPIO.output(LEDG, True)
        GPIO.output(LEDB, False)

    if LEDRoll == 2:  # Green
        LEDC = 'Green'
        GPIO.output(LEDR, False)
        GPIO.output(LEDG, True)
        GPIO.output(LEDB, False)

    if LEDRoll == 3:  # Cyan
        LEDC = 'Cyan'
        GPIO.output(LEDR, False)
        GPIO.output(LEDG, True)
        GPIO.output(LEDB, True)

    if LEDRoll == 4:  # Blue
        LEDC = 'Blue'
        GPIO.output(LEDR, False)
        GPIO.output(LEDG, False)
        GPIO.output(LEDB, True)

    if LEDRoll == 5:  # Violet
        LEDC = 'Violet'
        GPIO.output(LEDR, True)
        GPIO.output(LEDG, False)
        GPIO.output(LEDB, True)

    if DEBUG:
        print(LEDRoll)
        print(LEDC)
        time.sleep(1)
        RunCount += 1

        if RunCount >=25:
            GPIO.output(LEDR, False)
            GPIO.output(LEDG, False)
            GPIO.output(LEDB, False)
            exit()
    time.sleep(.033)
    '''
