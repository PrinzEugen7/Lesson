#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import time
import csv
import ftplib
import RPi.GPIO as GPIO

class Bme280():
  def __init__(self, i2c_address= 0x76, bus_number=1):
    import smbus
    self.digT = []
    self.digP = []
    self.digH = []
    self.t_fine = 0
    self.bus_number = bus_number
    self.bus = smbus.SMBus(self.bus_number)
    self.i2c_address = i2c_address
    self.setup()
    self.get_calib_param()
    self.data = []
    for i in range (0xF7, 0xF7+8):
        self.data.append(self.bus.read_byte_data(self.i2c_address,i))
    self.press_raw = (self.data[0] << 12) | (self.data[1] << 4) | (self.data[2] >> 4)
    self.temp_raw = (self.data[3] << 12) | (self.data[4] << 4) | (self.data[5] >> 4)
    self.humid_raw  = (self.data[6] << 8)  |  self.data[7]
    
  def get_calib_param(self):
    calib = []
     
    for i in range (0x88,0x88+24):
        calib.append(self.bus.read_byte_data(self.i2c_address,i))
    calib.append(self.bus.read_byte_data(self.i2c_address,0xA1))
    for i in range (0xE1,0xE1+7):
         calib.append(self.bus.read_byte_data(self.i2c_address,i))

    self.digT.append((calib[1] << 8) | calib[0])
    self.digT.append((calib[3] << 8) | calib[2])
    self.digT.append((calib[5] << 8) | calib[4])
    self.digP.append((calib[7] << 8) | calib[6])
    self.digP.append((calib[9] << 8) | calib[8])
    self.digP.append((calib[11]<< 8) | calib[10])
    self.digP.append((calib[13]<< 8) | calib[12])
    self.digP.append((calib[15]<< 8) | calib[14])
    self.digP.append((calib[17]<< 8) | calib[16])
    self.digP.append((calib[19]<< 8) | calib[18])
    self.digP.append((calib[21]<< 8) | calib[20])
    self.digP.append((calib[23]<< 8) | calib[22])
    self.digH.append( calib[24] )
    self.digH.append((calib[26]<< 8) | calib[25])
    self.digH.append( calib[27] )
    self.digH.append((calib[28]<< 4) | (0x0F & calib[29]))
    self.digH.append((calib[30]<< 4) | ((calib[29] >> 4) & 0x0F))
    self.digH.append( calib[31] )

    for i in range(1,2):
         if self.digT[i] & 0x8000: self.digT[i] = (-self.digT[i] ^ 0xFFFF) + 1

    for i in range(1,8):
         if self.digP[i] & 0x8000: self.digP[i] = (-self.digP[i] ^ 0xFFFF) + 1

    for i in range(0,6):
        if self.digH[i] & 0x8000: self.digH[i] = (-self.digH[i] ^ 0xFFFF) + 1  

  def  get_data(self):
    temp = self.get_temp()
    pressure = self.get_pressure()
    humid = self.get_humid()
    return temp, humid, pressure
    
  def get_pressure(self):
    pressure = 0.0
    v1 = (self.t_fine / 2.0) - 64000.0
    v2 = (((v1 / 4.0) * (v1 / 4.0)) / 2048) * self.digP[5]
    v2 = v2 + ((v1 * self.digP[4]) * 2.0)
    v2 = (v2 / 4.0) + (self.digP[3] * 65536.0)
    v1 = (((self.digP[2] * (((v1 / 4.0) * (v1 / 4.0)) / 8192)) / 8)  + ((self.digP[1] * v1) / 2.0)) / 262144
    v1 = ((32768 + v1) * self.digP[0]) / 32768
     
    if v1 == 0: return 0
    pressure = ((1048576 - self.press_raw) - (v2 / 4096)) * 3125
    if pressure < 0x80000000: pressure = (pressure * 2.0) / v1
    else: pressure = (pressure / v1) * 2
    v1 = (self.digP[8] * (((pressure / 8.0) * (pressure / 8.0)) / 8192.0)) / 4096
    v2 = ((pressure / 4.0) * self.digP[7]) / 8192.0
    pressure = pressure + ((v1 + v2 + self.digP[6]) / 16.0)  
    return pressure/100

  def get_temp(self):
    v1 = (self.temp_raw/ 16384.0 - self.digT[0] / 1024.0) * self.digT[1]
    v2 = (self.temp_raw/ 131072.0 - self.digT[0] / 8192.0) * (self.temp_raw/ 131072.0 - self.digT[0] / 8192.0) * self.digT[2]
    self.t_fine = v1 + v2
    return self.t_fine / 5120.0

  def get_humid(self):
    var_h =   self.t_fine  - 76800.0
    if var_h != 0:
         var_h = (self.humid_raw - (self.digH[3] * 64.0 + self.digH[4]/16384.0 * var_h)) * (self.digH[1] / 65536.0 * (1.0 + self.digH[5] / 67108864.0 * var_h * (1.0 + self.digH[2] / 67108864.0 * var_h)))
    else:
         return 0
    var_h = var_h * (1.0 - self.digH[0] * var_h / 524288.0)
    if var_h > 100.0:
         var_h = 100.0
    elif var_h < 0.0:
         var_h = 0.0
         
    return var_h

  def setup(self):
    osrs_t = 1                #Temperature oversampling x 1
    osrs_p = 1                #Pressure oversampling x 1
    osrs_h = 1                #Humidity oversampling x 1
    mode   = 3                #Normal mode
    t_sb   = 5                #Tstandby 1000ms
    filter = 0                #Filter off
    spi3w_en = 0              #3-wire SPI Disable

    ctrl_meas_reg = (osrs_t << 5) | (osrs_p << 2) | mode
    config_reg    = (t_sb << 5) | (filter << 2) | spi3w_en
    ctrl_hum_reg  = osrs_h
    self.bus.write_byte_data(self.i2c_address, 0xF2, ctrl_hum_reg)
    self.bus.write_byte_data(self.i2c_address, 0xF4, ctrl_meas_reg)
    self.bus.write_byte_data(self.i2c_address, 0xF5, config_reg)

