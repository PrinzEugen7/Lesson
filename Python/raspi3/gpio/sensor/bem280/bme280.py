#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import smbus

#ALTITUDE= 600


class BME280:
	DEVICE_ADDRESS = 0x76
	BUS_CHANNEL = 1

	def __init__(self,address = DEVICE_ADDRESS,channel = BUS_CHANNEL):
		self.address = address
		self.channel = channel
		self.bus = smbus.SMBus(self.channel)
		self.t_fine = 0
        
		data = self.bus.read_byte_data(self.address,0xD0)
		self.bus.write_byte_data(self.address,0xF2,0x01)
		self.bus.write_byte_data(self.address,0xF4,0x27)
		self.bus.write_byte_data(self.address,0xF5,0xA0)
		data = self.bus.read_i2c_block_data(self.address,0x88,6)
		self.dig_T1 = (data[1] << 8) | data[0]
		self.dig_T2 = (data[3] << 8) | data[2]
		self.dig_T3 = (data[5] << 8) | data[4]
		data = self.bus.read_i2c_block_data(self.address,0x8E,18)
		self.dig_P1 = (data[ 1] << 8) | data[ 0]
		self.dig_P2 = (data[ 3] << 8) | data[ 2]
		self.dig_P3 = (data[ 5] << 8) | data[ 4]
		self.dig_P4 = (data[ 7] << 8) | data[ 6]
		self.dig_P5 = (data[ 9] << 8) | data[ 8]
		self.dig_P6 = (data[11] << 8) | data[10]
		self.dig_P7 = (data[13] << 8) | data[12]
		self.dig_P8 = (data[15] << 8) | data[14]
		self.dig_P9 = (data[17] << 8) | data[16]
		data[0] = self.bus.read_byte_data(self.address,0xA1)
		self.dig_H1 = data[0]
		data = self.bus.read_i2c_block_data(self.address,0xE1,7)
		self.dig_H2 = (data[1] << 8) | data[0]
		self.dig_H3 = data[2]
		self.dig_H4 = (data[3] << 4) | (data[4] & 0x0f)
		self.dig_H5 = (data[5] << 4) | ((data[4]>>4) & 0x0f)
		self.dig_H6 = data[6]


	def getTemperature(self):
		temp_xlsb = self.bus.read_byte_data(self.address,0xFC)
		temp_lsb = self.bus.read_byte_data(self.address,0xFB)
		temp_msb = self.bus.read_byte_data(self.address,0xFA)
		temp_raw = (temp_msb << 12) | (temp_lsb << 4) | (temp_xlsb >> 4)
		temp_data = (((((temp_raw >> 3) - (self.dig_T1 << 1))) * self.dig_T2) >> 11) +\
			 ((((((temp_raw >> 4) - self.dig_T1) * ((temp_raw >> 4) - self.dig_T1)) >> 12) * self.dig_T3) >> 14)
		self.t_fine = temp_data
		temp_data = (temp_data * 5 + 128) >> 8
		return temp_data / 100.0


	def getPressure(self):
		    data = self.bus.read_i2c_block_data(self.address,0xF7,3)
		    press_raw = (data[0] << 12) | (data[1] << 4) | (data[2] >> 4)

		    v1 = (self.t_fine / 2.0) - 64000.0
                    v2 = (((v1 / 4.0) * (v1 / 4.0)) / 2048) * dig_P6
                    v2 = v2 + ((v1 * dig_P5) * 2.0)
                    v2 = (v2 / 4.0) + (dig_P4 * 65536.0)
                    v1 = (((dig_P3 * (((v1 / 4.0) * (v1 / 4.0)) / 8192)) / 8)  + ((dig_P2 * v1) / 2.0)) / 262144
                    v1 = ((32768 + v1) * dig_P1) / 32768
     
                    if v1 == 0: return 0
                    press = ((1048576 - press_raw) - (v2 / 4096)) * 3125
                    if press < 0x80000000: press = (press * 2.0) / v1
                    else: press = (pressure / v1) * 2
                    v1 = (dig_P9 * (((press / 8.0) * (press / 8.0)) / 8192.0)) / 4096
                    v2 = ((press / 4.0) * dig_P8) / 8192.0
                    press = press + ((v1 + v2 + dig_P7) / 16.0)  
                    return press/100

	
	def getHumidity(self):
		data = self.bus.read_i2c_block_data(self.address,0xFD,2)

		hum_raw = (data[0] << 8) | data[1]

		v_x1 = self.t_fine - 76800
		v_x1 =  (((((hum_raw << 14) -((self.dig_H4) << 20) - ((self.dig_H5) * v_x1)) +\
			(16384)) >> 15) * (((((((v_x1 * self.dig_H6) >> 10) *\
			(((v_x1 * (self.dig_H3)) >> 11) + 32768)) >> 10) + 2097152) *\
			self.dig_H2 + 8192) >> 14))
		v_x1 = (v_x1 - (((((v_x1 >> 15) * (v_x1 >> 15)) >> 7) * self.dig_H1) >> 4))
		if v_x1 < 0:
			v_x1 = 0
		if v_x1 > 419430400:
			v_x1 = 419430400
		
		hum = (v_x1 >> 12)
		
		return (hum/1024.0)

bme280 = BME280()
temp = round(bme280.getTemperature(),1)
humid = round(bme280.getHumidity(),1)
press = round(bme280.getPressure(),1)
print("気温：", temp + "[C]")
print("湿度：", humid + "[%]")
print("気圧:", press + "[hPa]")
