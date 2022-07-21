import RPi.GPIO as GPIO
import time

piezoPin = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(piezoPin, GPIO.OUT)

Buzz = GPIO.PWM(piezoPin, 440)

melody = [130, 146, 164, 174, 195, 220, 246, 261]

def Melody(a) :
	Buzz.start(90)
	Buzz.ChangeFrequency(melody[a])
	time.sleep(0.3)
	Buzz.stop()

try :
	while True :
		key = int(input())
#		Buzz.start(90)

		for i in range(0, len(melody)) :
			if key == i :
				Melody(i)
			else :
				pass

except KeyboardInterrupt :
	GPIO.cleanup()
