from flask import Flask, jsonify, request, render_template
from service.CreateQuizsService import *

app = Flask(__name__)


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
    
    return jsonify(
        CreateQuizsService.createQuizs(
            scope,
            number
            )
        )

if __name__ == '__main__':
    app.run()