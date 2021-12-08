# 초간단 웹서버 프로그램 웹 브라우저에서 http://localhost:5000/ 으로 접속
from flask import Flask
app = Flask(__name__)           # Flask 서버 객체를 이 모듈로 생성

@app.route("/")                 # 웹에서 적속할 때의 최상위 폴더를 의미
def helloworld():               # 그 폴더를 접근했을 때 실행하는 함수는 바로 밑에 줄에 써 주어야 함
    return "Hello World"

if __name__ == "__main__":      # 이 그로그램을 직접호출하여 실행할 경우에만 실행
    app.run(host="0.0.0.0")     # 내 기계에서 접근함. 포트번호는 5000번이 default