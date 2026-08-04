# 💳 Credit Risk Classification

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange?logo=scikitlearn)
![MLflow](https://img.shields.io/badge/MLflow-Tracking-blue?logo=mlflow)
![FastAPI](https://img.shields.io/badge/FastAPI-API-009688?logo=fastapi)
![License](https://img.shields.io/badge/License-MIT-green)

An end-to-end machine learning project for **credit risk classification**, featuring data preprocessing, feature engineering, model training, experiment tracking with MLflow, and deployment-ready inference APIs using FastAPI.

---

## 📌 Project Overview

This project follows a production-oriented machine learning workflow:

- Data preprocessing and cleaning
- Exploratory Data Analysis (EDA)
- Feature engineering
- Model training and evaluation
- Experiment tracking with MLflow
- Model inference using FastAPI
- Reproducible project structure

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- MLflow
- FastAPI
- Docker

---

## 📂 Project Structure

```text
credit-risk-classification/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── feature_store/
│
├── notebooks/
├── src/
│   ├── data/
│   ├── features/
│   ├── models/
│   ├── training/
│   ├── inference/
│   └── utils/
│
├── api/
├── artifacts/
├── configs/
├── requirements.txt
└── README.md
```

---

## 🚀 Workflow

```text
Raw Data
    │
    ▼
Data Preprocessing
    │
    ▼
Feature Engineering
    │
    ▼
Model Training
    │
    ▼
Model Evaluation
    │
    ▼
MLflow Tracking
    │
    ▼
FastAPI Inference API
```

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/credit-risk-classification.git

cd credit-risk-classification

python -m venv .venv

source .venv/bin/activate      # Linux/macOS
# .venv\Scripts\activate       # Windows

pip install -r requirements.txt
```

---

## ▶️ Run

Train model

```bash
python main.py
```

Start API

```bash
uvicorn api.main:app --reload
```

Launch MLflow UI

```bash
mlflow ui
```

---

## 📈 Features

- End-to-end ML pipeline
- Modular project structure
- Feature engineering pipeline
- MLflow experiment tracking
- FastAPI inference service
- Ready for Docker deployment

---

## 📄 License

This project is licensed under the MIT License.
