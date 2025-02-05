# **Project Setup Guide**

This document provides detailed instructions to set up the project environment, install dependencies, and run the project.

---

## **1️⃣ Prerequisites**

Ensure you have the following software installed on your system:

- Python (version 3.8 or above)
- Git
- pip (Python package manager)

---

## **2️⃣ Clone the Repository**

1. Open a terminal and navigate to the directory where you want to store the project.
2. Clone the repository using the following command:
   ```bash
   git clone https://github.com/mateen-mk/Hotel-Booking-Cancellation.git
   ```
3. Navigate to the project folder:
   ```bash
   cd Hotel-Booking-Cancellation
   ```

---

## **3️⃣ Set Up Virtual Environment**

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```
2. Activate the virtual environment:
   - **Windows**:
     ```bash
     .venv\Scripts\activate
     ```
   - **Mac/Linux**:
     ```bash
     source .venv/bin/activate
     ```

---

## **4️⃣ Install Dependencies**

Install the required Python libraries:
```bash
pip install -r requirements.txt
```

---

## **5️⃣ Configure Environment Variables**

1. Create a `.env` file in the project root directory.
2. Add the necessary environment variables. For example:
   ```
   DATABASE_URL=your_database_url
   ```
3. These variables will be loaded into the project during runtime.

---

## **6️⃣ Understand the Project Structure**

Here is an overview of the project folder structure:

```plaintext
├── config/
│   └── schema.yaml        # Dataset schema definition
├── docs/
│   └── setup.md           # Project setup instructions
├── src/
│   ├── preprocess.py      # Data preprocessing scripts
│   ├── train.py           # Model training script
├── tests/                 # Unit tests for the project
├── requirements.txt       # Python dependencies
├── Makefile               # Automation commands
└── .env                   # Environment variables
```

---


## **9️⃣ Push Code to Git**

You can use the `Makefile` to commit and push code changes. Run:
```bash
make git-push msg="your message"
```
The changes will be pushed to the `main` branch.

---



Update this setup.md