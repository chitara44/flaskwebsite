from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():

    return render_template('casa.html')

@app.route('/about')
def about():
    return '<h1> Hello ricardo this is the about page </h1>'

@app.route('/asknumber')
def asknumber():
    return '<h1> Hello ricardo this is the asknumber page </h1>'

@app.route('/draftlist')
def draftlist():
    return render_template('draftlist.html', quotes = 'este es el texto')