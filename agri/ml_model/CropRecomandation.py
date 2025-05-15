
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib
import os

# Load the dataset 
data = pd.read_csv('Crop_recommendation.csv')

# Features and target
X = data.drop('label', axis=1)
y = data['label']

# Train the model
model = DecisionTreeClassifier()
model.fit(X, y)

# Save the model in the same folder
model_path = 'crop_recommendation_model.pkl'
joblib.dump(model, model_path)



