import spidev

spi = spidev.SpiDev()
spi.open(0, 0)  # SPI bus 0, device 0 (CE0)
spi.max_speed_hz = 1000000  # Set SPI speed to 1 MHz

try:
    response = spi.xfer2([0xAA])  # Send 0xAA
    print("Response:", response)
finally:
    spi.close()