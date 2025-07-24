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
    balance = float(balance)
    return f"입력하신 잔고는 {balance}원 입니다."

if __name__ == '__main__':
    app.run(debug=True)
