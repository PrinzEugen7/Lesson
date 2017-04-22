#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import sys
import thread

def calc_distance(TRIG, ECHO, num, v=17000):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
    GPIO.setwarnings(False)
    while(num):

        GPIO.output(TRIG, GPIO.LOW)
        time.sleep(0.3)
        
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO) == 0:
          t_start = time.time()
        
        while GPIO.input(ECHO) == 1:
          t_end = time.time()

        time = t_end - t_start
        distance = v * time
        print(distance, "cm")
    GPIO.cleanup()
        
def main():
    calc_distance(14, 15, 10)

        
if __name__ == "__main__":
    main()
