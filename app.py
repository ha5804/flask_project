# square.py
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/register', methods = ["GET"])
def register():
    return render_template("register.html")

@app.route('/register', methods=['POST'])
def register_post():
    username = request.form['username']
    password = request.form['password']
    
    # 아직은 DB 없이 단순 출력만
    print(f"가입한 사용자: {username}, 비밀번호: {password}")

    return redirect('/')

if __name__ == '__main__':
    app.run(debug = True)

