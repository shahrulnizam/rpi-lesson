import RPi.GPIO as GPIO
from time import sleep

LED1 = 21

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED,GPIO.OUT)

try:
    while 1:
        print("HIGH")
        GPIO.output(LED,GPIO.HIGH)
        sleep(1)
        print("LOW")
        GPIO.output(LED,GPIO.LOW)
        sleep(1)
finally:
    GPIO.output(LED,GPIO.LOW)
