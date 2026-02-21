import os

# Base path: current folder (Data_Wrangling repo)
BASE_PATH = "."

# 15 projects with short descriptions (you can edit later)
projects = {
    "credit_card_fraud_detection": "Detect fraudulent credit card transactions using machine learning.",
    "customer_churn_prediction": "Predict customer churn for businesses to improve retention.",
    "stock_price_prediction": "Predict future stock prices using historical data and AI models.",
    "predictive_maintenance_iot": "Use IoT sensor data to predict machine failures in advance.",
    "insurance_risk_modeling": "Analyze insurance risk and calculate premiums using data science.",
    "medical_iot_monitoring": "Monitor patient health data from IoT devices for early warning.",
    "youtube_analytics_prediction": "Predict video performance metrics on YouTube channels.",
    "sports_performance_analytics": "Analyze and predict athlete performance using sports data.",
    "supply_chain_forecasting": "Forecast supply chain demand and optimize logistics.",
    "mining_production_optimization": "Optimize mining operations using production data analysis.",
    "robotics_fault_detection": "Detect faults in robotic actuators and sensors automatically.",
    "healthcare_readmission": "Predict hospital readmissions to improve patient care.",
    "excel_automation_pipeline": "Automate Excel data pipelines for enterprise workflows.",
    "customer_lifetime_value": "Calculate and predict customer lifetime value for businesses.",
    "graph_fraud_detection": "Detect fraud patterns in graph-based network data."
}

# Standard subfolders per project
subfolders = ["data/raw", "data/processed", "notebooks", "src", "reports"]

for project, description in projects.items():
    project_path = os.path.join(BASE_PATH, project)
    os.makedirs(project_path, exist_ok=True)

    # Create all subfolders
    for sub in subfolders:
        os.makedirs(os.path.join(project_path, sub), exist_ok=True)

    # Create README.md with description
    readme_file = os.path.join(project_path, "README.md")
    with open(readme_file, "w") as f:
        f.write(f"# {project}\n\n")
        f.write(f"{description}\n\n")
        f.write("## Project Structure\n")
        f.write("- data/raw : Raw datasets\n")
        f.write("- data/processed : Cleaned and processed data\n")
        f.write("- notebooks : Jupyter notebooks\n")
        f.write("- src : Python scripts\n")
        f.write("- reports : Analysis reports or output\n")

    # Create placeholder main.py in src/
    main_file = os.path.join(project_path, "src", "main.py")
    with open(main_file, "w") as f:
        f.write(f"# {project} main script\n")
        f.write("print('Hello, world!')\n")

    # Create placeholder notebook
    notebook_file = os.path.join(project_path, "notebooks", "example.ipynb")
    if not os.path.exists(notebook_file):
        with open(notebook_file, "w") as f:
            f.write("{\n \"cells\": [],\n \"metadata\": {},\n \"nbformat\": 4,\n \"nbformat_minor\": 5\n}")

print("✅ All 15 projects created with professional structure and tracked files!")