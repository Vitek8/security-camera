from flask import Flask, render_template, Response, redirect, url_for, request
import socket
import vlc
import functions as func
from camera import Camera

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/text_to_speech", methods=["POST", "GET"])
def text_to_speech():
    if request.method == "POST":
        text = request.form["tts"]
        print(text)
        return redirect(url_for("text_to_speech_redirect", speech=text))
    else:
        return render_template("text_to_speech.html")


@app.route("/text_to_speech/<speech>")
def text_to_speech_redirect(speech):
    func.speech(speech)
    player = vlc.MediaPlayer("C:/Users/vitek/OneDrive/Plocha/speech.mp3")
    player.play()
    return redirect(url_for("text_to_speech"))


@app.route("/text_to_speech/")
def repeat():
    player = vlc.MediaPlayer("C:/Users/vitek/OneDrive/Plocha/speech.mp3")
    player.play()
    return redirect(url_for("text_to_speech"))

@app.route('/camera', methods=[ "GET"])
def index():
    ser_values = func.read()
    ver = ser_values[0]
    hor = ser_values[1]
    step = ser_values[2]
    data = {"ver": ver, "hor": hor, "step": step}
    print("vertikální osa: " + str(ver))
    print("horizontální osa: " + str(hor))
    func.servo("hor", hor)
    func.servo("ver", ver)
    return render_template("camera.html", data=data)


@app.route("/camera/<data>", methods=["GET"])
def cam(data):
    func.write(data)
    return redirect(url_for("index"))


@app.route('/camera_streaming')
def camera():
    return Response(
        func.gen(),
        mimetype='multipart/x-mixed-replace; boundary=frame',
    )

#picamera
#@app.route('/camera_streaming')
#def camera():
#    return Response(func.gen_pi(Camera()),
#        func.gen(),
#        mimetype='multipart/x-mixed-replace; boundary=frame',
#    )

if __name__ == "__main__":
    ip = socket.gethostbyname(socket.gethostname())
    app.run(host=ip, port=5000, debug=True)
