from flask import Flask, render_template, request
from flask import redirect
import pandas as pd
from power_generation import PowerPredictionModel
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/input', methods=['GET', 'POST'])
def input():
    if request.method == 'GET':
        return render_template('input.html')
    
@app.route('/result')
def result():
    return render_template('result.html')
@app.route('/month')
def month():
    return render_template('month.html')
@app.route('/live')
def live():
    return render_template('live.html')
if __name__ == '__main__':
    app.run(debug=True)
