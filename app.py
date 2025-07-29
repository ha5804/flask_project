from flask import Flask, render_template, request, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.secret_key = 'supersecretekey'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///users.db"
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = True, nullable = False)
    password = db.Column(db.String(100), nullable = False)

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    username = session.get('username')
    return render_template("home.html", username = username)

@app.route('/register', methods = ["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        if User.query.filter_by(username = username).first():
            return "이미 존재하는 아이디입니다"
        
        new_user = User(username = username, password = password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))
    return render_template("register.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username, password=password).first()
        if user:
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return "아이디 또는 비밀번호가 틀렸습니다."
    return render_template('login.html')

# 로그아웃
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug = True)

