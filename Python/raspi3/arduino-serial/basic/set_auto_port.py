# -*- coding: utf-8 -*-
import serial
import serial.tools.list_ports

def main():
    ser = serial.Serial(list(serial.tools.list_ports.comports())[0][0], 9600, timeout=1)
    while True:
        flag = input()
        ser.write(flag.encode())
        # ser.write(flag) # python2
        if(flag == 'a'): # aが入力されたら通信終了
            break;
    ser.close()

if __name__ == '__main__':
    main()
