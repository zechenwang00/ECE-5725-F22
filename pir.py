import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def motion(channel):
	print("motion detected")
	
GPIO.add_event_detect(17, GPIO.RISING, callback=motion)

while True:
	try:
		pass
	except KeyboardInterrupt:
		GPIO.cleanup()




