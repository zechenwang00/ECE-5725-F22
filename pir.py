import RPi.GPIO as GPIO
import config
import requests
import datetime

# GPIO setup
PIR_1 = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_1, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# callbacks
def motion(channel):
	message = 'motion detected'
	curr_time = datetime.datetime.now().strftime("%H:%M:%S %d/%m/%Y")
	# resp = requests.post('https://textbelt.com/text', {
	# 	'phone': config.PHONE,
	# 	'message': message + " at " + curr_time,
	# 	'key': config.KEY,
	# })
	# debug uses
	print(message + " at " + curr_time)
	# print(resp.json())
	
GPIO.add_event_detect(PIR_1, GPIO.RISING, callback=motion)

while True:
	try:
		pass
	except KeyboardInterrupt:
		GPIO.cleanup()




