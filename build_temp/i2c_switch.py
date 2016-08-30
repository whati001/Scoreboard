#!/usr/bin/python3

import sys
import smbus
import time

bus = smbus.SMBus(1)
print("I2C-Address in HEX: "+sys.argv[1])
adr = int(sys.argv[1])+12
print("I2C-Address in DEZ: "+str(adr))

bus.write_byte_data(adr,0x00,0x00)
while 1:
	bus.write_byte_data(adr,0x09,0x00)
	print("PORT is LOW!!!")
	time.sleep(1)
	bus.write_byte_data(adr,0x09,0xFF)
	print("PORT is HIGH!!!")
	time.sleep(1)


