import os
import nbformat as nbf

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
    notebook_path = os.path.join(BASE_PATH, project, "notebooks", "template.ipynb")
    os.makedirs(os.path.dirname(notebook_path), exist_ok=True)

    nb = nbf.v4.new_notebook()

    # Add title cell
    nb.cells.append(nbf.v4.new_markdown_cell(f"# {project} - Example Notebook\nThis notebook demonstrates basic data loading, EDA, and a placeholder ML pipeline."))

    # Add code cell: import libraries
    nb.cells.append(nbf.v4.new_code_cell(
        "import pandas as pd\n"
        "import matplotlib.pyplot as plt\n"
        "import seaborn as sns\n"
        "sns.set()\n"
    ))

    # Add code cell: load dataset
    nb.cells.append(nbf.v4.new_code_cell(
        "raw_file = '../data/raw/sample_data.csv'\n"
        "processed_file = '../data/processed/sample_data.csv'\n"
        "df_raw = pd.read_csv(raw_file)\n"
        "df_processed = pd.read_csv(processed_file)\n"
        "df_raw.head()"
    ))

    # Add code cell: basic EDA
    nb.cells.append(nbf.v4.new_code_cell(
        "print('Raw Data Info:')\n"
        "print(df_raw.info())\n\n"
        "print('Summary Statistics:')\n"
        "print(df_raw.describe())\n\n"
        "df_raw.hist(figsize=(10,8))\n"
        "plt.show()"
    ))

    # Add code cell: placeholder ML code
    nb.cells.append(nbf.v4.new_code_cell(
        "# Placeholder ML pipeline\n"
        "from sklearn.model_selection import train_test_split\n"
        "from sklearn.ensemble import RandomForestClassifier\n"
        "\n"
        "# This is just an example; update target and features accordingly\n"
        "if 'is_fraud' in df_raw.columns:\n"
        "    X = df_raw.drop('is_fraud', axis=1)\n"
        "    y = df_raw['is_fraud']\n"
        "    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)\n"
        "    model = RandomForestClassifier()\n"
        "    model.fit(X_train, y_train)\n"
        "    print('Accuracy:', model.score(X_test, y_test))\n"
        "else:\n"
        "    print('No ML target defined; please update notebook for your project.')"
    ))

    # Write notebook
    with open(notebook_path, "w", encoding="utf-8") as f:
        nbf.write(nb, f)

print("✅ Example notebooks created for all 15 projects!")