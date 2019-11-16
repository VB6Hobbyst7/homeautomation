#!/usr/bin/python3

from flask import Flask, redirect
import requests
import socket
from bs4 import BeautifulSoup

app = Flask(__name__)

app_host = "mbx.bevilacqua.us:8080"
roku_host = "roku.bevilacqua.us"
yamaha_host = "yamaha.bevilacqua.us"
sharp_host = "192.168.0.206"

t = "&nbsp&nbsp&nbsp&nbsp"


def index():

    header = """
             <!DOCTYPE HTML>
             <html>
             <head>
             <title>{}</title>
             <body bgcolor="#000000">
             <center>
             <font color="white" size="5">
             <big><big><big>
             <b>{}</b><br><br>
             """.format(app_host, app_host)

    body = """
           <a style="color:green" href="/on/">on</a>{}{}{}{}<a style="color:green" href="/off/">off</a><br><br>
           <a style="color:green" href="/volup/">volup</a>{}{}
           <a style="color:green" href="/mute/">mute</a>{}{}
           <a style="color:green" href="/voldown/">voldown</a><br><br>
           <a style="color:green" href="/av1/">av1</a>{}
           <a style="color:green" href="/av2/">av2</a>{}
           <a style="color:green" href="/audio1/">audio1</a><br><br>
           <a style="color:blue" href="/back/">back</a>{}{}{}{}<a style="color:blue" href="/home/">home</a><br><br>
           <a style="color:red" href="/up/">up</a><br><br>
           <a style="color:red" href="/left/">left</a>{}{}<a style="color:blue" href="/sel/">sel</a>{}{}
           <a style="color:red" href="/right/">right</a><br><br>
           <a style="color:red" href="/down/">down</a><br><br><br>
           <a style="color:blue" href="/rev/">rev</a>{}{}<a style="color:blue" href="/play/">play</a>{}{}
           <a style="color:blue" href="/fwd/">fwd</a><br><br>
           <a style="color:blue" href="/info/">info</a><br><br>
           """.format(t, t, t, t, t, t, t, t, t, t, t, t, t, t, t, t, t, t, t, t, t, t)

    footer = """
             </big></big></big>
             </font>
             </center>
             </body>
             </html>
             """

    html = header+body+footer

    return html


@app.route("/")
def default_page():
    return index()


@app.route("/back/")
def back():
    requests.request("POST", "http://{}:8060/keypress/back".format(roku_host))
    return redirect("http://{}".format(app_host), code=302)


@app.route("/home/")
def home():
    requests.request("POST", "http://{}:8060/keypress/home".format(roku_host))
    return redirect("http://{}".format(app_host), code=302)


@app.route("/up/")
def up():
    requests.request("POST", "http://{}:8060/keypress/up".format(roku_host))
    return redirect("http://{}".format(app_host), code=302)


@app.route("/left/")
def left():
    requests.request("POST", "http://{}:8060/keypress/left".format(roku_host))
    return redirect("http://{}".format(app_host), code=302)


@app.route("/sel/")
def sel():
    requests.request("POST", "http://{}:8060/keypress/select".format(roku_host))
    return redirect("http://{}".format(app_host), code=302)


@app.route("/right/")
def right():
    requests.request("POST", "http://{}:8060/keypress/right".format(roku_host))
    return redirect("http://{}".format(app_host), code=302)


@app.route("/down/")
def down():
    requests.request("POST", "http://{}:8060/keypress/down".format(roku_host))
    return redirect("http://{}".format(app_host), code=302)


@app.route("/info/")
def info():
    requests.request("POST", "http://{}:8060/keypress/info".format(roku_host))
    return redirect("http://{}".format(app_host), code=302)


@app.route("/fwd/")
def fwd():
    requests.request("POST", "http://{}:8060/keypress/fwd".format(roku_host))
    return redirect("http://{}".format(app_host), code=302)


@app.route("/rev/")
def rev():
    requests.request("POST", "http://{}:8060/keypress/rev".format(roku_host))
    return redirect("http://{}".format(app_host), code=302)


@app.route("/play/")
def play():
    requests.request("POST", "http://{}:8060/keypress/play".format(roku_host))
    return redirect("http://{}".format(app_host), code=302)


@app.route("/volup/")
def volup():
    r = requests.request("POST", "http://{}/YamahaRemoteControl/ctrl".format(yamaha_host),
                         data="<YAMAHA_AV cmd=\"GET\">"
                              "<Main_Zone>"
                              "<Volume>"
                              "<Lvl>GetParam</Lvl>"
                              "</Volume>"
                              "</Main_Zone>"
                              "</YAMAHA_AV>")
    soup = BeautifulSoup(r.content, 'lxml')
    current_volume = soup.find('val').text
    step = 10
    vol = int(current_volume) + int(step)
    requests.request("POST", "http://{}/YamahaRemoteControl/ctrl".format(yamaha_host),
                     data="<YAMAHA_AV cmd=\"PUT\">"
                          "<Main_Zone>"
                          "<Volume>"
                          "<Lvl>"
                          "<Val>{}</Val>"
                          "<Exp>1</Exp>"
                          "<Unit>dB</Unit>"
                          "</Lvl>"
                          "</Volume>"
                          "</Main_Zone>"
                          "</YAMAHA_AV>".format(vol))
    return redirect("http://{}".format(app_host), code=302)


