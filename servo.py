import RPi.GPIO as GPIO
from time import sleep
import time

def SetAngle(angle):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(32, GPIO.OUT)
    pwm=GPIO.PWM(32, 50)
    pwm.start(0)
    duty = angle / 18 + 2
    GPIO.output(32, True)
    pwm.ChangeDutyCycle(duty)
    sleep(2)
    GPIO.output(32, False)
    pwm.ChangeDutyCycle(0)
    pwm.stop()
    GPIO.cleanup()





