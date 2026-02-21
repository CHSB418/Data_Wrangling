import os

BASE_PATH = "."  # current folder (data_wrangling)

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
    path = os.path.join(BASE_PATH, project)
    os.makedirs(path, exist_ok=True)
    print(f"Created folder: {path}")