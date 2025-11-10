import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle

# Load dataset
data = pd.read_csv('5.urldata.csv')

# Extract features (URL) and labels
X = data['url']
y = data['label']

# Convert URLs into numeric features using CountVectorizer
vectorizer = CountVectorizer(analyzer='char', ngram_range=(3, 5))  # Analyzes URL characters in chunks
X_transformed = vectorizer.fit_transform(X)

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X_transformed, y, test_size=0.2, random_state=42)

# Train a Random Forest classifier
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the model and vectorizer for future use
with open('phishing_model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

with open('vectorizer.pkl', 'wb') as vectorizer_file:
    pickle.dump(vectorizer, vectorizer_file)

print("Model trained and saved successfully!")
