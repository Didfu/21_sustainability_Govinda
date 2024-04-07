from flask import Flask, render_template, request
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from flask import redirect

app = Flask(__name__)

# Sample dataset for demonstration
data = {
    'X': [1, 2, 3, 4, 5],
    'y': [2, 4, 5, 4, 5]
}

# Load machine learning model
model = LinearRegression()
X_train = pd.DataFrame(data['X'])
y_train = pd.DataFrame(data['y'])
model.fit(X_train, y_train)

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
def predict():
    # Get user input
    input_x = int(request.form.get('input_x', 0))
    
    # Make prediction using the model
    prediction = model.predict([[input_x]])
    
    # Generate graph
    plt.scatter(data['X'], data['y'], color='blue')
    plt.scatter(input_x, prediction, color='red')
    plt.plot(data['X'], model.predict(X_train), color='green')
    plt.xlabel('X')
    plt.ylabel('y')
    plt.title('Linear Regression Prediction')
    plt.savefig('static/prediction_plot.png')  # Save the plot
    plt.close()  # Close the plot to free up memory
    
    return render_template('result.html', prediction=prediction[0])
@app.route('/month')
def result():
    return render_template('month.html')
@app.route('/live')
def live():
    return render_template('live.html')
if __name__ == '__main__':
    app.run(debug=True)
