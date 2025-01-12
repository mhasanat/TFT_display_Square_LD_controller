import spidev
from time import sleep

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 500000

def send_command(command):
    spi.xfer2([0x00, command])
    print(f"Sent Command: 0x{command:02X}")

def send_data(data):
    spi.xfer2([0x01, data])
    print(f"Sent Data: 0x{data:02X}")

def initialize_display():
    send_command(0xFF)  # Enter extended command set
    send_data(0x77)
    send_data(0x01)
    send_data(0x00)
    send_data(0x00)
    send_data(0x13)

    send_command(0x11)  # Exit sleep mode
    sleep(0.12)         # Wait 120ms

    send_command(0x29)  # Display ON
    sleep(0.02)         # Wait 20ms
    print("Display initialized.")

try:
    initialize_display()
finally:
    spi.close()
    print("SPI closed.")