@app.route("/voldown/")
def voldown():
    r = requests.request("POST", "http://{}/YamahaRemoteControl/ctrl".format(yamaha_host),
                         data="<YAMAHA_AV cmd=\"GET\">"
                              "<Main_Zone>"
                              "<Volume>"
                              "<Lvl>GetParam</Lvl>"
                              "</Volume>"
                              "</Main_Zone>"
                              "</YAMAHA_AV>")
    soup = BeautifulSoup(r.content, 'lxml')
    current_volume = soup.find('val').text
    step = 10
    vol = int(current_volume) - int(step)
    requests.request("POST", "http://{}/YamahaRemoteControl/ctrl".format(yamaha_host),
                     data="<YAMAHA_AV cmd=\"PUT\">"
                          "<Main_Zone>"
                          "<Volume>"
                          "<Lvl>"
                          "<Val>{}</Val>"
                          "<Exp>1</Exp>"
                          "<Unit>dB</Unit>"
                          "</Lvl>"
                          "</Volume>"
                          "</Main_Zone>"
                          "</YAMAHA_AV>".format(vol))
    return redirect("http://{}".format(app_host), code=302)


@app.route("/mute/")
def mute():
    r = requests.request("POST", "http://{}/YamahaRemoteControl/ctrl".format(yamaha_host),
                         data="<YAMAHA_AV cmd=\"GET\">"
                              "<Main_Zone>"
                              "<Volume>"
                              "<Mute>GetParam</Mute>"
                              "</Volume>"
                              "</Main_Zone>"
                              "</YAMAHA_AV>")
    soup = BeautifulSoup(r.content, 'lxml')
    mute_state = soup.find('mute').text

    if mute_state in 'Off':
        mute_set = 'On'
    else:
        mute_set = 'Off'

    requests.request("POST", "http://{}/YamahaRemoteControl/ctrl".format(yamaha_host),
                     data="<YAMAHA_AV cmd=\"PUT\">"
                          "<Main_Zone>"
                          "<Volume>"
                          "<Mute>{}</Mute>"
                          "</Volume>"
                          "</Main_Zone>"
                          "</YAMAHA_AV>".format(mute_set))
    return redirect("http://{}".format(app_host), code=302)


@app.route("/av1/")
def av1():
    requests.request("POST", "http://{}/YamahaRemoteControl/ctrl".format(yamaha_host),
                     data="<YAMAHA_AV cmd=\"PUT\">"
                          "<Main_Zone>"
                          "<Input>"
                          "<Input_Sel>AV1</Input_Sel>"
                          "</Input>"
                          "</Main_Zone>"
                          "</YAMAHA_AV>")
    return redirect("http://{}".format(app_host), code=302)


@app.route("/av2/")
def av2():
    requests.request("POST", "http://{}/YamahaRemoteControl/ctrl".format(yamaha_host),
                     data="<YAMAHA_AV cmd=\"PUT\">"
                          "<Main_Zone>"
                          "<Input>"
                          "<Input_Sel>AV2</Input_Sel>"
                          "</Input>"
                          "</Main_Zone>"
                          "</YAMAHA_AV>")
    return redirect("http://{}".format(app_host), code=302)


@app.route("/audio1/")
def audio1():
    requests.request("POST", "http://{}/YamahaRemoteControl/ctrl".format(yamaha_host),
                     data="<YAMAHA_AV cmd=\"PUT\">"
                          "<Main_Zone>"
                          "<Input>"
                          "<Input_Sel>AUDIO1</Input_Sel>"
                          "</Input>"
                          "</Main_Zone>"
                          "</YAMAHA_AV>")
    return redirect("http://{}".format(app_host), code=302)


@app.route("/on/")
def on():

    port = 10002
    data = 'user\x0dpass\x0dPOWR1   \x0d'
    encdata = data.encode()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.connect((sharp_host, port))
    sock.sendall(encdata)
    sock.close()
    return redirect("http://{}".format(app_host), code=302)


@app.route("/off/")
def off():

    port = 10002
    data = 'user\x0dpass\x0dPOWR0   \x0d'
    encdata = data.encode()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.connect((sharp_host, port))
    sock.sendall(encdata)
    sock.close()
    return redirect("http://{}".format(app_host), code=302)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
