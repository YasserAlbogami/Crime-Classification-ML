import pandas as pd
import re
import nltk
from nltk.corpus import stopwords

# Download stopwords from NLTK (only required once)
nltk.download("stopwords")

# Load English stopwords
stop_words = set(stopwords.words("english")) # "the", "is", "at", "which", "and", "in", "a", "an", "to", "of", "by", "on", "with"

# Load dataset
df = pd.read_csv("train.csv")

# Function to clean text
def preprocess_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r"\W", " ", text)  # Remove special characters
    text = " ".join([word for word in text.split() if word not in stop_words])  # Remove stopwords
    return text

# Apply preprocessing to 'Descript' column
df["cleaned_text"] = df["Descript"].apply(preprocess_text)

# Save cleaned data
df[["cleaned_text", "Category"]].to_csv("cleaned_crime_reports.csv", index=False)

print("Preprocessing complete! Data saved as 'cleaned_crime_reports.csv'")
