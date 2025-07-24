from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/balance/')
def learn():
    return render_template('lstm/index.html')

if __name__ == '__main__':
    app.run(debug=True)
