import spidev
import RPi.GPIO as GPIO
import time

# GPIO and SPI setup
RESET_PIN = 27  # GPIO27 (Pin 13)
SCS_PIN = 8     # GPIO8 (Pin 24) - Optional if SPI manages Chip Select automatically

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(RESET_PIN, GPIO.OUT)

# Initialize SPI
spi = spidev.SpiDev()
spi.open(0, 0)  # SPI bus 0, device 0 (CE0)
spi.max_speed_hz = 500000  # Lower SPI speed if necessary

# Reset sequence
def reset_display():
    GPIO.output(RESET_PIN, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(RESET_PIN, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(RESET_PIN, GPIO.HIGH)
    time.sleep(0.1)

# SPI functions
def send_command(command):
    """Send a command to the display."""
    spi.xfer2([0x00, command])  # Prefix 0x00 indicates a command

def send_data(data):
    """Send data to the display."""
    spi.xfer2([0x01, data])  # Prefix 0x01 indicates data

# Initialization sequence
def initialize_display():
    """Initialize the display with commands and data."""
    send_command(0xFF)
    send_data(0x77)
    send_data(0x01)
    send_data(0x00)
    send_data(0x00)
    send_data(0x13)
    send_command(0xEF)
    send_data(0x08)
    send_command(0xFF)
    send_data(0x77)
    send_data(0x01)
    send_data(0x00)
    send_data(0x00)
    send_data(0x10)
    # Add additional commands and data from the initialization sequence as needed

try:
    print("Resetting display...")
    reset_display()
    print("Initializing display...")
    initialize_display()
    print("Initialization complete!")
finally:
    spi.close()
    GPIO.cleanup()
