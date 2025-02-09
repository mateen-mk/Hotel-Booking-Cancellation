# 🏨 Hotel Booking Cancellation Prediction System 🌟  

<div align="center">
  <img src="https://5.imimg.com/data5/EF/GO/MY-17287433/hotel-bookings-500x500.jpg" alt="Hotel Banner" width="1000"/><br>

*Empowering hotels to predict cancellations and optimize their operations!*
</div>

--- 

## 📖 **Overview**  
The **Hotel Booking Cancellation Prediction System** is an end-to-end machine learning solution designed to forecast whether a hotel booking will be canceled. This system helps hotels improve revenue management, streamline operations, and plan resources effectively. It uses historical booking data to train models that predict cancellations, and it comes with a robust, modular pipeline that covers every step from data ingestion to model deployment.

---

**❓ Problem Statement**  
<div align="center">
  <img src="notebooks/figures/EDA/Cancellation_status.png" alt="Cancellation Analysis"/>
</div>

Hotels face significant challenges due to last-minute booking cancellations 🚫, leading to revenue loss and inefficient resource management. This system predicts whether a booking will be canceled, empowering hotels to optimize pricing 🏷️, staffing 👥, and inventory 📦.  

**✨ Solution**  
A **machine learning-powered pipeline** that:  
🔹 Processes historical booking data  
🔹 Detects patterns and predicts cancellations  
🔹 Generates actionable insights through easy-to-understand visuals  

---

## 🚀 **Key Features**  
- **Automated Data Pipelines** 📊: From raw data to predictions, fully automated!  
- **Smart Preprocessing** 🧹: Handles missing values, outliers, and data drift.  
- **Model Zoo** 🤖: Trains and compares 5+ ML models (Random Forest, XGBoost, etc.).  
- **Visual Reports** 📈: Interactive charts for decision-makers.  
- **One-Click Deployment** 🚢: Docker and Streamlit support.  

---

## 💡 Key Features

- **Data Ingestion & Validation**  
  📥 Automatically fetches and validates raw booking data from a MySQL database.
  
- **Data Preprocessing**  
  🔍 Cleans and transforms data (handles missing values, encoding, normalization) for accurate predictions.
  
- **Model Training & Evaluation**  
  🏋️‍♂️ Trains multiple models with hyperparameter tuning to select the best performer, and evaluates them using robust metrics.
  
- **Model Deployment**  
  🌐 Deploys the trained model via an interactive web application (using Flask/Streamlit) for real-time predictions.
  
- **MLOps Integration**  
  🔧 Implements versioning, monitoring (data drift, performance), and automated workflows for continuous improvement.
  
- **Interactive Notebooks**  
  📊 Jupyter notebooks document every stage of the pipeline with visualizations and detailed analyses.

---

## 🗂️ Project Structure

