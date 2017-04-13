#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

def main():
        GPIO.setmode(GPIO.BCM)          # GPIO番号で指定
        GPIO.setup(25, GPIO.OUT)        # GPIO25を出力用に設定
        GPIO.output(25, GPIO.HIGH)      # 点灯
        time.sleep(2)                       # 2秒待機
        GPIO.output(25, GPIO.LOW)       # 消灯
        time.sleep(2)               # 2秒待機
        GPIO.output(25, GPIO.HIGH)      # 点灯
        time.sleep(2)                       # 2秒待機
        GPIO.output(25, GPIO.LOW)       # 消灯
        time.sleep(2)                       # 2秒待機
        GPIO.cleanup()                      # GPIOピンの設定解除

if __name__ == "__main__":
    main()
