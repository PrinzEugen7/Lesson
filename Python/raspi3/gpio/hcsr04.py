#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

def pulseIn(pin, start):
    if start==1: end = 0
    else: end = 1
    while GPIO.input(ECHO_PIN) == end:
        t_start = time.time()
        
    while GPIO.input(ECHO_PIN) == start:
        t_end = time.time()

    return t_end - t_start

def calc_distance(TRIG_PIN, ECHO_PIN, num, v=17000):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRIG_PIN,GPIO.OUT)
    GPIO.setup(ECHO_PIN,GPIO.IN)
    GPIO.setwarnings(False)
    while(num):

        GPIO.output(TRIG_PIN, GPIO.LOW)
        time.sleep(0.3)
        
        GPIO.output(TRIG_PIN, True)
        time.sleep(0.00001)
        GPIO.output(TRIG_PIN, False)
        t = pulseIn(TRIG, 1)
        distance = v * t
        print(distance, "cm")
    GPIO.cleanup()
        
def main():
    calc_distance(14, 15, 10)

        
if __name__ == "__main__":
    main()
