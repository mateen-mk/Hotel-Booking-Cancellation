import os
from pathlib import Path

list_of_files = [
    "data/raw/.gitkeep",
    "data/interim/.gitkeep",
    "data/processed/.gitkeep",
    "data/external/.gitkeep",
    "data/features/.gitkeep",

    "src/data/__init__.py",
    "src/features/__init__.py",
    "src/models/__init__.py",
    "src/pipelines/__init__.py",
    "src/predict/__init__.py",
    "src/evaluation/__init__.py",
    "src/utils/__init__.py",
    "src/utils/helpers.py",
    "src/constants/__init__.py",
    "src/entities/__init__.py",
    "src/entities/config_entity.py",
    "src/entities/artifact_entity.py",
    "src/initializers/__init__.py",
    "src/initializers/initializers.py",
    "src/visualization/__init__.py",
    "src/visualization/plot_creator.py",
    
    "trained_models/.gitkeep",
    
    "configs/schema.yaml",
    
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "tests/e2e/__init__.py",
    
    "deploy/api/__init__.py",
    "deploy/docker/Dockerfile",
    "deploy/cloud/__init__.py",
    
    "reports/figures/.gitkeep",
    "reports/tables/.gitkeep",
    
    "notebooks/trails.ipynb",
    
    "logs/pipeline_logs/.gitkeep",
    "logs/app_logs/.gitkeep",
    
    "docs/architecture.md",
    "docs/api.md",
    "docs/setup.md",
    
    "requirements.txt",
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
