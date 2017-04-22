#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

def main():
    TRIG = 14
    ECHO = 15
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)    
    while(1):

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
        c = sys.stdin.read(1)
        if c == 's':
            # GPIOピンの設定解除        
            GPIO.cleanup()   
            break
        
if __name__ == "__main__":
    main()
