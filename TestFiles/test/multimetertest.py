import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.OUT)  # Use GPIO3
GPIO.output(3, GPIO.HIGH)
input("GPIO3 is HIGH. Press Enter to exit...")
GPIO.cleanup()
