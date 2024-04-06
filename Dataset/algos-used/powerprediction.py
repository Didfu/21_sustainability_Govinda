import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset
df = pd.read_csv("Power19-23.csv")

# Convert the "DateTime" column to datetime format
df["DateTime"] = pd.to_datetime(df["DateTime"])

# Extract date and time components
df["Day"] = df["DateTime"].dt.day
df["Month"] = df["DateTime"].dt.month
df["Year"] = df["DateTime"].dt.year
df["Hour"] = df["DateTime"].dt.hour

# Define features (X) and target variable (Y)
X = df[["Day", "Month", "Year", "Hour", "Wind speed", "Air temperature", "Pressure"]]
Y = df["Power generated"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Initialize and train the Random Forest Regressor
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model performance using Mean Squared Error (MSE) and R-squared score
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print the evaluation metrics
print("Mean Squared Error (MSE):", mse)
print("R-squared score:", r2)