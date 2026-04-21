# Website Blocker AI

An AI-powered website blocker that uses machine learning to detect and block malicious websites.

## Features

- Train a machine learning model on phishing and malicious website data
- GUI application to check and block websites
- Automatic blocking by modifying the hosts file (requires administrator privileges)

## Installation

1. Install Python dependencies:

   ```
   pip install -r requirements.txt
   ```

2. Train the model:
   ```
   python model/main.py --train
   ```

## Usage

### Training the Model

Run the training script to build the AI model:

```
python model/main.py --train
```

This will:

- Load the dataset from `data/malicious_phish.csv`
- Train a logistic regression model using TF-IDF features
- Save the model and vectorizer to the `model/` directory

### Running the GUI

Launch the desktop application:

```
python model/main.py --gui
```

The GUI allows you to:

- Enter a URL to check if it's malicious
- View the AI's decision (BLOCK or ALLOW)
- Unblock previously blocked websites
- View history of checks

## Project Structure

```
website_blocker_ai/
├── core/
│   ├── blocker.py      # Website blocking logic
│   └── predictor.py    # AI prediction module
├── data/
│   ├── malicious_phish.csv  # Training dataset
│   └── train_model.py       # Model training script
├── gui/
│   └── app.py          # Tkinter GUI application
├── model/
│   ├── main.py         # Main entry point
│   ├── model.pkl       # Trained model (generated)
│   └── vectorizer.pkl  # TF-IDF vectorizer (generated)
└── requirements.txt    # Python dependencies
```

## Requirements

- Python 3.7+
- Administrator privileges for blocking websites (modifies hosts file)
- Dependencies: pandas, scikit-learn, joblib

## How It Works

1. The model is trained on a dataset of URLs labeled as phishing, benign, or defacement.
2. URLs are converted to TF-IDF features for machine learning.
3. A logistic regression classifier predicts if a URL is malicious.
4. Malicious URLs are automatically blocked by adding entries to the system's hosts file.

## Notes

- Blocking websites requires administrator privileges on Windows.
- The model classifies 'phishing' and 'defacement' URLs as malicious.
- The GUI is in Vietnamese, but can be easily translated.
