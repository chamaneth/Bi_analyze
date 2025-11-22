# Bi_Analyze Dashboard 🚀

**My first Power BI project!** Previously, I worked with Looker, but this is my first hands-on Power BI dashboard.  
It visualizes daily COVID-19 cases across Sri Lanka’s districts.

---

## 📊 Dashboard Highlights
- **Line Chart:** Daily trend of COVID-19 cases  
- **Bar Chart:** District-wise total cases  
- **KPI Cards:** Total | Average | Max daily cases  
- **Optional:** 7-day moving average for trend smoothing  

---

## 🖼 Screenshots
<img width="1359" height="685" alt="Dashboard Screenshot 1" src="https://github.com/user-attachments/assets/77ae42b1-78fd-4f74-a7c8-6014884e42d9" />  

<img width="1358" height="685" alt="Dashboard Screenshot 2" src="https://github.com/user-attachments/assets/4dec2078-f312-454c-b787-66d66c2d2bf7" />

---
## 💻 Tools Used

Power BI Desktop – Dashboard creation.

Python (pandas + kagglehub) – Data loading & preprocessing.

CSV Dataset – Daily COVID-19 cases by district.

## 💾 Dataset
Loaded from the [Sri Lanka COVID-19 Dataset on Kaggle](https://www.kaggle.com/asheniranga/sri-lanka-covid19-dataset) using **kagglehub**:

```python
# Install dependencies if needed:
# pip install kagglehub[pandas-datasets]

import kagglehub
from kagglehub import KaggleDatasetAdapter

file_path = "daily_situation.csv"

# Load the dataset as a pandas DataFrame
df = kagglehub.load_dataset(
    KaggleDatasetAdapter.PANDAS,
    "asheniranga/sri-lanka-covid19-dataset",
    file_path
)

print(df.head())
''''


