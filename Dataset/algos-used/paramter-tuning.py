from sklearn.model_selection import GridSearchCV

# Define the range of values for n_estimators
param_grid = {'n_estimators': [50, 100, 150, 200]}

# Initialize the Random Forest classifier
rf_classifier = RandomForestClassifier(random_state=42)

# Perform grid search
grid_search = GridSearchCV(estimator=rf_classifier, param_grid=param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)

# Get the best parameter value
best_n_estimators = grid_search.best_params_['n_estimators']
print("Best n_estimators:", best_n_estimators)

# Initialize the Random Forest classifier with the best n_estimators
rf_classifier_best = RandomForestClassifier(n_estimators=best_n_estimators, random_state=42)

# Train the classifier with the best parameter
rf_classifier_best.fit(X_train, y_train)

# Predict on the testing set
y_pred_best = rf_classifier_best.predict(X_test)

# Calculate accuracy
accuracy_best = accuracy_score(y_test, y_pred_best)
print("Accuracy with best n_estimators:", accuracy_best)
