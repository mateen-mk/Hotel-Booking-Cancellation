import os
from pathlib import Path

list_of_files = [
    # "artifacts/data/raw",
    # "artifacts/data/processed",
    # "artifacts/models",
    # "artifacts/reports/data",
    # "artifacts/reports/model",

    "src/configs/__init__.py",
    "src/data/__init__.py",
    "src/model/__init__.py",
    "src/pipelines/__init__.py",
    "src/mlops/__init__.py",

    "src/core/constants/__init__.py",
    "src/core/entities/__init__.py",
    "src/core/entities/artifact_entity.py",
    "src/core/entities/config_entity.py",
    "src/core/utils/__init__.py",
    "src/core/utils/helpers.py",
    "src/core/logger/__init__.py",
    "src/core/exception/__init__.py",
    
    "notebooks/trails.ipynb",
    "notebooks/figures",

    "settings/schema.yaml",
    
    "docs/architecture.md",
    "docs/api.md",
    "docs/setup.md",
    
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "tests/e2e/__init__.py",
    
    # "deployment/api/__init__.py",
    # "deployment/docker",
    # "deployment/cloud/__init__.py",
        
    "logs",

    "requirements.txt",
    "setup.py",
]

# Create directories and files
for filepath in list_of_files:
    filepath = Path(filepath)
    if filepath.suffix == "":  # If it's a directory
        os.makedirs(filepath, exist_ok=True)
    else:  # If it's a file
        filedir, filename = os.path.split(filepath)
        if filedir:
            os.makedirs(filedir, exist_ok=True)
        if not os.path.exists(filepath):
            with open(filepath, "w") as f:
                pass
