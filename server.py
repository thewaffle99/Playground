from types import BuiltinFunctionType
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/play')
def play1():
    return render_template('play.html',num=3, color='blue')

@app.route('/play/<int:num>')
def play2(num):
    return render_template('play.html',num=num)

@app.route('/play/<int:num>/<string:color>')
def play3(num=3,color='blue'):
    return render_template('play.html',num=num,color=color)

if __name__=="__main__":
    app.run(debug=True)

