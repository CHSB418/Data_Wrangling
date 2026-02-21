import os

projects = [
    "credit_card_fraud_detection",
    "customer_churn_prediction",
    "stock_price_prediction",
    "predictive_maintenance_iot",
    "insurance_risk_modeling",
    "medical_iot_monitoring",
    "youtube_analytics_prediction",
    "sports_performance_analytics",
    "supply_chain_forecasting",
    "mining_production_optimization",
    "robotics_fault_detection",
    "healthcare_readmission",
    "excel_automation_pipeline",
    "customer_lifetime_value",
    "graph_fraud_detection"
]

base_path = "ml_portfolio_projects"


def write_file(path, content):
    with open(path, "w") as f:
        f.write(content)


requirements = """pandas
numpy
scikit-learn
matplotlib
seaborn
joblib
fastapi
uvicorn
"""

main_code = """from pipelines.training_pipeline import run_pipeline

if __name__ == "__main__":
    run_pipeline()
"""

config_code = """DATA_PATH = "data/raw/data.csv"
MODEL_PATH = "models/model.pkl"
TARGET_COLUMN = "target"
"""

pipeline_code = """from src.data_ingestion import load_data
from src.preprocessing import preprocess
from src.model_training import train_model
from src.evaluation import evaluate
from src.config import TARGET_COLUMN, MODEL_PATH


def run_pipeline():
    df = load_data()
    X_train, X_test, y_train, y_test = preprocess(df, TARGET_COLUMN)
    model = train_model(X_train, y_train, MODEL_PATH)
    evaluate(model, X_test, y_test)
"""

ingestion_code = """import pandas as pd
from src.config import DATA_PATH

def load_data():
    return pd.read_csv(DATA_PATH)
"""

preprocess_code = """from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def preprocess(df, target):
    df = df.drop_duplicates()
    df = df.fillna(df.median(numeric_only=True))

    X = df.drop(columns=[target])
    y = df[target]

    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    return train_test_split(X, y, test_size=0.2, random_state=42)
"""

train_code = """from sklearn.ensemble import RandomForestClassifier
import joblib


def train_model(X_train, y_train, path):
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    joblib.dump(model, path)
    return model
"""

eval_code = """from sklearn.metrics import classification_report


def evaluate(model, X_test, y_test):
    preds = model.predict(X_test)
    print(classification_report(y_test, preds))
"""

readme = """# Enterprise ML Project

End-to-end ML pipeline with preprocessing, training, and evaluation.
"""


def create_project(name):

    project_path = os.path.join(base_path, name)

    folders = [
        "data/raw",
        "data/processed",
        "models",
        "src",
        "pipelines",
        "api",
        "tests"
    ]

    for folder in folders:
        os.makedirs(os.path.join(project_path, folder), exist_ok=True)

    write_file(os.path.join(project_path, "requirements.txt"), requirements)
    write_file(os.path.join(project_path, "main.py"), main_code)
    write_file(os.path.join(project_path, "README.md"), readme)

    write_file(os.path.join(project_path, "src/config.py"), config_code)
    write_file(os.path.join(project_path, "src/data_ingestion.py"), ingestion_code)
    write_file(os.path.join(project_path, "src/preprocessing.py"), preprocess_code)
    write_file(os.path.join(project_path, "src/model_training.py"), train_code)
    write_file(os.path.join(project_path, "src/evaluation.py"), eval_code)

    write_file(os.path.join(project_path, "pipelines/training_pipeline.py"), pipeline_code)


if __name__ == "__main__":

    os.makedirs(base_path, exist_ok=True)

    for project in projects:
        create_project(project)

    print("✅ All projects created successfully!")