import os

# All folders will be created inside the current repo
BASE_PATH = "."  # current folder (Data_Wrangling)

# List of 15 projects
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

# Optional: add basic structure / files for each project
subfolders = ["data", "notebooks", "src", "reports"]

for project in projects:
    project_path = os.path.join(BASE_PATH, project)
    os.makedirs(project_path, exist_ok=True)

    # Create subfolders inside each project
    for sub in subfolders:
        os.makedirs(os.path.join(project_path, sub), exist_ok=True)

    # Optional: create a placeholder main.py file
    main_file = os.path.join(project_path, "main.py")
    if not os.path.exists(main_file):
        with open(main_file, "w") as f:
            f.write(f"# {project} main script\n")
            f.write("print('Hello, world!')\n")

print("✅ All 15 projects created successfully inside the cloned repo!")
