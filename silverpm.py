#!/usr/bin/python

""" silverpm

Control a Gembird silvershield power manager device ("Advanced surge 
protector"). Allows setting and getting the status of each outlet 
relay.

usage: silverpm [options]

options:
-t <outlet>     Toggle outlet
-f <outlet>     Disable outlet
-o <outlet>     Enable outlet
-p <outlet>     Read power status of outlet
-r <outlet>     Read relay status of outlet

where <outlet> is between 1 and 4.

"""
import usb.core
import usb.util
import getopt
import sys

VENDORID = 0x04B4
PRODUCT_ID_SISPM = 0xFD11
PRODUCT_ID_MSISPM_OLD = 0xFD10
PRODUCT_ID_MSISPM_FLASH = 0xFD12
PRODUCT_ID_SISPM_FLASH_NEW = 0xFD13

class power_manager(object):
	def __init__(self, vendor_id = VENDORID, product_id = PRODUCT_ID_SISPM_FLASH_NEW):
		self.dev = usb.core.find(idVendor=vendor_id, idProduct=product_id)

		if self.dev is None:
			raise Exception("No power manager found")

	def get_serial(self):
		return self.dev.ctrl_transfer(0xa1, 0x01, (0x03 << 8) | 1, 0, 6)

	def __usb_write(self, b1, b2):
		buffer = [b1, b2, 0, 0, 0]
		return self.dev.ctrl_transfer(0x21, 0x09, (0x03 << 8) | b1, 0, buffer)

	def __usb_read(self, b1, b2):
		return self.dev.ctrl_transfer(0x21 | usb.util.CTRL_IN, 0x01, (0x03 << 8) | b1, 0, 6 )

	def enable_outlet(self, outlet):
		self.__usb_write(3*outlet, 0x03)

	def disable_outlet(self, outlet):
		self.__usb_write(3*outlet, 0x00)

	def outlet_status(self, outlet):
		response = self.__usb_read(3*outlet, 0x03)
	
		relay = bool(response[1] & (1 << 0))
		power = bool(response[1] & (1 << 1))
		return (relay, power)  

	def __str__(self):
		serial = self.get_serial()
		return "%02X:%02X:%02X:%02X:%02X" % (serial[0], serial[1], 
											 serial[2], serial[3], 
											 serial[4])

if __name__ == "__main__":
	try:
		opts, args = getopt.getopt(sys.argv[1:], 't:f:o:p:r:')
	except getopt.error:
		print(__doc__)
		sys.exit(2)

	p = power_manager()
	print("Using device %s" % p)
			
	for o, a in opts:
		outlet = int(a)
		if (outlet < 1 or outlet > 4):
			print("Invalid outlet (%d)" % outlet)
			sys.exit(1)
			
		if o == '-t':
			(is_on, _) = p.outlet_status(outlet)
			if is_on:
				p.disable_outlet(outlet)
			else:
				p.enable_outlet(outlet)
		elif o == '-f':
			p.disable_outlet(outlet) 
		elif o == '-o':
			p.enable_outlet(outlet)
		elif o == '-p':
			(_, is_powered) = p.outlet_status(outlet)
			print(is_powered)
		elif o == '-r':
			(is_on, _) = p.outlet_status(outlet)
			print(is_on)
