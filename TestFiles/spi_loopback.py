import spidev

# Initialize SPI
spi = spidev.SpiDev()
spi.open(0, 0)  # Open SPI bus 0, device 0
spi.max_speed_hz = 500000

# Send a byte (e.g., 0xAA) and read the response
response = spi.xfer2([0xAA])
print(f"Response: {response}")

spi.close()
