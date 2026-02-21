import os
import subprocess
from datetime import datetime
import pandas as pd
import numpy as np
import nbformat as nbf

# ------------------------
# Settings
# ------------------------
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
subfolders = ["data/raw", "data/processed", "notebooks", "src", "reports"]

# ------------------------
# 1. Create Project Folders
# ------------------------
for project in projects:
    for sub in subfolders:
        path = os.path.join(BASE_PATH, project, sub)
        os.makedirs(path, exist_ok=True)
    # main.py placeholder
    main_file = os.path.join(BASE_PATH, project, "src", "main.py")
    if not os.path.exists(main_file):
        with open(main_file, "w") as f:
            f.write(f"# {project} main script\nprint('Hello world from {project}')\n")

print("✅ Project folders and main.py files created.")

# ------------------------
# 2. Create Sample Datasets
# ------------------------
for project in projects:
    raw_path = os.path.join(BASE_PATH, project, "data", "raw", "sample_data.csv")
    processed_path = os.path.join(BASE_PATH, project, "data", "processed", "sample_data.csv")

    # Example small datasets
    if project == "credit_card_fraud_detection":
        df = pd.DataFrame({"transaction_id": range(1,11), "amount": np.random.randint(10,1000,10), "is_fraud": np.random.randint(0,2,10)})
    elif project == "customer_churn_prediction":
        df = pd.DataFrame({"customer_id": range(1,11), "tenure": np.random.randint(1,36,10), "churn": np.random.randint(0,2,10)})
    elif project == "stock_price_prediction":
        df = pd.DataFrame({"date": pd.date_range("2026-01-01", periods=10), "stock_price": np.round(np.random.uniform(100,500,10),2)})
    else:
        df = pd.DataFrame({"id": range(1,11), "value": np.random.randint(1,100,10)})

    df.to_csv(raw_path, index=False)
    df.to_csv(processed_path, index=False)

print("✅ Sample datasets created.")

# ------------------------
# 3. Create Example Notebooks
# ------------------------
for project in projects:
    notebook_path = os.path.join(BASE_PATH, project, "notebooks", "template.ipynb")
    nb = nbf.v4.new_notebook()
    nb.cells.append(nbf.v4.new_markdown_cell(f"# {project} Example Notebook\nEDA and placeholder ML code"))
    nb.cells.append(nbf.v4.new_code_cell(
        "import pandas as pd\nimport matplotlib.pyplot as plt\nimport seaborn as sns\nsns.set()"
    ))
    nb.cells.append(nbf.v4.new_code_cell(
        "raw_file = '../data/raw/sample_data.csv'\ndf = pd.read_csv(raw_file)\ndf.head()"
    ))
    nb.cells.append(nbf.v4.new_code_cell(
        "df.hist(figsize=(8,6))\nplt.show()"
    ))
    nb.cells.append(nbf.v4.new_code_cell(
        "# Placeholder ML\nif 'is_fraud' in df.columns:\n    from sklearn.model_selection import train_test_split\n    from sklearn.ensemble import RandomForestClassifier\n    X = df.drop('is_fraud', axis=1)\n    y = df['is_fraud']\n    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=42)\n    model=RandomForestClassifier()\n    model.fit(X_train,y_train)\n    print('Accuracy:', model.score(X_test,y_test))"
    ))
    with open(notebook_path, "w", encoding="utf-8") as f:
        nbf.write(nb, f)

print("✅ Example notebooks created.")

# ------------------------
# 4. Autopush to GitHub
# ------------------------
os.chdir(BASE_PATH)

def git(cmd):
    return subprocess.run(["git"] + cmd, capture_output=True, text=True).stdout.strip()

status = git(["status", "--porcelain"])
if not status:
    print("✅ Repo is up-to-date. Nothing to commit.")
else:
    git(["add", "."])
    commit_msg = f"Auto-build: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    git(["commit", "-m", commit_msg])
    push_result = git(["push", "origin", "main"])
    print("🚀 Changes pushed to GitHub:\n", push_result)