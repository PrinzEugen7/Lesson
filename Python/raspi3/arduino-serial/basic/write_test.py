# -*- coding: utf-8 -*-
import serial

def main():
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    while True:
        flag =　input()
        ser.write(flag.encode())
        # ser.write(flag) # python2
        if(flag == 'a'): # aが入力されたら通信終了
            break;
    ser.close()

if __name__ == '__main__':
    main()
