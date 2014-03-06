import sys
import os
import RPi.GPIO as GPIO
import time
import pygame

DEBUG = False
RUNNING = True
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
pygame.init()

screen = pygame.display.set_mode([50,50])

ObjStep = 22
ObjDir = 27
SlideStep = 17
SlideDir = 4
LEDR = 24
LEDG = 18
LEDB = 23
#LEDRoll = 0
StepPause = 0.005 #0.001

GPIO.setup(LEDR, GPIO.OUT)
GPIO.setup(LEDG, GPIO.OUT)
GPIO.setup(LEDB, GPIO.OUT)
GPIO.setup(ObjStep, GPIO.OUT)
GPIO.setup(ObjDir, GPIO.OUT)
GPIO.setup(SlideStep, GPIO.OUT)
GPIO.setup(SlideDir, GPIO.OUT)

print ('Hello World!')

LR = False
LG = False
LB = False

if DEBUG:
    print('Debug Powers ACTIVATE!')
    RunCount = 1

GPIO.output(LEDR, True)
GPIO.output(LEDG, True)
GPIO.output(LEDB, True)
time.sleep(2)

while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP1:
                LR = not LR
                #print(LR)
            if event.key == pygame.K_KP2:
                LG = not LG
                #print(LG)
            if event.key == pygame.K_KP3:
                LB = not LB
                #print(LB)
                

            if event.key == pygame.K_KP7:
                ObjRun = True
                ObjDir = True
                #print(LR)
            if event.key == pygame.K_KP8:
                ObjRun = False
                #print(LG)
            if event.key == pygame.K_KP9:
                ObjRun = True
                ObjDir = False
                #print(LB)

            if event.key == pygame.K_KP4:
                print('4')
            if event.key == pygame.K_KP5:
                #print(LG)
            if event.key == pygame.K_KP6:
                #print(LB)


    GPIO.output(LEDR, LR)
    GPIO.output(LEDG, LG)
    GPIO.output(LEDB, LB)

    if ObjRun is True:

    else:
        # No Object Run

'''
    ###############
    #STEPPER MOTORS
    ###############

while x <= 5:
    print(x)
    x = x + 1
    i = 0
    j = 0

    time.sleep(1)
    GPIO.output(DirPin, GPIO.HIGH)

    while i <= 250:
        i = i + 1
        GPIO.output(StepPin, GPIO.HIGH)
        time.sleep(pause)
        GPIO.output(StepPin, GPIO.LOW)
        time.sleep(pause)
        
    time.sleep(.5)
    GPIO.output(DirPin, GPIO.LOW)

    while j <= 250:
        j = j + 1
        GPIO.output(StepPin, GPIO.HIGH)
        time.sleep(pause)
        GPIO.output(StepPin, GPIO.LOW)
        time.sleep(pause)
'''
