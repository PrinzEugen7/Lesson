# -*- coding: utf-8 -*-
import serial

def main():
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    while True:
        flag = raw_input()
        ser.write(flag)
        if(flag == 'a'): # aが入力されたら通信終了
            break;
    ser.close()

if __name__ == '__main__':
    main()
