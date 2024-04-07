import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

class PowerPredictionModel:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.model = None
        self.preprocess_data()
        self.train_model()

    def preprocess_data(self):
        """Preprocess the power data from the given CSV file."""
        power_df = pd.read_csv(self.csv_file)
        power_df["DateTime"] = pd.to_datetime(power_df["DateTime"], format="%d-%m-%Y %H:%M")
        power_df["day"] = power_df["DateTime"].dt.day
        power_df["month"] = power_df["DateTime"].dt.month
        power_df["year"] = power_df["DateTime"].dt.year
        power_df["hour"] = power_df["DateTime"].dt.hour
        X = power_df[["day", "month", "year", "hour", "Wind speed", "Air temperature", "Pressure"]]
        y = power_df["Power generated"]
        return X, y

    def train_model(self):
        """Split the data, train a RandomForestRegressor model."""
        X, y = self.preprocess_data()
        X_train, X_test, y_train, self.y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        X_train, X_val, y_train, self.y_val = train_test_split(X_train, y_train, test_size=0.25, random_state=42)
        self.model = RandomForestRegressor()
        self.model.fit(X_train, y_train)

        # Validate the model on the validation set
        self.y_pred_val = self.model.predict(X_val)        

        # Test the model on the test set
        self.y_pred_test = self.model.predict(X_test)

        # Evaluate test performance

    def evaluate(self):
        print("Evaluation of Prediction model")
        val_mse = mean_squared_error(self.y_val, self.y_pred_val)
        val_r2 = r2_score(self.y_val, self.y_pred_val)
        test_mse = mean_squared_error(self.y_test, self.y_pred_test)
        test_r2 = r2_score(self.y_test, self.y_pred_test)
        print(f"Validation - MSE:{val_mse}\tR2:{val_r2}")
        print(f"Testing    - MSE:{test_mse}\tR2:{test_r2}")
        pass 

    def predict_power(self, input_df):
        """Predict power generation based on user input."""
        if self.model is None:
            raise Exception("Model has not been trained. Please train the model first.")

        # Ensure input_data is a DataFrame with the correct columns

        input_df["DateTime"] = pd.to_datetime(input_df["DateTime"], format="%Y-%m-%d %H:%M:%S")
        input_df["day"] = input_df["DateTime"].dt.day
        input_df["month"] = input_df["DateTime"].dt.month
        input_df["year"] = input_df["DateTime"].dt.year
        input_df["hour"] = input_df["DateTime"].dt.hour

        # Use the trained model to make predictions
        X_input = input_df[["day", "month", "year", "hour", "Wind speed", "Air temperature", "Pressure"]]
        predicted_power = self.model.predict(X_input)
        n1 = predicted_power * 0.20
        n2 = predicted_power * 0.45
        n3 = predicted_power * 0.35
        return n1, n2, n3

if __name__ == "__main__":
    p = PowerPredictionModel("Power19-23.csv")
    p.preprocess_data()
    p.train_model()
    p.evaluate()
    p.predict_power(pd.read_csv("validation.csv"))

