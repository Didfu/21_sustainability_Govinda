from flask import Flask, render_template, request
from flask import redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/input', methods=['GET', 'POST'])
def input():
    if request.method == 'GET':
        return render_template('input.html')
    elif request.method == 'POST':
        # Process the form data
        input_pressure = float(request.form.get('input_pressure', 0))
        input_wind = float(request.form.get('input_wind', 0))
        input_temperature = float(request.form.get('input_temperature', 0))
        input_date = request.form.get('input_date', '')
        input_time = request.form.get('input_time', '')
        # Generate graph
        
        return render_template('input.html')
@app.route('/predict', methods=['POST'])



@app.route('/month')
def result():
    return render_template('month.html')
@app.route('/live')
def live():
    return render_template('live.html')
if __name__ == '__main__':
    app.run(debug=True)
