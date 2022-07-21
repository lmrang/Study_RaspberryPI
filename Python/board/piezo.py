import RPi.GPIO as GPIO
import time

piezoPin = 13
#멜로디 리스트
melody = [130, 146, 164, 174, 195, 220, 246, 261]

GPIO.setmode(GPIO.BCM)
GPIO.setup(piezoPin, GPIO.OUT)
#PWM 설정
Buzz = GPIO.PWM(piezoPin, 440)

try :
	while True :
		Buzz.start(50) #PWM 시작(duty = 50)
		for i in range(0, len(melody)) :
			Buzz.ChangeFrequency(melody[i])
			time.sleep(0.3)
		Buzz.stop()
		time.sleep(1)

except KeyboardInterrupt :
	GPIO.cleanup()