def read_csv(filename):
    f = open(filename, "r")
    csv_data = csv.reader(f)
    list = [ e for e in csv_data]
    f.close()
    return list
    
def update_list2d(list, data):
    for i in range(len(list)):
        if list[i][0]==data[0]: list[i] = data
    return list

def write_csv(filename, list):
   with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(list)   

   f.close()

def ftp_upload(filename, destination, host, user, password):
    # 接続先サーバーのホスト名
    ftp = ftplib.FTP(host)
    ftp.set_pasv("true")
    # ユーザ名とパスワードを指定しログイン
    ftp.login(user, password)
    # アップロードするファイル
    fp = open(filename, 'rb')
    # アップロード先のディレクトリ
    ftp.storbinary(destination,fp)
    # 終了処理
    ftp.close()
    fp.close()

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
    return t_end - t_start

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
    t = 0
    ts = 30 # サンプリング時間
    while(1):
        # LOW状態の時間tを求める
        dt = pulseIn(PIN, 0)
        if dt<1: t = t + dt
        
        if ((time.time() - t0) > ts):
            # LOWの割合[0-100%]
            ratio = (100*t)/ts
            # ほこりの濃度を算出
            concent = 1.1 * pow(ratio,3) - 3.8 * pow(ratio,2) + 520 * ratio + 0.62
            break
    return pcs2ugm3(concent)
 
filename = 'data.csv'
destination =  "STOR /sample/test.csv"
host = "xxx"
user = "xxx"
password = "xxx"
PIN = 14
# ピン番号をGPIOで指定
GPIO.setmode(GPIO.BCM)
# TRIG_PINを出力, ECHO_PINを入力
GPIO.setup(PIN,GPIO.IN)
GPIO.setwarnings(False)

while(1):
　　　　dt = datetime.datetime.now()
    if str(dt.minutes) == "0":
        bme280 = Bme280(0x76, 1)
        temp, humid, press = bme280.get_data()
        csv_data = read_csv(filename)
        date = dt.strftime('%Y-%m-%d %H:%M')
        pm25 = get_pm25(PIN)
        data = [date, temp, humid, press, pm25]
        csv_data2 = update_list2d(csv_data, data)
        write_csv(filename, csv_data2)
        ftp_upload(filename, destination, host, user, password)
        print(data)
        time.sleep(1)
    time.sleep(30)

# ピン設定解除
GPIO.cleanup()
