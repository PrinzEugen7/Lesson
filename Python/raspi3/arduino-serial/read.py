import serial
import time

def main():
    ser = serial.Serial('/dev/ttyACM0', 9600)
    time.sleep(2)
    t0 = time.time()

    while time.time() - t0 > 5:
        # シリアル通信でデータを受信
        str = con.read(30)
        print(str)

if __name__ == '__main__':
    main()
