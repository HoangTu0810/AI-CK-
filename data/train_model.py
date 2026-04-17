import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib
import os

def train_and_save():
    csv_path = os.path.join(os.path.dirname(__file__), 'malicious_phish.csv')
    print(f"Loading CSV from {csv_path}")
    df = pd.read_csv(csv_path)
    print(f"Loaded {len(df)} rows")
    # Assume 'phishing' and 'defacement' are malicious, 'benign' is safe
    df['label'] = df['type'].apply(lambda x: 1 if x in ['phishing', 'defacement'] else 0)
    
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(df['url'])
    y = df['label']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = LogisticRegression()
    model.fit(X_train, y_train)
    
    # Save model and vectorizer
    model_dir = os.path.join(os.path.dirname(__file__), '..', 'model')
    os.makedirs(model_dir, exist_ok=True)
    joblib.dump(model, os.path.join(model_dir, 'model.pkl'))
    joblib.dump(vectorizer, os.path.join(model_dir, 'vectorizer.pkl'))
    
    print("Model trained and saved successfully.")