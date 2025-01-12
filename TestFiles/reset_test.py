import RPi.GPIO as GPIO
import time

RESET_PIN = 27  # GPIO27 (Pin 13)

# Setup GPIO for RESET
GPIO.setmode(GPIO.BCM)
GPIO.setup(RESET_PIN, GPIO.OUT)

# Perform a reset
GPIO.output(RESET_PIN, GPIO.HIGH)
time.sleep(0.1)
GPIO.output(RESET_PIN, GPIO.LOW)
time.sleep(0.1)
GPIO.output(RESET_PIN, GPIO.HIGH)
