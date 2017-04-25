import serial
import time

def main():
    ser = serial.Serial('/dev/ttyACM0', 9600)
    time.sleep(2)
    t0 = time.time()

    while time.time() - t0 < 5:
        # シリアル通信でデータを受信
        str = ser.read(4)
        # 読み込んだデータの表示
        print(str.decode())
        #print str #python2系の場合

if __name__ == '__main__':
    main()
