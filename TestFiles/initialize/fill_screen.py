import spidev
from time import sleep

# Initialize SPI
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 500000

# Send a command to the LT7680
def send_command(command):
    spi.xfer2([0x00, command])
    print(f"Sent Command: 0x{command:02X}")

# Send data to the LT7680
def send_data(data):
    spi.xfer2([0x01, data])
    print(f"Sent Data: 0x{data:02X}")

# Initialize the display
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

# Fill the screen with a single color
def fill_screen(color):
    send_command(0x2C)  # Memory Write command
    for _ in range(320 * 240):  # Assuming 320x240 resolution
        send_data(color)  # Fill with the specified color
    print(f"Screen filled with color: 0x{color:02X}")

# Main logic
try:
    initialize_display()
    fill_screen(0xFF)  # Example: Fill the screen with white
finally:
    spi.close()
    print("SPI closed.")
