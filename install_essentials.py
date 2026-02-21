import subprocess
import sys

# List of essential packages for multiple roles
packages = [
    # Software / App Dev
    "flask", "django", "fastapi", "requests", "beautifulsoup4",

    # Testing / QA / Automation
    "pytest", "selenium", "robotframework", "coverage",

    # Data Engineering / Data Science / AI & ML
    "pandas", "numpy", "scikit-learn", "matplotlib", "seaborn",
    "jupyter", "nbformat", "tensorflow", "torch", "xgboost", "lightgbm",

    # Cloud / DevOps / SRE
    "boto3", "azure-mgmt-resource", "google-cloud-storage", "docker", "kubernetes"
]

def install(package):
    print(f"⚡ Installing {package} ...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def check_and_install(package):
    try:
        __import__(package)
        print(f"✅ {package} is already installed")
    except ImportError:
        # Special case for some packages where import name != pip name
        special_import_names = {
            "google-cloud-storage": "google.cloud.storage",
            "azure-mgmt-resource": "azure.mgmt.resource",
            "torch": "torch",
            "xgboost": "xgboost",
            "lightgbm": "lightgbm",
        }
        import_name = special_import_names.get(package, package)
        try:
            __import__(import_name)
            print(f"✅ {package} is already installed")
        except ImportError:
            install(package)

if __name__ == "__main__":
    print("🚀 Checking and installing essential Python packages...")
    for pkg in packages:
        check_and_install(pkg)
    print("🎉 All essential packages are ready!")