```plaintext

├── 📁 artifacts/                   # Auto-generated artifacts (ignored in Git)
│   ├── 📁 data/                    # Datasets
│   │   ├── 📁 interim/             # Interim data (e.g., data.csv)
│   │   ├── 📁 processed/           # Preprocessed data (e.g., processed.csv)
│   │   ├── 📁 raw/                 # Raw data (e.g., raw.csv)
│   │   └── 📁 splitted/            # Train, test splits (train.csv, test.csv)
│   ├── 📁 objects/                 # Saved objects & models
│   │   ├── 📁 model/               # Trained model (model.pkl)
│   │   └── 📁 preprocessor/        # Preprocessing object (preprocessor.pkl)
│   └── 📁 reports/                 # Evaluation, metrics, and drift reports
│       ├── 📁 evaluation/          # Model evaluation reports (report.json)
│       ├── 📁 metrics/             # Metrics files (metrics.json)
│       ├── 📁 params/              # Hyperparameter configurations (params.json)
│       └── 📁 validation/          # Data validation reports (drift_report.yaml)
│
├── 📁 docs/                        # Documentation
│   ├── 📄 api.md                   # API documentation
│   ├── 📄 architecture.md          # System architecture
│   ├── 📄 project_plan.md          # Project planning & roadmap
│   ├── 📄 setup.md                 # Setup instructions
│   └── 📄 workflow.md              # Detailed workflow description
│
├── 📁 logs/                        # Log files for debugging and monitoring
│
├── 📁 notebooks/                   # Jupyter notebooks for experimentation
│   ├── 📁 figures/                 # Visualizations & charts
│   │   ├── 📁 data_preprocessing/  # Figures for data preprocessing
│   │   ├── 📁 EDA/                 # Exploratory Data Analysis figures
│   │   └── 📁 model_training/      # Figures from model training (feature importance, model comparison)
│   ├── 📘 01-fetch_data.ipynb      # Data fetching demonstration
│   ├── 📘 02-EDA.ipynb             # Exploratory Data Analysis
│   ├── 📘 03-data_preprocessing.ipynb  # Data preprocessing steps
│   ├── 📘 04-model_building.ipynb  # Model training and evaluation
│   └── 📘 trails.ipynb             # Additional experiments
│
├── 📁 settings/                    # Configuration files
│   ├── ⚙️ model.yaml               # Model settings and hyperparameters
│   └── ⚙️ schema.yaml              # Data schema definition
│
├── 📁 src/                         # Source code
│   ├── 📁 configs/                # Configuration related code (e.g., MySQL connection)
│   ├── 📁 core/                   # Core utilities, logger, exceptions, constants, etc.
│   │   ├── 📁 constants/           # Constants to use throughout the project
│   │   ├── 📁 entities/            # Entities (artifact_entities, config_entities)
│   │   ├── 📁 exceptions/          # Custom exceptions
│   │   ├── 📁 logger/              # Custom Logging 
│   │   └── 📁 utils/               # General utility functions
│   ├── 📁 data/                   # Data ingestion, preprocessing, validation, etc.
│   │   ├── 📜 data_ingestion.py    # Data ingestion script
│   │   ├── 📜 data_preprocessing.py  # Data preprocessing script
│   │   ├── 📜 data_split.py        # Data Splitting script (train, test)
│   │   └── 📜 data_validation.py   # Data validation script
│   ├── 📁 mlops/                  # MLOps scripts (monitoring, deployment, versioning, CI/CD)
│   ├── 📁 model/                  # Model training, evaluation, prediction, validation
│   │   ├── 📜 model_evaluation.py  # Model Evaluation script
│   │   ├── 📜 model_trainer.py     # Model Training script
│   │   ├── 📜 model_validation.py  # Model Validation script
│   │   └── 📜 predictor.py         # Model Prediction script
│   └── 📁 pipelines/              # Workflow orchestration for data & model pipelines
│       ├── 📜 data_pipeline.py     # Data Pipeline to Handle src/data/ scripts
│       ├── 📜 model_pipeline.py    # Model Pipeline to Handle src/model/ scripts
│       └── 📜 run_pipe.py          # Workflow orchestration for data & model pipelines
│
├── 📁 tests/                       # Unit and integration tests
│
├── ⚙️ main.py                     # Main entry point to run the pipeline
├── 📄 Makefile                    # Build and automation commands
├── 📄 LICENSE
├── 📄 README.md                   # Project documentation (this file)
└── 📄 requirements.txt            # Python dependencies
```

> **Note**: The `artifacts` folder (auto-generated files) is excluded via `.gitignore`.

---

## 🔍 **Exploratory Data Analysis (EDA)**  
We analyzed **100,000+ bookings** to uncover trends, some of them are following:  
- 🗺️ **Guest Origins**: Most guests come from Portugal and Europe. 

  ![Country Distribution](notebooks/figures/EDA/Country_wise_guests.png)

- 📅 **Booking Patterns**: 

  ![Monthly Distribution](notebooks/figures/EDA/Guest_distribution_over_month.png)

- 💰 **Pricing Insights**:

  ![Price Trends](notebooks/figures/EDA/Room_price_per_night_over_monts.png)  

---

## 🤖 **Model Training & Evaluation**  
### **Performance Highlights**  
| Model           | Accuracy | Precision | Recall | F1 Score | AUC Score |
|-----------------|----------|-----------|--------|----------|-----------|
| Random Forest   |   86%    |    81%    |  80%   |    80%   |    93%    |
| XGBoost         |   85%    |    84%    |  72%   |    78%   |    91%    |

- **Model Comparison**:

  ![Model Comparison](notebooks/figures/model_training/model_comparison/Accuracy.png)  

---

## 🛠️ **Getting Started**  
### **Prerequisites**  
- Python 3.8+ 🐍  
- MySQL (for raw data) 🗃️  

### **Installation**  
1. Clone the repo:  
   ```bash
   git clone https://github.com/yourusername/hotel-booking-cancellation.git
   cd hotel-booking-cancellation
   ```
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```
3. Configure `.env` with your database credentials.  

### **Run the Pipeline**  
```bash
python main.py  # Trains models and generates artifacts!
```

---

## 🧩 **Technologies Used**  
- **Backend**: Python, Scikit-learn, XGBoost  
- **Data Processing**: Pandas, NumPy  
- **Visualization**: Matplotlib, Seaborn  
- **Deployment**: Flask, Docker  

---

## 🌈 **Future Improvements**  
- 🕵️ **Real-Time Monitoring**: Track model performance live.  
- 📱 **Mobile App**: Notify staff about high-risk cancellations.  
- 🌍 **Multi-Hotel Support**: Scale for hotel chains.  

---

## 👥 **Contributors**  
- **Your Name** 👩💻 - [LinkedIn](https://linkedin.com/in/yourprofile) | [Email](mailto:you@example.com)  

**Made with ❤️ for stress-free hotel management!**  

---

<div align="center">
  <img src="notebooks/figures/data_preprocessing/heatmap.png" alt="Data Correlation" width="600"/>
</div>