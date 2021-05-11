from time import sleep
from gpiozero import DistanceSensor
import RPi.GPIO as GPIO
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)
#led on PWM pin 21 @200hz (no flickering)
led = GPIO.PWM(21,200)
#ensure LED is turned off
led.start(0)

dist_sensor = DistanceSensor(echo=24, trigger=18, max_distance=4)


while True:
	try:
		dist = dist_sensor.distance	
		#set brightness level, the closer an object the higher
		#the brightness level	
		brightness = 100 - 25*(dist)
		int(brightness)
		print("Distance sensor read %.1f cm" % (dist_sensor.distance * 100))
		print('brightness ',brightness)
		led.ChangeDutyCycle(brightness)
		#sleep(1)

	except KeyboardInterrupt:
		print("exit")
		sys.exit()
		GPIO.cleanup()



