import RPi.GPIO as GPIO

# Configure GPIO pin for backlight control
BACKLIGHT_PIN = 3  # GPIO3 (BCM numbering)

try:
    # Set up GPIO mode
    GPIO.setmode(GPIO.BCM)

    # Set GPIO3 as an output pin
    GPIO.setup(BACKLIGHT_PIN, GPIO.OUT)

    # Turn off the backlight
    print("Turning OFF backlight")
    GPIO.output(BACKLIGHT_PIN, GPIO.LOW)

finally:
    # Clean up GPIO to release the pin
    GPIO.cleanup()
    print("GPIO cleaned up.")
