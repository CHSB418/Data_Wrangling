import os

# Base path is the current folder (Data_Wrangling)
BASE_PATH = "."

# 15 project folders
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
    project_path = os.path.join(BASE_PATH, project)
    os.makedirs(project_path, exist_ok=True)  # make sure folder exists

    # Create main.py placeholder
    main_file = os.path.join(project_path, "main.py")
    if not os.path.exists(main_file):
        with open(main_file, "w") as f:
            f.write(f"# {project} main script\n")
            f.write("print('Hello, world!')\n")

print("✅ Placeholder main.py files created in all project folders!")