import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
#GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(15,GPIO.IN)
test_input = GPIO.input(15)
print(test_input)

