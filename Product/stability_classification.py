import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from power_generation import PowerPredictionModel
import matplotlib.pyplot as plt
import pickle
import os

class StabilityPredictor:
    def __init__(self, csv_file):
        self.data = pd.read_csv(csv_file)
        self.preprocess_data()
        self.train_model()

    def preprocess_data(self):
        self.data["stability"] = self.data["stability"].replace({"stable": 1, "unstable": 0})
        self.data["date"] = pd.to_datetime(self.data["date"], format="%d-%m-%Y %H:%M")
        self.data["day"] = self.data["date"].dt.day
        self.data["month"] = self.data["date"].dt.month
        self.data["year"] = self.data["date"].dt.year
        self.data["hour"] = self.data["date"].dt.hour
        self.X = self.data[["day", "month", "year", "hour", "n1", "n2", "n3", "c1", "c2", "c3", "p1", "p2", "p3"]]
        self.y = self.data["stability"]
        
    def train_model(self, n_estimators=150, random_state=42):
        X_train_val, self.X_test, y_train_val, self.y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=random_state)
        self.X_train, self.X_val, self.y_train, self.y_val = train_test_split(X_train_val, y_train_val, test_size=0.25, random_state=random_state)
        self.model = RandomForestClassifier(n_estimators=n_estimators, random_state=random_state)
        self.model.fit(self.X_train, self.y_train)

    def evaluate_model(self):
        print("Evaluation of Classification model")
        y_train_pred = self.model.predict(self.X_train)
        train_accuracy = accuracy_score(self.y_train, y_train_pred)

        y_val_pred = self.model.predict(self.X_val)
        val_accuracy = accuracy_score(self.y_val, y_val_pred)

        y_test_pred = self.model.predict(self.X_test)
        test_accuracy = accuracy_score(self.y_test, y_test_pred)
        return ({"Training Accuracy": train_accuracy, "Validation Accuracy": val_accuracy, "Testing Accuracy": test_accuracy})
        # return ("Training Accuracy: ",train_accuracy,"\nValidation Accuracy: ", val_accuracy, "\nTesting Accuracy: ", test_accuracy )

    def predict_stability(self, input_data, n1, n2, n3):
        input_data["date"] = pd.to_datetime(input_data["date"], format="%d-%m-%Y %H:%M")
        input_data["day"] = input_data["date"].dt.day
        input_data["month"] = input_data["date"].dt.month
        input_data["year"] = input_data["date"].dt.year
        input_data["hour"] = input_data["date"].dt.hour
        new_df = pd.DataFrame({
            "day": input_data["day"],
            "month": input_data["month"],
            "year": input_data["year"],
            "hour": input_data["hour"],
            "n1": n1,
            "n2": n2,
            "n3": n3,
            "c1": input_data["c1"],
            "c2": input_data["c2"],
            "c3": input_data["c3"],
            "p1": input_data["p1"],
            "p2": input_data["p2"],
            "p3": input_data["p3"],
        })
        predicted_stability = self.model.predict(new_df)
        print(predicted_stability)
        return predicted_stability
    

# Example usage:
# if __name__ == "__main__":
#     csv_file = "Datasets/Grid with Power.csv"
#     predictor = StabilityPredictor(csv_file)
#     predictor.evaluate_model()

#     p = PowerPredictionModel("Datasets/Power19-23.csv")
#     n1, n2, n3 = p.predict_power(pd.read_csv("Datasets/validation.csv"))
    
#     predictor.predict_stability(pd.read_csv("Datasets/grid_validation.csv"), n1, n2, n3)
