import RPi.GPIO as GPIO
import time

def measure() :
	GPIO.output(triggerPin, True)
	time.sleep(0.0001)
	GPIO.output(triggerPin, False)
	start = time.time()

	while GPIO.input(echoPin) == False :
		start = time.time()
	while GPIO.input(echoPin) == True :
		stop = time.time()

	elapsed = stop - start
	distance = (elapsed * 19000)/2

	return distance

def Melody(a) :
	Buzz.start(90)
	Buzz.ChangeFrequency(melody[7])
	time.sleep(0.2)
	Buzz.stop()
	time.sleep(a)

triggerPin = 20
echoPin = 21
piezo = 16

melody = [130, 146, 164, 174, 195, 220, 246, 261]

GPIO.setmode(GPIO.BCM)
GPIO.setup(triggerPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)
GPIO.setup(piezo, GPIO.OUT)

Buzz = GPIO.PWM(piezo, 440)

try :
	while True :
		distance = measure()
		print("%.2f cm" %distance)

		if distance < 5 :
			Melody(0.05)
		elif distance < 10 :
			Melody(0.15)
		elif distance < 18 :
			Melody(0.3)
		else :
			Melody(0.5)

except KeyboardInterrupt :
	GPIO.cleanup()
