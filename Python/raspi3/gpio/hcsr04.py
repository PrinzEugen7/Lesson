#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

def main():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    TRIG = 14
    ECHO = 15
    
    while(1):
        GPIO.setup(TRIG,GPIO.OUT)
        GPIO.setup(ECHO,GPIO.IN)
        GPIO.output(TRIG, GPIO.LOW)
        time.sleep(0.3)
        
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO) == 0:
          signaloff = time.time()
        
        while GPIO.input(ECHO) == 1:
          signalon = time.time()

        timepassed = signalon - signaloff
        distance = timepassed * 17000
        print(distance, "cm")

        
if __name__ == "__main__":
    main()
