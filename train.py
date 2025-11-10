import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

# Step 1: Load the dataset
data = pd.read_csv('abc.csv')  

# Check the first few rows to understand the data
print("First few rows of the dataset:")
print(data.head())

# Step 2: Preprocess the data
# Extract the URL column as the feature (X) and the type column as the label (y)
X = data['url']
y = data['type']

# Use CountVectorizer to convert URLs into feature vectors (Bag-of-Words approach)
vectorizer = CountVectorizer()

# Transform the URLs into feature vectors (numerical representation)
X_vec = vectorizer.fit_transform(X)

# Step 3: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2, random_state=42)

# Step 4: Initialize the RandomForest Classifier for multiclass classification
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Step 5: Train the model on the training data
model.fit(X_train, y_train)

# Step 6: Evaluate the model's performance on the test data
y_pred = model.predict(X_test)

# Step 7: Print the classification report (precision, recall, F1-score)
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Step 8: Evaluate the accuracy of the model
accuracy = model.score(X_test, y_test)
print(f'Model Accuracy: {accuracy * 100:.2f}%')

# Step 9: Save the trained model and vectorizer to files using joblib
joblib.dump(model, 'phishing_model.pkl')  # Save the trained model
joblib.dump(vectorizer, 'vectorizer.pkl')  # Save the vectorizer (for transforming URLs later)

print("Model and vectorizer have been saved successfully!")
