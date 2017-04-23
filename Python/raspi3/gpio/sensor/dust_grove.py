#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

# HIGH or LOWの時計測
def pulseIn(PIN, start=1, end=0):
    if start==0: end = 1
    t_start = 0
    t_end = 0
    # ECHO_PINがHIGHである時間を計測
    while GPIO.input(PIN) == end:
        t_start = time.time()
        
    while GPIO.input(PIN) == start:
        t_end = time.time()
    return int((t_end - t_start)*1000000)

# 単位をμg/m^3に変換
def pcs2ugm3 (pcs):
  pi = 3.14159
  # 全粒子密度(1.65E12μg/ m3)
  density = 1.65 * pow (10, 12)
  # PM2.5粒子の半径(0.44μm)
  r25 = 0.44 * pow (10, -6)
  vol25 = (4/3) * pi * pow (r25, 3)
  mass25 = density * vol25 # μg
  K = 3531.5 # per m^3 
  # μg/m^3に変換して返す
  return pcs * K * mass25

# pm2.5計測
def get_pm25(PIN):
    t0 = time.time()
    low_oc = 0
    ts = 30 # サンプリング時間
    while(1):
        # LOWの占有率
        low_oc = low_oc + pulseIn(PIN, 0)
        if ((time.time() - t0) > ts):
            # LOWの割合
            ratio = low_oc/(ts*1000*10.0)
            # ほこりの濃度を算出
            concent = 1.1 * pow(ratio,3) - 3.8 * pow(ratio,2) + 520 * ratio + 0.62
            print(ratio, " [%]")
            print(concent, " [pcs/0.01cf]")
            print(pcs2ugm3(concent), " [ug/m^3]")
            break

PIN = 15
# ピン番号をGPIOで指定
GPIO.setmode(GPIO.BCM)
# TRIG_PINを出力, ECHO_PINを入力
GPIO.setup(PIN,GPIO.IN)
GPIO.setwarnings(False)

for i in range(10):
    get_pm25(PIN)

# ピン設定解除
GPIO.cleanup()
