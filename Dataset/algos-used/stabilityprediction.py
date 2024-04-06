import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from google.colab import files

# Read the dataset into a pandas DataFrame
data = pd.read_csv('GwithS.csv')

# Convert 'DateTime' column to datetime type
data['date'] = pd.to_datetime(data['date'], format="%d-%m-%Y %H:%M")

# Extract features from DateTime
data['hour'] = data['date'].dt.hour
data['day'] = data['date'].dt.day
data['month'] = data['date'].dt.month
data['year'] = data['date'].dt.year

# Define features (c1, c2, c3, p1, p2, p3, hour, day, month, year) and target variable (stability)
X = data[['c1', 'c2', 'c3', 'p1', 'p2', 'p3', 'hour', 'day', 'month', 'year']]
y = data['stability']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Random Forest classifier
rf_classifier = RandomForestClassifier(n_estimators=90, random_state=42)

# Train the classifier
rf_classifier.fit(X_train, y_train)

# Predict on the testing set
y_pred = rf_classifier.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)