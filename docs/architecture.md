# 🏠 **Hotel Booking Cancellation Prediction - Architecture**

## 🔍 **Overview**
The objective of this project is to build an end-to-end machine learning pipeline to predict the likelihood of hotel booking cancellations. The pipeline is scalable, modular, and deployable in a production environment.  

It integrates modern tools and practices such as:
- **Evidently.ai**: For automated data validation, drift detection, and generating data quality reports.
- **DVC**: For versioning data and model artifacts.
- **MLflow**: For experiment tracking and model lifecycle management.
- **GitHub Actions**: For CI/CD automation.
- **AWS**: For cloud-based storage and deployment.

---

## 🔄 **Workflow Overview**

### **End-to-End Workflow**
```plaintext
Data Ingestion --> Data Validation --> Data Versioning --> Data Preprocessing --> Feature Engineering --> 
Model Training --> Experiment Tracking --> Model Evaluation --> Model Deployment
```

### **Tools in Workflow**
| Stage                     | Tools/Frameworks                       |
|---------------------------|----------------------------------------|
| Data Ingestion            | MySQL, Pandas                          |
| Data Validation           | Evidently.AI                           |
| Data Versioning           | DVC (with AWS S3 backend)              |
| Data Preprocessing        | Pandas, NumPy                          |
| Feature Engineering       | Scikit-learn, Custom Transformers      |
| Model Training            | Scikit-learn, XGBoost                  |
| Experiment Tracking       | MLflow (local or remote server)        |
| Deployment                | Flask, Docker, AWS (EC2, Lambda)       |
| CI/CD Automation          | GitHub Actions                         |

---

## ⚙️ **Components and Responsibilities**

1. **Data Layer**:
   - **Ingestion**: Fetch raw data from MySQL using `src/data/ingest.py`.
   - **Validation**: Validate schema and data quality using `configs/schema.yaml`.
   - **Versioning**: Track raw and processed data versions with **DVC** (backend: AWS S3).

2. **Feature Layer**:
   - **Transformation**: Handle missing values, outliers, and standardize data using custom pipelines in `src/features/transformers.py`.
   - **Feature Engineering**: Extract meaningful features such as:
     - Day of the week from booking date.
     - Whether the booking is during the peak season.
     - Customer type encoding.

3. **Modeling Layer**:
   - Train multiple machine learning models with a modular approach (`src/models/train.py`).
   - Save the best-performing model using **MLflow** with hyperparameters and metrics tracked.

4. **Deployment Layer**:
   - Develop an API in Flask (`deploy/api/`) for serving predictions.
   - Package the app into a Docker container (`deploy/docker/`) for portability.
   - Deploy the application to AWS EC2 or AWS Lambda.

5. **CI/CD Automation**:
   - Use **GitHub Actions** to automate:
     - Linting and code quality checks.
     - Unit and integration tests.
     - Deployment to cloud environments.

---

## 📂 **Folder Structure**
<details>
<summary>🔍 Click to expand the folder structure</summary>

```plaintext
├── data
│   ├── raw              # Raw data from MySQL
│   ├── interim          # Intermediate processed data
│   ├── processed        # Final preprocessed data
│   ├── external         # External data sources
│   ├── features         # Feature engineering output
├── src
│   ├── data             # Scripts for data ingestion and validation
│   ├── features         # Scripts for data transformation and feature engineering
│   ├── models           # Scripts for model training and evaluation
│   ├── pipelines        # End-to-end pipeline orchestration
│   ├── predict          # Scripts for making predictions
│   ├── evaluation       # Model evaluation scripts
│   ├── utils            # Helper functions and utilities
│   ├── visualization    # Scripts for creating plots
├── deploy
│   ├── api              # Flask API for prediction
│   ├── docker           # Dockerfiles for containerization
│   ├── cloud            # Deployment scripts for AWS
├── configs              # YAML configuration files
├── notebooks            # Jupyter notebooks for experimentation
├── tests                # Unit, integration, and e2e tests
├── trained_models       # Serialized models (managed by DVC)
├── reports              # Figures and tables for reporting
├── logs                 # Logs for pipelines and app
├── docs                 # Documentation (architecture, setup, API)
```
</details>

---

## 💧 **Data Flow**

1. **Data Ingestion**:
   - Fetch raw booking data from MySQL using credentials stored in `.env`.
   - Store raw data in `data/raw/`.

2. **Data Validation**:
   - Validate data schema using `configs/schema.yaml` and Pydantic.
   - Log any discrepancies in `logs/pipeline_logs`.

3. **Data Preprocessing**:
   - Handle missing values and outliers.
   - Store cleaned data in `data/processed/`.

4. **Data Versioning**:
   - Use DVC to version raw, interim, and processed data.
   - Store data files on AWS S3 for scalability.

5. **Modeling**:
   - Train models with hyperparameter tuning tracked by MLflow.
   - Save the best model in `trained_models/`.

6. **Deployment**:
   - Serve predictions via Flask API.
   - Deploy the API to AWS (EC2 or Lambda) using Docker.

---

## 🤖 **Integration of Advanced Tools**

### **Data Validation**
- **Tool**: [Evidently.ai](https://evidentlyai.com/)  
- **Purpose**: Perform automated data validation and generate data quality reports. It helps ensure data consistency, identify missing values, and detect potential drifts in data distribution.
- **Workflow**:
  1. **Data Quality Check**: Validate data schema and identify anomalies in the raw dataset.
  2. **Drift Detection**: Monitor for data drift by comparing new data with historical data.
  3. **Integration**: Use Evidently’s Python API in the pipeline to generate visual reports or JSON outputs for logging.

### **DVC (Data Version Control)**
- **Purpose**: Manage and version control data, features, and model artifacts.
- **Setup**:
  - Initialize: `dvc init`
  - Add remote storage (AWS S3): `dvc remote add -d s3remote s3://your-bucket-name`
  - Track files: `dvc add data/raw/`

### **MLflow**
- **Purpose**: Track experiments, register models, and manage the model lifecycle.
- **Integration**:
  - Start MLflow tracking server locally or remotely.
  - Log metrics and models during training:
    ```python
    import mlflow
    with mlflow.start_run():
        mlflow.log_param("model", "XGBoost")
        mlflow.log_metric("accuracy", accuracy)
        mlflow.sklearn.log_model(model, "model")
    ```

### **GitHub Actions**
- **Purpose**: Automate CI/CD processes.
- **Sample Workflow** (`.github/workflows/main.yml`):
  ```yaml
  name: CI/CD Pipeline

  on:
    push:
      branches:
        - main

  jobs:
    build-and-test:
      runs-on: ubuntu-latest

      steps:
        - name: Checkout repository
          uses: actions/checkout@v3
          
        - name: Set up Python
          uses: actions/setup-python@v4
          with:
            python-version: '3.8'

        - name: Install dependencies
          run: pip install -r requirements.txt

        - name: Run tests
          run: pytest tests/
  ```

### **AWS**
- **Purpose**: Cloud storage and deployment.
- **Components**:
  - **S3**: Store raw and processed data, models, and logs.
  - **EC2**: Host the Flask API for production.
  - **Lambda**: Serverless deployment for lightweight predictions.
  - **IAM**: Set up roles and permissions for secure cloud access.

---

## ✨ **Future Enhancements**
1. **AutoML Integration**: Automate model selection and hyperparameter tuning.
2. **Data Drift Monitoring**: Set up monitoring for model performance degradation.
3. **Advanced Deployment**:
   - Use Kubernetes for scaling.
   - Transition to serverless ML pipelines (AWS Step Functions).
