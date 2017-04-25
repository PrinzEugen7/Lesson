# -*- coding: utf-8 -*-
import serial

def main():

    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    while True:
        flag = input()
        flag = flag + "\0"
        ser.write(flag.encode())
        # python2 ver
        #flag = raw_input()
        #ser.write(flag+"\n")
        if(flag == 'q'): # qが入力されたら通信終了
            break;
    ser.close()

if __name__ == '__main__':
    main()
