import RPi.GPIO as GPIO
import time

debug = True
running = True

GPIO.setmode(GPIO.BCM)
LEDR = 18
LEDG = 24
LEDB = 23