from bmp280 import BMP280
import dataxml

try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus

class Sensors:
    def __init__(self):
        bus = SMBus(1)
        self.bmp280 = BMP280(i2c_dev=bus)

    def new_mesure(self):
        temperature = self.bmp280.get_temperature()
        pressure = self.bmp280.get_pressure()
        altitude = self.bmp280.get_altitude()
        dataxml.new_mesure(temperature, pressure, altitude)
