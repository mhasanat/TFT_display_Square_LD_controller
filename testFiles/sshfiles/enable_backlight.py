import RPi.GPIO as GPIO

# Configure GPIO pin for backlight control
BACKLIGHT_PIN = 3  # GPIO3 (BCM numbering)

try:
    # Set up GPIO mode
    GPIO.setmode(GPIO.BCM)

    # Set GPIO3 as an output pin
    GPIO.setup(BACKLIGHT_PIN, GPIO.OUT)

    # Turn on the backlight
    print("Turning ON backlight")
    GPIO.output(BACKLIGHT_PIN, GPIO.HIGH)

finally:
    # Do not clean up GPIO here to keep the pin state
    pass
