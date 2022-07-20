import RPi.GPIO as GPIO
import time

input_on = 23	#yellow
input_off = 24	#red
led = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(input_on, GPIO.IN)
GPIO.setup(input_off, GPIO.IN)
GPIO.setup(led, GPIO.OUT)

try :
	while True :
		if GPIO.input(input_on) == True :
			GPIO.output(led, True)
			time.sleep(0.2)
		elif GPIO.input(input_off) == True :
			GPIO.output(led, False)
			time.sleep(0.2)

except KeyboardInterrupt :
	GPIO.cleanup()
