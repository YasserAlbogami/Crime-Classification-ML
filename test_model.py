import joblib

# Load trained model and vectorizer
model = joblib.load("crime_classifier.pkl")

# Function to classify a new police report
def classify_report(report_text):
    prediction = model.predict([report_text])[0]
    print(f"🛑 Report: {report_text}")
    print(f"✅ Predicted Crime Category: {prediction}")
    print("-" * 50)

# 📌 Test Sample Crime Reports
test_reports = [
    "battery",  # Expected: ASSAULT
    "trespassing",  # Expected: TRESPASS
    "resisting arrest",  # Expected: OTHER OFFENSES
    "malicious mischief vandalism vehicles",  # Expected: VANDALISM
    "forgery credit card",  # Expected: FRAUD
    "burglary apartment house forcible entry",  # Expected: BURGLARY
    "possession meth amphetamine",  # Expected: DRUG/NARCOTIC
    "stolen automobile",  # Expected: VEHICLE THEFT
    "violation municipal police code",  # Expected: OTHER OFFENSES
    "petty theft auto strip",  # Expected: LARCENY/THEFT
    "robbery street gun",  # Expected: ROBBERY
    "checks forgery felony",  # Expected: FORGERY/COUNTERFEITING
    "parole violation",  # Expected: OTHER OFFENSES
    "violation restraining order",  # Expected: OTHER OFFENSES
    "inflict injury cohabitee",  # Expected: ASSAULT
]


# Run classification on each test report
for report in test_reports:
    classify_report(report)
