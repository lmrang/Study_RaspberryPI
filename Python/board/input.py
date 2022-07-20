import RPi.GPIO as GPIO
import time

switchPin = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(switchPin, GPIO.IN)
count = 0

try:
	while True:
		if GPIO.input(switchPin) == True :
			count=count+1
			print(count)
			time.sleep(0.2)

except KeyboardInterrupt:
	GPIO.cleanup()
