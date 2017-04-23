#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

def calc_distance(TRIG_PIN, ECHO_PIN, num, v=34000):
    # ピン番号をGPIOで指定
    GPIO.setmode(GPIO.BCM)
    # TRIG_PINを出力, ECHO_PINを入力
    GPIO.setup(TRIG_PIN,GPIO.OUT)
    GPIO.setup(ECHO_PIN,GPIO.IN)
    GPIO.setwarnings(False)
    
    for i in range(num):
        # TRIGピンを0.3[s]だけLOW
        GPIO.output(TRIG_PIN, GPIO.LOW)
        time.sleep(0.3)
        # TRIGピンを0.00001[s]だけ出力(超音波発射)        
        GPIO.output(TRIG_PIN, True)
        time.sleep(0.00001)
        GPIO.output(TRIG_PIN, False)
        # ECHO_PINがHIGHである時間を計測
        while GPIO.input(ECHO_PIN) == 0:
            t_start = time.time()
        
        while GPIO.input(ECHO_PIN) == 1:
            t_end = time.time()

        t = t_end - t_start
        # 距離[cm] = 音速[cm/s] * 時間[s]/2
        distance = v * t/2
        print(distance, "cm")
    # ピン設定解除
    GPIO.cleanup()
        
def main():
    # 距離計測(TRIGピン番号, ECHO_PIN番号, 計測回数, 音速[cm/s])
    calc_distance(14, 15, 10, 34000)

        
if __name__ == "__main__":
    main()
