import RPi.GPIO as GPIO
from time import sleep
import time




def SetAngle(angle):
    pin = 1
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    pwm = GPIO.PWM(pin, 50)
    pwm.start(100)
    duty = angle / 16.8 + 2
    GPIO.output(pin, True)
    pwm.ChangeDutyCycle(duty)
    sleep(0.5)
    GPIO.output(pin, False)
    pwm.ChangeDutyCycle(0)
    pwm.stop()
    GPIO.cleanup()


pos = input("zadej hodnotu mezi 0 a 180: ")
pos = float(pos)
neco = pos
neco = float(neco)
SetAngle(pos)
while 1:
    pos = input("zadej hodnotu mezi 0 a 180: ")
    pos = float(pos)
    if neco != pos:
        SetAngle(pos)
        neco = pos
    elif pos == 999:
        print("rotace")
        for i in range(0, 180):
            SetAngle(i)
    else:
        print("beze zmeny")






