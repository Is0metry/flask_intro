from flask import Flask
from flask import render_template, request
import model as m
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index(prediction=None):
    if request.method == 'POST':
        prediction = m.predict(request.form['txt_input'])
    return render_template('index.html', prediction=prediction)


@app.route('/hello/')
def hello():
    return 'Hello, Im alive'
