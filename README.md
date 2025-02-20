# DicodingsCollection Dashboard ✨

# Dataset: https://drive.google.com/drive/folders/1PBvnJ96WP7vEXvyxMvKOwW8u5P4sltvc?usp=sharing
# Project Overview
This project analyzes an E-Commerce Public Dataset to understand customer payment behavior. The key focus is to explore the relationship between total payment value and the number of payment installments.
The project includes data analysis, visualization, and a Streamlit dashboard to present insights interactively.

# Business Questions: 
```
1. What is the total payment value grouped by the number of payment installments?
2. How many orders were placed for each number of payment installments?
```

# Dataset Description
The dataset contains transactional data from an e-commerce platform, including:
Order ID: Unique identifier for each order
Payment Value: Total amount paid by the customer
Number of Installments:  Number of payments chosen by the customer

# Key Findings
📌 Customers tend to prefer shorter installment plans, with most payments completed in 1-3 installments.
📌 The total revenue is highest in lower installment ranges, suggesting that customers prefer full payments.
📌 The number of orders decreases as the installment count increases.

# How to Reproduce the Analysis
```
## Setup Environment - Anaconda
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```
```
## Setup Environment - Shell/Terminal
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
```
```
## Run Streamlit Dashboard
streamlit run streamlit_dashboard.py
Technologies Used
Python (Pandas, NumPy, Matplotlib, Seaborn)
Jupyter Notebook for data analysis
Streamlit for interactive dashboard
```
