import cv2
import io
import requests

vc = cv2.VideoCapture(0)


def gen():
    while True:
        read_return_code, frame = vc.read()
        frame = cv2.flip(frame, 1)
        frame = cv2.resize(frame, (350, 200))
        encode_return_code, image_buffer = cv2.imencode('camera.png', frame)
        io_buf = io.BytesIO(image_buffer)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + io_buf.read() + b'\r\n')

def gen_pi(camera):
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


def servo_hor(val=50):
    pass


def servo_ver(val=50):
    pass


def servo(direction, val):
    if direction == 'ver':
        servo_ver(val)

    if direction == 'hor':
        servo_hor(val)


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

    with open('C:/Users/vitek/OneDrive/Plocha/speech.mp3', 'wb') as f:
        f.write(response.content)
