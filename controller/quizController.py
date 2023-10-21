from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

import sys
import os

# 현재 스크립트의 경로를 가져옴
current_path = os.path.dirname(os.path.abspath(__file__))

sys.path.append(os.path.join(current_path, '../service'))
from quizService import * 

#app에서 static 폴더를 React의 build 폴더로 설정
app = Flask(__name__, static_folder='../front/build', static_url_path='/')
CORS(app)

#메인 페이지 라우팅
@app.route('/')
def index():
    return app.send_static_file('index.html')

#템플릿 API
@app.route('/home', methods=['GET'])
def fetchHome():
    return render_template('home.html')

@app.route('/generate_page', methods=['GET'])
def FetchGeneratePage():
    return render_template('create.html')

@app.route('/solve_page', methods=['GET'])
def fetchSolvePage():
    return render_template('solve.html')

#문제 생성 API
@app.route('/create/quiz', methods=['GET'])
def fetchQuizsController():
    scope = request.args.get('scope')
    number = request.args.get('number')
    if scope is None or number is None:
        return 'scope와 number 쿼리 매개변수가 필요합니다.'
    
    # return "hello"
    return jsonify(
        CreateQuizsService.createQuizs(
            scope,
            number
            )
        )