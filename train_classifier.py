import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Load preprocessed dataset
df = pd.read_csv("cleaned_crime_reports.csv")

# Split dataset into training (80%) and testing (20%)
X_train, X_test, y_train, y_test = train_test_split(df["cleaned_text"], df["Category"], test_size=0.2, random_state=42)

# Create a text classification pipeline
pipeline = Pipeline([
    ("tfidf", TfidfVectorizer()),  # Convert text to TF-IDF features
    ("classifier", MultinomialNB())  # Train a Naïve Bayes classifier
])

# Train the model
pipeline.fit(X_train, y_train)

# Evaluate model performance
y_pred = pipeline.predict(X_test)

print("Model Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Save trained model
joblib.dump(pipeline, "crime_classifier.pkl")

print("Model training complete! ✅ Model saved as 'crime_classifier.pkl'")
