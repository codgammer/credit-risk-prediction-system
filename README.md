# Credit Risk Prediction App

A Machine Learning web application that predicts whether a credit applicant is **Good Risk** or **Bad Risk** using an Extra Trees Classifier model.  
The app provides an interactive UI built with Streamlit for real-time prediction.

---

## 🚀 Features

- Predict credit risk instantly from user input
- Machine learning model trained using Extra Trees Classifier
- Categorical feature encoding using LabelEncoder
- Clean interactive Streamlit interface
- Reproducible environment with requirements.txt

---

## 🧠 Model Overview

The model was trained on a credit dataset using:

- Extra Trees Classifier (Ensemble ML)
- Feature encoding for categorical attributes
- Structured input pipeline
- Scikit-learn training workflow

Input features:

- Age
- Sex
- Job
- Housing
- Saving accounts
- Checking account
- Purpose
- Credit amount
- Duration

Output:

- Good Risk
- Bad Risk

---

## 🖥️ Tech Stack

- Python
- Scikit-learn
- Pandas
- NumPy
- Streamlit
- Joblib

---

## 📂 Project Structure

```
credit-risk-prediction/
│
├── app.py
├── Extra_Trees_Credit_model.pkl
├── *_encoder.pkl
├── requirements.txt
├── README.md
└── venv/ (ignored)
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/codgammer/credit-risk-prediction-system.git
cd credit-risk-prediction
```

Create virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Open browser:

```
http://localhost:8501
```

---

## 📊 Example Use Case

The app can be used by:

- Banks for loan pre-screening
- Fintech risk scoring
- Credit eligibility simulations
- Educational ML demonstrations

---

## 🔒 Notes

Model files are excluded from GitHub in production projects due to size and security.  
You may retrain or upload them privately if needed.

---

## 👨‍💻 Author

Kishan Prabhu  
AI & ML Engineer

---

## ⭐ Future Improvements

- Add probability confidence score
- Model explainability (SHAP)
- CSV batch predictions
- Deployment to cloud
- REST API integration

---

## 📜 License

This project is for educational purposes.
