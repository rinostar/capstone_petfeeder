from flask import Flask, render_template, request
import RPi.GPIO as GPIO
from time import sleep

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
	if request.method == "POST":
		in1 = 24
		in2 = 23
		en = 25
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(in1,GPIO.OUT)
		GPIO.setup(in2,GPIO.OUT)
		GPIO.setup(en,GPIO.OUT)
		GPIO.output(in1,GPIO.LOW)
		GPIO.output(in2,GPIO.LOW)
		p=GPIO.PWM(en,1000)
		p.start(50)
		GPIO.output(in1,GPIO.HIGH)
		sleep(5)
		GPIO.output(in1,GPIO.LOW)
		GPIO.cleanup()
		return render_template("index.html")
	elif request.method == "GET":
		return render_template("index.html")

if __name__ == '__main__':
	app.run(debug=True, host="0.0.0.0")
