import spidev
import RPi.GPIO as GPIO
import time

# GPIO setup for chip select (SCS#)
SCS_PIN = 8  # GPIO8 (Pin 24)
GPIO.setmode(GPIO.BCM)
GPIO.setup(SCS_PIN, GPIO.OUT)
GPIO.output(SCS_PIN, GPIO.HIGH)  # Set SCS# high initially (inactive)

# Initialize SPI
spi = spidev.SpiDev()
spi.open(0, 0)  # SPI bus 0, device 0
spi.max_speed_hz = 1000000  # 1 MHz SPI clock speed (adjust as needed)

# Function to send SPI commands
def send_command(cmd):
    GPIO.output(SCS_PIN, GPIO.LOW)  # Activate chip select
    spi.xfer2([cmd])  # Send command
    GPIO.output(SCS_PIN, GPIO.HIGH)  # Deactivate chip select

# Example initialization sequence
try:
    print("Initializing LT7680...")
    send_command(0x01)  # Reset command
    time.sleep(0.1)     # Small delay
    send_command(0x11)  # Sleep out command
    time.sleep(0.1)     # Small delay
    send_command(0x29)  # Display ON command
    print("LT7680 initialized!")
finally:
    spi.close()
    GPIO.cleanup()
