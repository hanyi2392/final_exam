# 웹서버 프로그램 웹 브라우저에서 http://localhost:5000/로 접속하면 
# index.html을 실행하고 버튼을 이용하여 LED 작동시킴

from flask import Flask, request
from flask import render_template
import RPi.GPIO as GPIO

app = Flask(__name__)
GPIO.setmode(GPIO.BOARD)                    #BOARD는 커넥터 pin번호 사용
pin=7                                       # 7번 pin. 즉, GPIO4 사용
GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW) 

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/led/on")                       # index.html에서 이 주소를 접속하여 해당 함수를 실행
def led_on():
    try:
        GPIO.output(pin, GPIO.HIGH)         # 불을 켜고
        return "ok"                         # 함수가 'ok'문자열을 반환함
    except :
        return "fail"

@app.route("/led/off")
def led_off():
    try:
        GPIO.output(pin, GPIO.LOW)
        return "ok"
    except :
        return "fail"

if __name__ == "__main__":
    app.run(host="0.0.0.0")