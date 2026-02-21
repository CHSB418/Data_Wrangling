import os
import pandas as pd
import numpy as np

BASE_PATH = "."  # Data_Wrangling repo

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

for project in projects:
    raw_path = os.path.join(BASE_PATH, project, "data", "raw")
    processed_path = os.path.join(BASE_PATH, project, "data", "processed")
    os.makedirs(raw_path, exist_ok=True)
    os.makedirs(processed_path, exist_ok=True)

    # Create small sample datasets depending on project type
    if project == "credit_card_fraud_detection":
        df = pd.DataFrame({
            "transaction_id": range(1, 11),
            "amount": np.random.randint(10, 1000, 10),
            "is_fraud": np.random.randint(0, 2, 10)
        })
    elif project == "customer_churn_prediction":
        df = pd.DataFrame({
            "customer_id": range(1, 11),
            "tenure": np.random.randint(1, 36, 10),
            "churn": np.random.randint(0, 2, 10)
        })
    elif project == "stock_price_prediction":
        df = pd.DataFrame({
            "date": pd.date_range("2026-01-01", periods=10),
            "stock_price": np.round(np.random.uniform(100, 500, 10), 2)
        })
    elif project == "predictive_maintenance_iot":
        df = pd.DataFrame({
            "machine_id": range(1, 6),
            "temperature": np.random.uniform(30, 100, 5),
            "vibration": np.random.uniform(0, 1, 5),
            "failure": np.random.randint(0, 2, 5)
        })
    elif project == "insurance_risk_modeling":
        df = pd.DataFrame({
            "policy_id": range(1, 11),
            "age": np.random.randint(18, 70, 10),
            "premium": np.random.randint(100, 1000, 10),
            "claim": np.random.randint(0, 2, 10)
        })
    elif project == "medical_iot_monitoring":
        df = pd.DataFrame({
            "patient_id": range(1, 6),
            "heart_rate": np.random.randint(60, 120, 5),
            "blood_pressure": np.random.randint(100, 160, 5)
        })
    elif project == "youtube_analytics_prediction":
        df = pd.DataFrame({
            "video_id": range(1, 11),
            "views": np.random.randint(1000, 50000, 10),
            "likes": np.random.randint(100, 5000, 10)
        })
    elif project == "sports_performance_analytics":
        df = pd.DataFrame({
            "athlete_id": range(1, 6),
            "speed": np.random.uniform(10, 30, 5),
            "score": np.random.randint(0, 100, 5)
        })
    elif project == "supply_chain_forecasting":
        df = pd.DataFrame({
            "item_id": range(1, 11),
            "demand": np.random.randint(50, 500, 10)
        })
    elif project == "mining_production_optimization":
        df = pd.DataFrame({
            "mine_id": range(1, 6),
            "output_tons": np.random.randint(100, 1000, 5)
        })
    elif project == "robotics_fault_detection":
        df = pd.DataFrame({
            "robot_id": range(1, 6),
            "temperature": np.random.uniform(20, 100, 5),
            "error_code": np.random.randint(0, 5, 5)
        })
    elif project == "healthcare_readmission":
        df = pd.DataFrame({
            "patient_id": range(1, 11),
            "days_since_last_visit": np.random.randint(1, 365, 10),
            "readmitted": np.random.randint(0, 2, 10)
        })
    elif project == "excel_automation_pipeline":
        df = pd.DataFrame({
            "record_id": range(1, 11),
            "value": np.random.randint(100, 1000, 10)
        })
    elif project == "customer_lifetime_value":
        df = pd.DataFrame({
            "customer_id": range(1, 11),
            "purchase_total": np.random.randint(100, 5000, 10)
        })
    elif project == "graph_fraud_detection":
        df = pd.DataFrame({
            "node_id": range(1, 11),
            "connected_to": np.random.randint(1, 11, 10),
            "is_fraud": np.random.randint(0, 2, 10)
        })
    else:
        df = pd.DataFrame()

    # Save CSV files
    df.to_csv(os.path.join(raw_path, "sample_data.csv"), index=False)
    df.to_csv(os.path.join(processed_path, "sample_data.csv"), index=False)

print("✅ Sample datasets created for all 15 projects!")