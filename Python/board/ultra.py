import RPi.GPIO as GPIO
import time

def measure() :
	GPIO.output(triggerPin, True)
	time.sleep(0.0001)	#10us
	GPIO.output(triggerPin, False)
	start = time.time()	#현재시간 저장

	while GPIO.input(echoPin) == False :
		start = time.time()
	while GPIO.input(echoPin) == True :
		stop = time.time()

	dlapsed = stop - start
	distance = (dlapsed * 19000) / 2

	return distance

triggerPin = 20
echoPin = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(triggerPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)

try :
	while True :
		distance = measure()
		print("Distance : %.2f cm" % distance)
		time.sleep(1)

except KeyboardInterrupt :
	GPIO.cleanup()
