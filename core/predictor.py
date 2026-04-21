import joblib
import os

class WebsitePredictor:
    def __init__(self):
        model_dir = os.path.join(os.path.dirname(__file__), '..', 'model')
        model_path = os.path.join(model_dir, 'model.pkl')
        vectorizer_path = os.path.join(model_dir, 'vectorizer.pkl')
        try:
            self.model = joblib.load(model_path)
            self.vectorizer = joblib.load(vectorizer_path)
        except FileNotFoundError:
            raise FileNotFoundError("Model files not found. Please train the model first using --train.")

    def predict(self, url: str) -> str:
        X = self.vectorizer.transform([url])
        pred = self.model.predict(X)[0]
        return "BLOCK" if pred == 1 else "ALLOW"

# Create a global predictor instance
predictor = WebsitePredictor()

def predict_website(url: str) -> str:
    return predictor.predict(url).lower()

# Create a global predictor instance
predictor = WebsitePredictor()

def predict_website(url: str) -> str:
    return predictor.predict(url).lower()