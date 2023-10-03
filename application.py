from flask import Flask, jsonify, request, render_template
app = Flask(__name__)


#템플릿 API
@app.route('/', methods=['GET'])
def process_url():
    return render_template('home.html')

@app.route('/create/problem', methods=['GET'])
def process_url():
    return render_template('create.html')

@app.route('/solve/problem', methods=['GET'])
def process_url():
    return render_template('solve.html')

#문제 생성 API

if __name__ == '__main__':
    app.run()