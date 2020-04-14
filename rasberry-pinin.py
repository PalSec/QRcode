import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)



GPIO.add_event_detect(4, GPIO.RISING)
def my_callback():
    print ("PUSHED!")
GPIO.add_event_callback(4, my_callback)