## 1️⃣ **Phase: Project Setup and Initialization**

4. **Document Project Setup**:
   - Create `docs/setup.md` with instructions for setting up the environment and dependencies.

---
### 🪜 **Steps for Phase** 1️⃣

### 1. **Define Objectives**

   - **Problem Statement**: 
     - Hotel bookings are often subject to cancellations, which can cause disruptions in planning and resource allocation. By predicting which bookings are likely to be canceled, hotels can take proactive measures, such as offering incentives to customers or overbooking, to mitigate the impact of cancellations. 
     - The objective of this project is to build a predictive model using features such as booking dates, lead time, customer type, and other relevant factors to classify bookings as `canceled` or `not canceled`.

   - **Evaluation Metrics**:
     - The model's performance will be evaluated using metrics like accuracy, precision, recall, F1 score and ROC curve to ensure its effectiveness in a real-world setting.

### 2. **Set Up Environment**

   - **Install Dependencies**:
      1. **Create a Virtual Environment**:
         - Use `venv` to create a virtual environment for the project:
         ```bash
         python -m venv .venv
         ```
         - Activate the virtual environment:
         - **Windows**:
            ```bash
            .venv\Scripts\activate
            ```
         - **Mac/Linux**:
            ```bash
            source .venv/bin/activate
            ```

      2. **Prepare `requirements.txt`**:
         - Since you might not know all the libraries you'll need upfront, start with the basic libraries commonly used in data science and machine learning:
         ```txt
         pandas
         numpy
         scikit-learn
         matplotlib
         seaborn
         python-dotenv
         ```
         - Install the initial dependencies using:
         ```bash
         pip install -r requirements.txt
         ```

      3. **Add New Dependencies**:
         - As your project progresses, whenever you install a new library, update the `requirements.txt` file using:
         ```bash
         pip freeze > requirements.txt
         ```

   - **Sensitive Credentials**:
      1. **Create a `.env` File**:
         - Store sensitive information like API keys or database credentials in a `.env` file. Example:
         ```
         DATABASE_URL=your_database_url
         API_KEY=your_api_key
         ```

      2. **Load Environment Variables in Code**:
         - Use the `dotenv` package to load these variables securely into your Python code:
         ```python
         from dotenv import load_dotenv
         import os

         # Load .env file
         load_dotenv()

         # Access variables
         database_url = os.getenv("DATABASE_URL")
         api_key = os.getenv("API_KEY")
         ```


### 3. **Prepare Essential Files**

   - **Create `schema.yaml`**  
      - The `schema.yaml` file is used to define the structure and metadata of your dataset. It ensures that the data adheres to the expected format during preprocessing and validation.

      **Steps to Prepare:**
      1. **Identify Features**:
         - List all the features in your dataset, along with their data types and any constraints. For example:
         - Numerical (e.g., `lead_time`, `adults`).
         - Categorical (e.g., `hotel`, `customer_type`).
         - Boolean (e.g., `is_canceled`).
         - Date/Time (e.g., `reservation_status_date`).

      2. **Write the File**:
         - Use the following YAML structure:
         ```yaml
         features:
            lead_time:
               type: numerical
               description: "Number of days between booking and check-in."
            hotel:
               type: categorical
               description: "Type of hotel (Resort or City)."
            is_canceled:
               type: boolean
               description: "Whether the booking was canceled (1: Yes, 0: No)."
            reservation_status_date:
               type: datetime
               description: "Date of the last reservation status."
         ```

      3. **Save**:
         - Save this file as `schema.yaml` in the `config/` folder.
   
   - **Create `Makefile`**
      - A `Makefile` helps automate common tasks like setting up the environment, preprocessing data, and training models.

      **Steps to Prepare:**
      1. **Identify Key Tasks**:
         - Define common tasks you’ll perform frequently. Examples:
         - Setting up the environment.
         - Running data preprocessing.
         - Training the model.

      2. **Write the File**:
         - Use the following structure for the `Makefile`:
         ```makefile
         # Install dependencies
         setup:
            pip install -r requirements.txt

         # Run data preprocessing
         preprocess:
            python src/preprocess.py

         # Train the model
         train:
            python src/train.py

         # Test the code
         test:
            pytest tests/

         # Run the entire pipeline
         pipeline: setup preprocess train test
         ```

      3. **Save**:
         - Save this file as `Makefile` in the root of your project.

### 4. **Document Project Setup**
   - **Create `docs/setup.md`**:
     - Document the setup process, such as installing dependencies, setting up the environment, and running the project.
 
---
