#!/usr/bin/python3

from flask import Flask, redirect
import requests
import subprocess
from bs4 import BeautifulSoup

app = Flask(__name__)


hostname = "mbx.bevilacqua.us:8080"
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
             """.format(hostname, hostname)

    body = """
           <a style="color:green" href="/on/">on</a>{}{}{}{}<a style="color:green" href="/off/">off</a><br><br>
           <a style="color:green" href="/volup/">volup</a>{}{}{}{}
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
    requests.request("POST", "http://192.168.0.198:8060/keypress/back")
    return redirect("http://{}".format(hostname), code=302)


@app.route("/home/")
def home():
    requests.request("POST", "http://192.168.0.198:8060/keypress/home")
    return redirect("http://{}".format(hostname), code=302)


@app.route("/up/")
def up():
    requests.request("POST", "http://192.168.0.198:8060/keypress/up")
    return redirect("http://{}".format(hostname), code=302)


@app.route("/left/")
def left():
    requests.request("POST", "http://192.168.0.198:8060/keypress/left")
    return redirect("http://{}".format(hostname), code=302)


@app.route("/sel/")
def sel():
    requests.request("POST", "http://192.168.0.198:8060/keypress/select")
    return redirect("http://{}".format(hostname), code=302)


@app.route("/right/")
def right():
    requests.request("POST", "http://192.168.0.198:8060/keypress/right")
    return redirect("http://{}".format(hostname), code=302)


@app.route("/down/")
def down():
    requests.request("POST", "http://192.168.0.198:8060/keypress/down")
    return redirect("http://{}".format(hostname), code=302)


@app.route("/info/")
def info():
    requests.request("POST", "http://192.168.0.198:8060/keypress/info")
    return redirect("http://{}".format(hostname), code=302)


@app.route("/fwd/")
def fwd():
    requests.request("POST", "http://192.168.0.198:8060/keypress/fwd")
    return redirect("http://{}".format(hostname), code=302)


@app.route("/rev/")
def rev():
    requests.request("POST", "http://192.168.0.198:8060/keypress/rev")
    return redirect("http://{}".format(hostname), code=302)


@app.route("/play/")
def play():
    requests.request("POST", "http://192.168.0.198:8060/keypress/play")
    return redirect("http://{}".format(hostname), code=302)


@app.route("/volup/")
def volup():
    r = requests.request("POST", "http://192.168.0.40/YamahaRemoteControl/ctrl", data="<YAMAHA_AV cmd=\"GET\">"
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
    p = requests.request("POST", "http://192.168.0.40/YamahaRemoteControl/ctrl", data="<YAMAHA_AV cmd=\"PUT\">"
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
    return redirect("http://{}".format(hostname), code=302)


@app.route("/voldown/")
def voldown():
    r = requests.request("POST", "http://192.168.0.40/YamahaRemoteControl/ctrl", data="<YAMAHA_AV cmd=\"GET\">"
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
    p = requests.request("POST", "http://192.168.0.40/YamahaRemoteControl/ctrl", data="<YAMAHA_AV cmd=\"PUT\">"
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
    return redirect("http://{}".format(hostname), code=302)


@app.route("/on/")
def on():
    subprocess.call(["echo -e -n 'a\x0da\x0dPOWR1   \x0d' | socat - tcp4:192.168.0.206:10002"], shell=True)
    return redirect("http://{}".format(hostname), code=302)


@app.route("/off/")
def off():
    subprocess.call(["echo -e -n 'a\x0da\x0dPOWR0   \x0d' | socat - tcp4:192.168.0.206:10002"], shell=True)
    return redirect("http://{}".format(hostname), code=302)


@app.route("/av1/")
def av1():
    requests.request("POST", "http://192.168.0.40/YamahaRemoteControl/ctrl", data="<YAMAHA_AV cmd=\"PUT\"><Main_Zone><Input><Input_Sel>AV1</Input_Sel></Input></Main_Zone></YAMAHA_AV>")
    return redirect("http://{}".format(hostname), code=302)


@app.route("/av2/")
def av2():
    requests.request("POST", "http://192.168.0.40/YamahaRemoteControl/ctrl", data="<YAMAHA_AV cmd=\"PUT\"><Main_Zone><Input><Input_Sel>AV2</Input_Sel></Input></Main_Zone></YAMAHA_AV>")
    return redirect("http://{}".format(hostname), code=302)


@app.route("/audio1/")
def audio1():
    requests.request("POST", "http://192.168.0.40/YamahaRemoteControl/ctrl", data="<YAMAHA_AV cmd=\"PUT\"><Main_Zone><Input><Input_Sel>AUDIO1</Input_Sel></Input></Main_Zone></YAMAHA_AV>")
    return redirect("http://{}".format(hostname), code=302)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
