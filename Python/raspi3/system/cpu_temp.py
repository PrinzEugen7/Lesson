#!/usr/bin/python
# -*- coding: utf-8 -*-

def get_temp():
    f = open("/sys/class/thermal/thermal_zone0/temp","r")
    tmp = 0
    for t in f:
        tmp = t[:2]+"."+t[2:5]
    f.close()
    return float(tmp)

if __name__=='__main__':
    temp = get_temp()
    print(str(temp))
