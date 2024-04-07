from flask import Flask, request, jsonify, render_template
import pandas as pd
from stability_classification import StabilityPredictor
from power_generation import PowerPredictionModel

from live import getData

app = Flask(__name__, template_folder="templates")

# Initialize the StabilityPredictor and PowerPredictionModel instances
power_prediction_model = PowerPredictionModel("Datasets/Power19-23.csv")
stability_predictor = StabilityPredictor("Datasets/Grid with Power.csv")


@app.route("/")
def home():
    return render_template('index.html')



@app.route('/power_generation')
def power_generation():
    data = getData()
    print(data)
    data["DateTime"] = pd.to_datetime(data["DateTime"], format="%d-%m-%Y %H:%M:%S")  # Assuming JSON input with required fields for stability prediction
    n1, n2, n3, power = power_prediction_model.predict_power(data)

    
    return jsonify({'Power Generated would be': power}), 200

@app.route('/evaluate', methods=['GET'])
def evaluate_model():
    res2 = stability_predictor.evaluate_model()
    res1 = power_prediction_model.evaluate()
    print(res1)
    print(res2)
    return render_template("evaluate.html", data={"Evaluation of power prediction model": res1, "Evaluation of stability classifier model": res2})

@app.route("/validate_data")
def validate_data():
    n1, n2, n3, power = power_prediction_model.predict_power(pd.read_csv("Datasets/validation.csv"))
    df = pd.read_csv("Datasets/grid_validation.csv")
    res = stability_predictor.predict_stability(df, n1, n2, n3)
    df["res"] = res.tolist()
    df["res"] = df["res"].replace({0: "unstable", 1: "stable"})
    return render_template("DataValidation.html", data = df, res=res.tolist())

if __name__ == '__main__':
    app.run(port=5000, debug=True)
