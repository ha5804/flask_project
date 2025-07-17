from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/lstm/')
def learn():
    return render_template('lstm/index.html')

@app.route('/lstm/step0')
def step0():
    return render_template('lstm/step0.html')

@app.route('/lstm/step1')
def step1():
    return render_template('lstm/step1.html')

@app.route('/lstm/step2')
def step2():
    return render_template('lstm/step2.html')

if __name__ == '__main__':
    app.run(debug=True)
