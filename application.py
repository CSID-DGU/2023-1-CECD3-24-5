from flask import Flask, jsonify, request, render_template
from service.CreateQuizsService import *
from flask_cors import CORS

import sys
import os

# 현재 스크립트의 경로를 가져옴
current_path = os.path.dirname(os.path.abspath(__file__))

sys.path.append(os.path.join(current_path, 'service'))

#app에서 static 폴더를 React의 build 폴더로 설정
app = Flask(__name__, static_folder='front/build', static_url_path='/')
CORS(app)

#메인 페이지 라우팅
@app.route('/')
def index():
    return app.send_static_file('index.html')


#문제 생성 API
@app.route('/create/quiz', methods=['GET'])
def fetchQuizsController():
    number = request.args.get('number', default=1, type=int)

    if number is None:
        return 'scope와 number 쿼리 매개변수가 필요합니다.'
    
    #CreateQuizsService의 인스턴스 생성
    quiz_service = CreateQuizsService()

    quizes = quiz_service.createQuizs(number)
    
    return jsonify(quizes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


