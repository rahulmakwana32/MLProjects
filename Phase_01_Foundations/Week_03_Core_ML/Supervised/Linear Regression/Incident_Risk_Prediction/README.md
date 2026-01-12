# ServiceNow Incident Risk Prediction

## 📌 Project Overview
This project demonstrates how to use **Multiple Linear Regression** to predict the **Escalation Risk Score** of ServiceNow incidents.

**Goal:** Identify high-risk tickets *before* they escalate, allowing support managers to take proactive action.

## 📂 Key Features
*   **Synthetic Data Generation**: Creates realistic ServiceNow data (Priority, Reassignments, Age, Sentiment).
*   **Dirty Data Simulation**: Intentionally injects missing values (`NaN`) to demonstrate real-world **Data Cleaning** techniques.
*   **Layman's Interpretation**: Translates complex model coefficients into plain English (e.g., "1 Bounce = +5 Risk Points").
*   **Comprehensive Evaluation**: specific breakdown of **$R^2$** vs **MAE** vs **RMSE**.

## � How to Pull Data from ServiceNow
To get real data for this model, you can use two methods:

### Method 1: Easy Export (CSV)
1.  Go to `Incident > All` in ServiceNow.
2.  Right-click the filter bar and select `Export > CSV`.
3.  **Crucial:** Ensure you include these columns in your view: 
    *   `number` (Incident ID)
    *   `priority`
    *   `reassignment_count` (Bounces)
    *   `calendar_st_duration` (Age/Duration)
    *   `sentiment_score` (if you have an AI Sentiment plugin installed)

### Method 2: REST API (Python)
You can pull data directly into pandas using `requests`:

```python
import requests
import pandas as pd

# 1. Setup credentials
url = 'https://YOUR_INSTANCE.service-now.com/api/now/table/incident'
user = 'admin' 
pwd = 'your_password'

# 2. Define headers and parameters (limit to 1000 records)
headers = {"Content-Type":"application/json","Accept":"application/json"}
params = {
    'sysparm_limit': '1000',
    'sysparm_fields': 'number,priority,reassignment_count,calendar_st_duration'
}

# 3. Request Data
response = requests.get(url, auth=(user,pwd), headers=headers, params=params)

# 4. Convert to DataFrame
if response.status_code == 200:
    data = response.json()['result']
    df = pd.DataFrame(data)
    print("Data loaded successfully!")
else:
    print("Error:", response.status_code)
```

## �🚀 Getting Started

### Prerequisites
You need Python 3 and the following libraries:
*   pandas
*   numpy
*   seaborn
*   matplotlib
*   scikit-learn

### Installation
You can install the required dependencies directly within the notebook or via terminal:

```bash
pip3 install pandas numpy seaborn matplotlib scikit-learn
```

### 🏃‍♂️ Usage
1.  Open `Incident_Risk_Prediction.ipynb` in VS Code or Jupyter Notebook.
2.  Run all cells to see the end-to-end workflow:
    *   **Step 1-2**: Generate data and clean up missing values.
    *   **Step 5**: See the "Decoder Ring" for the coefficients.
    *   **Step 6**: Check the Model Grades ($R^2$, MAE).

## 🧠 Business Logic & Metrics
The model uses synthetic data to simulate a real-world scenario where:
*   **Risk increases** with ticket age and number of reassignments ("bounces").
*   **Risk decreases** with positive sentiment.
