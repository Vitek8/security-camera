import io
import requests
from picamera import PiCamera
import RPi.GPIO as GPIO
import pigpio
import time
import os
import datetime
import picamera

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


def write(text):
    text = text.split(" ")
    ver = text[1]
    hor = text[3]
    step = text[5]
    ver = "ver " + ver
    hor = "hor " + hor
    step = "step " + step
    with open("data.txt", "w") as file:
        file.write(ver + "\n" + hor + "\n" + step)


def servo(direction, val):
    if direction == 'ver':
        servo_move(val, 27)

    if direction == 'hor':
        servo_move(val, 17)

#vertical_pin = 11
#horizontal_pin = 13
def servo_move(angle, pin):
    file = open("pos.txt", "r")
    pos = file.read()
    pos = int(pos)
    file.close()
    if (pos == 0):
        os.system("sudo pigpiod")
    fr = angle * 11 + 500
    pwm = pigpio.pi() 
    pwm.set_mode(pin, pigpio.OUTPUT)
    pwm.set_PWM_frequency(pin, 50 )
    #print("Úhel serva je: {}°".format(angle))
    #print("Pwm je: {}".format(fr))
    pwm.set_servo_pulsewidth(pin, fr) ;
    time.sleep(0.4)
    file = open("pos.txt", "r")
    pos = file.read()
    pos = int(pos)
    file.close()
    file = open("pos.txt", "w")
    pos = pos + 1
    pos = str(pos)
    file.write(pos)
    file.close()
    file = open("pos.txt", "r")
    pos = file.read()
    file.close()
    #print(pos)
    pos = int(pos)
    l = pos % 15
    pwm.set_PWM_dutycycle(pin, 0)
    pwm.set_PWM_frequency(pin, 0 )
    if pos != 0:
        if l == 0:
            os.system("sudo killall pigpiod")
            os.system("sudo pigpiod")
            os.system("sudo pigpiod")
            with open("pos.txt", "w") as file:
                file.write("0")


def read():
    with open("data.txt", 'r') as file:
        lines = file.readlines()
        for row in lines:
            attribute = row.split()
            if attribute[0] == 'ver':
                ver = int(attribute[1])
            if attribute[0] == 'hor':
                hor = int(attribute[1])
            if attribute[0] == 'step':
                step = int(attribute[1])
        return ver, hor, step


def speech(url2):
    url2 = url2.replace("<", "")
    url2 = url2.replace(">", "")
    url = 'https://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&q='
    url3 = '&tl=cs&total=1&idx=0&textlen='
    url = url + url2 + url3
    response = requests.get(url)

    with open("/home/pi/Desktop/Security camera/speech.mp3", "wb") as f:
        f.write(response.content)
        
        
def check():
    date = datetime.datetime.now()
    month = date.strftime("%b")
    months_en = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    months_cz = ["Leden", "Únor", "Březen", "Duben", "Květen", "Červen", "Červenec", "Srpen", "Září", "Říjen", "Listopad", "Prosinec"]

    if month == months_en[0]:
        cz_month = months_cz[0]
        if os.path.isdir(cz_month):
            record(cz_month)
        else:
            os.mkdir(cz_month)
            record(cz_month)

    elif month == months_en[1]:
        cz_month = months_cz[1]
        if os.path.isdir(cz_month):
            record(cz_month)
        else:
            os.mkdir(cz_month)
            record(cz_month)

    elif month == months_en[2]:
        cz_month = months_cz[2]
        if os.path.isdir(cz_month):
            record(cz_month)
        else:
            os.mkdir(months_cz)
            record(cz_month)

    elif month == months_en[3]:
        cz_month = months_cz[3]
        if os.path.isdir(cz_month):
            record(cz_month)
        else:
            os.mkdir(cz_month)
            record(cz_month)

    elif month == months_en[4]:
        cz_month = months_cz[4]
        if os.path.isdir(cz_month):
            record(cz_month)
        else:
            os.mkdir(cz_month)
            record(cz_month)

    elif month == months_en[5]:
        cz_month = months_cz[5]
        if os.path.isdir(cz_month):
            record(cz_month)
        else:
            os.mkdir(cz_month)
            record(cz_month)

    elif month == months_en[6]:
        cz_month = months_cz[6]
        if os.path.isdir(cz_month):
            record(cz_month)
        else:
            os.mkdir(cz_month)
            record(cz_month)

    elif month == months_en[7]:
        cz_month = months_cz[7]
        if os.path.isdir(cz_month):
            record(cz_month)
        else:
            os.mkdir(cz_month)
            record(cz_month)

    elif month == months_en[8]:
        cz_month = months_cz[8]
        if os.path.isdir(cz_month):
            record(cz_month)
        else:
            os.mkdir(cz_month)
            record(cz_month)

    elif month == months_en[9]:
        cz_month = months_cz[9]
        if os.path.isdir(cz_month):
            record(cz_month)
        else:
            os.mkdir(cz_month)
            record(cz_month)

    elif month == months_en[10]:
        cz_month = months_cz[10]
        if os.path.isdir(cz_month):
            record(cz_month)
        else:
            os.mkdir(cz_month)
            record(cz_month)

    elif month == months_en[11]:
        cz_month = months_cz[11]
        if os.path.isdir(cz_month):
            record(cz_month)
        else:
            os.mkdir(cz_month)
            record(cz_month)


def record(month):
    if sensor() == 1:
        date = datetime.datetime.now()
        name = date.strftime("%c")
        name = name + ".h264"
        name = name.replace(" ", "_")
        print(name)
        camera = picamera.PiCamera()
        camera.rotation = -180
        # camera.start_preview()
        camera.start_recording(month + "/" + name)
        time.sleep(20)
        print("Done")
        camera.stop_recording()
        #camera.stop_preview()




def sensor():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(18, GPIO.IN)
    while 1:
        i = GPIO.input(18)
        
        if i == 0:
            return 0

        elif i == 1:
            return 1
