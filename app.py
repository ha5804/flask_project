from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/balance/', methods =["POST"])
# POST, GET, PUT, DELETE는 대문자로 정의
def input_balance():
    balance = request.form["balance"]
    # balance는 문자열
    return render_template("index.html", balance = balance) 
    # reder_template으로 홈페이지를 연결하고, balance 값을 전달한다.

@app.route('/step1/')
def step1():
    return render_template("step1.html")
if __name__ == '__main__':
    app.run(debug=True)
